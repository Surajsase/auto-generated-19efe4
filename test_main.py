import unittest
from unittest.mock import patch
from main import get_bitcoin_price

class TestGetBitcoinPrice(unittest.TestCase):
    @patch('requests.get')
    def test_get_bitcoin_price(self, mock_get):
        mock_response = {'USD': 50000}
        mock_get.return_value.json.return_value = mock_response
        self.assertEqual(get_bitcoin_price(), mock_response['USD'])

    @patch('requests.get')
    def test_get_bitcoin_price_not_available(self, mock_get):
        mock_response = {}
        mock_get.return_value.json.return_value = mock_response
        self.assertEqual(get_bitcoin_price(), 'Price not available')

if __name__ == '__main__':
    unittest.main()