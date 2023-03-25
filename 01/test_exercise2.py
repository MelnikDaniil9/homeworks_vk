import io
import unittest
from unittest import mock
from exercise2 import reader


class TestReader(unittest.TestCase):
    read_data = (
        "а Роза упала на лапу Азора\n"
        "Карл у Клары украл кораллы,\n"
        "А Клара у Карла украла кларнет.\n"
        "Короле́ва Клара сильно карала\n"
        "Кавале́ра Карла за кражу кораллов!"
    )
    search_words = ["роза", "карла"]
    expected_line = [
        "а Роза упала на лапу Азора\n",
        "А Клара у Карла украла кларнет.\n",
        "Кавале́ра Карла за кражу кораллов!",
    ]

    def test_reader_str(self):
        mock_obj = mock.mock_open(read_data=self.read_data)
        with mock.patch("exercise2.open", mock_obj):
            result_line = list(reader("file", self.search_words))
        self.assertEqual(result_line, self.expected_line)
        search_words = ["роз"]
        expected_line = []
        with mock.patch("exercise2.open", mock_obj):
            result_line = list(reader("file", search_words))
        self.assertEqual(result_line, expected_line)

    def test_reader_file_obj(self):
        file = io.StringIO(self.read_data)
        result_line = list(reader(file, self.search_words))
        self.assertEqual(result_line, self.expected_line)
        search_words = ["Роз"]
        expected_line = []
        file = io.StringIO(self.read_data)
        result_line = list(reader(file, search_words))
        self.assertEqual(result_line, expected_line)
