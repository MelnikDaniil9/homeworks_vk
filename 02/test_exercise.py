import unittest
from unittest import mock
from exercise import parse_json


class TestParserJson(unittest.TestCase):
    def setUp(self) -> None:
        self.keyword_callback_mock = mock.Mock()

    def test_vk_example_from_task(self):
        self.assertEqual(
            parse_json(
                '{"key1": "Word1 word2", "key2": "word2 word3"}',
                self.keyword_callback_mock,
                ["key1"],
                ["word2"],
            ),
            None,
        )
        self.assertEqual(
            self.keyword_callback_mock.mock_calls, [mock.call("key1", "word2")]
        )
        self.assertEqual(self.keyword_callback_mock.call_count, 1)

    def test_calls_parse_json(self):
        params_json = """{
                "key11": "value1",
                "key12": {
                    "key21": "value21",
                    "key22": {
                        "key33": "value33 value12",
                        "key34": {
                            "key44": {
                                "key55" : "value55",
                                "key56" : "value0"
                            }
                        }
                    }
                },
                "key13": "value13"
            }"""
        # Если keyword_callback = None
        self.assertEqual(
            parse_json(
                params_json,
                None,
                ["key13", "key33", "key56", "key55"],
                ["value13", "value33", "value12", "value0"],
            ),
            None,
        )
        self.keyword_callback_mock.assert_not_called()
        self.assertEqual(self.keyword_callback_mock.call_count, 0)
        # Если json_str = None
        self.assertEqual(
            parse_json(
                None,
                self.keyword_callback_mock,
                ["key13", "key33", "key56", "key55"],
                ["value13", "value33", "value12", "value0"],
            ),
            None,
        )
        self.keyword_callback_mock.assert_not_called()
        self.assertEqual(self.keyword_callback_mock.call_count, 0)
        # Если keywords = None
        self.assertEqual(
            parse_json(
                params_json,
                self.keyword_callback_mock,
                ["key13", "key33", "key56", "key55"],
                None,
            ),
            None,
        )
        self.keyword_callback_mock.assert_not_called()
        self.assertEqual(self.keyword_callback_mock.call_count, 0)
        # Если required_fields = None
        self.assertEqual(
            parse_json(
                params_json,
                self.keyword_callback_mock,
                None,
                ["value13", "value33", "value12", "value0"],
            ),
            None,
        )
        self.keyword_callback_mock.assert_not_called()
        self.assertEqual(self.keyword_callback_mock.call_count, 0)
        # Тест с несколькими найденными required_field и keyword
        self.assertEqual(
            parse_json(
                params_json,
                self.keyword_callback_mock,
                ["key13", "key33", "key56", "key55"],
                ["value13", "value33", "value12", "value0"],
            ),
            None,
        )
        mock_calls = [
            mock.call("key13", "value13"),
            mock.call("key33", "value33"),
            mock.call("key33", "value12"),
            mock.call("key56", "value0"),
        ]
        # Проверкa аргументов, с которыми были вызваны колбеки
        self.assertEqual(self.keyword_callback_mock.mock_calls, mock_calls)
        self.assertEqual(self.keyword_callback_mock.call_count, 4)
