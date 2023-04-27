import socket
from collections import Counter
from urllib.request import urlopen
from bs4 import BeautifulSoup
import threading
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('-w', '--workers', type=int, help='Count workers')
parser.add_argument('-k', '--words', type=int, help='Count words')
args = parser.parse_args()
COUNT_TH = args.workers
COUNT_WORD = args.words
sum_urls = 0


def pars(url):
    try:
        html_page = urlopen(url)
    except Exception:
        print("Bad link")
        return None
    html_content = html_page.read()
    soup = BeautifulSoup(html_content, "html.parser")
    text = soup.get_text()
    words = text.split()
    words.sort()
    return words


def workers(urls, client_sock):
    global sum_urls
    for url in urls:
        pars_url = pars(url)
        if pars_url is None:
            words_json = {f"{url}": "Неверная ссылка"}
        else:
            words_json = {f"{url}": f"{Counter(pars_url).most_common(COUNT_WORD)}"}
        client_sock.sendall(str(words_json).encode())
        sum_urls += 1
        print(sum_urls)


def thread(data, client_sock):
    data = data.decode().strip().split(",")
    count_url = (len(data) + COUNT_TH - 1) // COUNT_TH
    threads = [
        threading.Thread(
            target=workers,
            name=f"thread_{i}",
            args=(
                data[i * count_url : count_url * (i + 1)],
                client_sock,
            ),
        )
        for i in range(COUNT_TH)
    ]

    for th in threads:
        th.start()

    for th in threads:
        th.join()


def handle_client(client_sock, addr):
    buffer = b""
    while True:
        try:
            data = client_sock.recv(1024)
            buffer += data
        except TimeoutError:
            if buffer:
                thread(buffer, client_sock)
            break
    client_sock.close()
    print("client done:", addr)


def run_server():
    server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_sock.bind(("localhost", 1489))
    server_sock.listen(10)

    while True:
        client_sock, addr = server_sock.accept()
        client_sock.settimeout(2)
        print("client connected", addr)
        handle_client(client_sock, addr)


if __name__ == "__main__":
    run_server()
