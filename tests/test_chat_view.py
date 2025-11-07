from django.test import TestCase, Client
from unittest.mock import patch


class ChatViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('main.create_agent_executor')
    def test_api_chat_returns_mocked_output(self, mock_create):
        class DummyExecutor:
            def invoke(self, payload):
                return {'output': 'mocked response'}

        mock_create.return_value = DummyExecutor()

        resp = self.client.post('/api/chat/', data='{"input":"hello"}', content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        self.assertIn('mocked response', resp.json().get('output', ''))
