import unittest
from unittest import mock
from client import create_threads, send_data


class TestClient(unittest.TestCase):
    # По умолчанию 5 потоков
    def test_create_threads(self):
        with mock.patch("client.send_data") as mock_send_data:
            mock_send_data.return_value = "Отправлено на сервер"
            data = "https://en.wikipedia.org/wiki/Namikawa_S%C5%8Dsuke, " \
                   "https://en.wikipedia.org/wiki/Gr%C3%A9gory_Pastel, https://en.wikipedia.org/wiki/Stolyarenko, " \
                   "https://en.wikipedia.org/wiki/Homosexuality_and_the_United_Church_of_Canada, " \
                   "https://en.wikipedia.org/wiki/The_Natural_Economic_Order, " \
                   "https://en.wikipedia.org/wiki/Namikawa_S%C5%8Dsuke, " \
                   "https://en.wikipedia.org/wiki/Gr%C3%A9gory_Pastel, https://en.wikipedia.org/wiki/Stolyarenko, " \
                   "https://en.wikipedia.org/wiki/Homosexuality_and_the_United_Church_of_Canada, " \
                   "https://en.wikipedia.org/wiki/The_Natural_Economic_Order"
            create_threads(data)
            mock_calls = [
                mock.call([
                    "https://en.wikipedia.org/wiki/Namikawa_S%C5%8Dsuke",
                    " https://en.wikipedia.org/wiki/Gr%C3%A9gory_Pastel"
                ]),
                mock.call([
                    " https://en.wikipedia.org/wiki/Stolyarenko",
                    " https://en.wikipedia.org/wiki/Homosexuality_and_the_United_Church_of_Canada"
                ]),
                mock.call([
                    " https://en.wikipedia.org/wiki/The_Natural_Economic_Order",
                    " https://en.wikipedia.org/wiki/Namikawa_S%C5%8Dsuke"
                ]),
                mock.call([
                    " https://en.wikipedia.org/wiki/Gr%C3%A9gory_Pastel",
                    " https://en.wikipedia.org/wiki/Stolyarenko"
                ]),
                mock.call([
                    " https://en.wikipedia.org/wiki/Homosexuality_and_the_United_Church_of_Canada",
                    " https://en.wikipedia.org/wiki/The_Natural_Economic_Order"
                ]),
            ]
            self.assertEqual(mock_send_data.mock_calls, mock_calls)
            self.assertEqual(mock_send_data.call_count, 5)

    def test_send_data(self):
        # Проверка, что при получении пустого ответа сокет закрывается
        with mock.patch('socket.socket') as mock_socket:
            instance = mock_socket.return_value
            instance.recv.return_value = b''
            send_data(['test'])
            instance.connect.assert_called_once_with(('localhost', 1489))
            instance.sendall.assert_called_once_with(b'test')
            instance.close.assert_called_once()

