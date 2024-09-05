import unittest
from unittest.mock import patch, Mock
from order_book import order_book
import requests
class TestOrderBook(unittest.TestCase):

    @patch('order_book.requests.get')
    def test_order_book_success(self, mock_get):
        # Create a mock response object with a successful status code and sample JSON data
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': 'sample'}
        mock_get.return_value = mock_response

        # Call the function under test
        result = order_book()

        # Check that the mock request was made with the correct URL and parameters
        mock_get.assert_called_once_with('https://api.pro.coins.ph/openapi/quote/v1/depth', params={'symbol': 'BTCPHP'})
        
        # Verify the function's return value
        self.assertEqual(result, {'data': 'sample'})

    @patch('order_book.requests.get')
    def test_order_book_failure(self, mock_get):
        # Create a mock response object with a failure status code
        mock_response = Mock()
        mock_response.status_code = 500
        mock_get.return_value = mock_response

        # Ensure that an exception is raised for a non-successful status code
        with self.assertRaises(requests.HTTPError):
            order_book()

if __name__ == '__main__':
    unittest.main()
