import unittest
from unittest import mock

from exercise1 import SomeModel, Mood
from exercise1 import predict_message_mood


class TestPredictMessageMood(unittest.TestCase):
    def setUp(self):
        self.model_obj = SomeModel()

    def test_predict_message_neud(self):
        with mock.patch("exercise1.SomeModel.predict") as mock_predict:
            mock_predict.return_value = -1
            self.assertEqual(
                predict_message_mood("as", self.model_obj), Mood.NEUD.value
            )
            mock_predict.return_value = 0
            self.assertEqual(predict_message_mood("1", self.model_obj), Mood.NEUD.value)
            mock_calls = [
                mock.call("as"),
                mock.call("1"),
            ]
            self.assertEqual(mock_calls, mock_predict.mock_calls)

    def test_predict_message_norm(self):
        with mock.patch("exercise1.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.3
            self.assertEqual(
                predict_message_mood("Ifas", self.model_obj), Mood.NORM.value
            )
            mock_predict.return_value = 0.5
            self.assertEqual(
                predict_message_mood("saxz", self.model_obj), Mood.NORM.value
            )
            mock_predict.return_value = 0.8
            self.assertEqual(
                predict_message_mood("asd1", self.model_obj), Mood.NORM.value
            )
            mock_calls = [
                mock.call("Ifas"),
                mock.call("saxz"),
                mock.call("asd1"),
            ]
            self.assertEqual(mock_calls, mock_predict.mock_calls)

    def test_predict_message_otl(self):
        with mock.patch("exercise1.SomeModel.predict") as mock_predict:
            mock_predict.return_value = 0.9
            self.assertEqual(
                predict_message_mood("asa", self.model_obj), Mood.OTL.value
            )
            mock_predict.return_value = 1
            self.assertEqual(
                predict_message_mood("asa", self.model_obj), Mood.OTL.value
            )
            mock_calls = [
                mock.call("asa"),
                mock.call("asa"),
            ]
            self.assertEqual(mock_calls, mock_predict.mock_calls)

    def test_predict_message_error_call(self):
        with self.assertRaises(AssertionError):
            predict_message_mood("", self.model_obj, 0.1, 0.3)
        with self.assertRaises(AssertionError):
            predict_message_mood("", self.model_obj, 1, 0)
        with self.assertRaises(AssertionError):
            predict_message_mood("str", self.model_obj, 0.1, 0.1)
