import socket
import time
import unittest
import subprocess


class TestServer(unittest.TestCase):
    def setUp(self):
        self.server_process = subprocess.Popen(
            ["python3", "server.py", "-w", "10", "-k", "5"]
        )
        time.sleep(1)

    def tearDown(self):
        self.server_process.terminate()
        self.server_process.wait()

    def test_connection(self):
        server_address = ("localhost", 1489)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex(server_address)
        s.close()
        self.assertEqual(result, 0)

    def test_correct_url(self):
        url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
        expected_result = {
            url: "[('the', 454), ('Python', 337), ('and', 260), ('from', 247), ('on', 228)]"
        }
        server_address = ("localhost", 1489)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(server_address)
        s.sendall(bytes(url.encode()))
        while True:
            data = s.recv(1024)
            if not data:
                break
            else:
                result = data.decode()
                self.assertEqual(result, str(expected_result))
        s.close()

    def test_incorrect_url(self):
        url = "ttps://en.wikipedia.org/wiki/Python_language"
        expected_result = {url: "Неверная ссылка"}
        server_address = ("localhost", 1489)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect(server_address)
        s.sendall(bytes(url.encode()))
        while True:
            data = s.recv(1024)
            if not data:
                break
            else:
                result = data.decode()
                self.assertEqual(result, str(expected_result))
        s.close()

    def test_multiple_urls(self):
        # Данные на вики могут обновиться
        urls = [
            "https://en.wikipedia.org/wiki/Namikawa_S%C5%8Dsuke",
            "https://en.wikipedia.org/wiki/Python_(programming_language)",
            "https://en.wikipedia.org/wiki/OpenAI",
            "https://en.wikipedia.org/wiki/Artificial_intelligence",
            "https://en.wikipedia.org/wiki/Neural_network",
        ]
        expected_results = [
            {urls[0]: "[('the', 56), ('of', 40), ('and', 23), ('a', 19), ('in', 17)]"},
            {
                urls[
                    1
                ]: "[('the', 454), ('Python', 337), ('and', 260), ('from', 247), ('on', 228)]"
            },
            {
                urls[
                    2
                ]: "[('the', 326), ('to', 202), ('of', 186), ('a', 164), ('on', 163)]"
            },
            {
                urls[
                    3
                ]: "[('the', 627), ('and', 476), ('of', 475), ('to', 297), ('^', 256)]"
            },
            {
                urls[
                    4
                ]: "[('of', 170), ('the', 167), ('and', 122), ('to', 89), ('in', 80)]"
            },
        ]
        for i in range(len(urls)):
            server_address = ("localhost", 1489)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect(server_address)
            s.sendall(bytes(urls[i].encode()))
            while True:
                data = s.recv(1024)
                if not data:
                    break
                else:
                    result = data.decode()
                    self.assertEqual(result, str(expected_results[i]))
            s.close()
