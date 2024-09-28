from unittest.mock import patch
import unittest
import c_mocks_on_tests.external_module


class TestExternalAPI(unittest.TestCase):
    @patch("c_mocks_on_tests.external_module.external_function")
    def test_external_function_mock(self, mock_external_function):
        mock_external_function.return_value = "mocked_value"
        result = c_mocks_on_tests.external_module.external_function()
        self.assertEqual(result, "mocked_value")

    def test_external_function(self):
        result = c_mocks_on_tests.external_module.external_function()
        self.assertEqual(result, "original_value")
