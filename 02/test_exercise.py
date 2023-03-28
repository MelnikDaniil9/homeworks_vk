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
        params = [
            (
                params_json,
                ["key13", "key33", "key56", "key55"],
                ["value13", "value33", "value12", "value0"],
            ),
            (
                params_json,
                [],
                ["value13", "value33", "value12"],
            ),
            (
                params_json,
                ["key13", "key33"],
                [],
            ),
            (
                "",
                ["key13", "key33"],
                ["value13", "value33", "value12"],
            ),
        ]
        for json_str, required_fields, keywords in params:
            with self.subTest():
                self.assertEqual(
                    parse_json(
                        json_str, self.keyword_callback_mock, required_fields, keywords
                    ),
                    None,
                )
        mock_calls = [
            mock.call("value13"),
            mock.call("value33"),
            mock.call("value12"),
            mock.call("value0"),
        ]
        self.assertEqual(self.keyword_callback_mock.mock_calls, mock_calls)
        self.assertEqual(self.keyword_callback_mock.call_count, 4)
