import unittest
from unittest.mock import patch
from app import create_app
from app.config import TestConfig

class TestWeatherAPI(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config_class=TestConfig).test_client()
        self.app.testing = True

    @patch('app.extensions.cache')
    def test_get_weather_api(self, mock_cache):
        # Mock the cache methods (get and set) to prevent actual Redis interaction
        mock_cache.get.return_value = None
        mock_cache.set.return_value = True

        response = self.app.get('/weather?location=toronto')

        #Assertions
        self.assertEqual(response.status_code, 200)
        response_data = response.get_json()
        self.assertTrue(response_data['success'])
        self.assertIn('data', response_data)
        self.assertIn('values', response_data['data'])
