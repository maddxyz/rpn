
import unittest
from unittest.mock import patch
from app import create_app

class TestOpRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    def test_list_operators(self):
        response = self.client.get('/rpn/op')
        self.assertEqual(response.status_code, 200)
        self.assertIn('operators', response.json)

    @patch('services.stack_manager.StackManager.apply_operator')
    def test_apply_operator(self, mock_apply_operator):
        mock_apply_operator.return_value = 10
        response = self.client.post('/rpn/op/+/stack/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Operator applied', 'stack_id': '123', 'operator': '+', 'result': 10})
        mock_apply_operator.assert_called_with('123', '+')

    def test_apply_invalid_operator(self):
        response = self.client.post('/rpn/op/invalid_op/stack/123')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json, {'error': 'Invalid operator'})

if __name__ == '__main__':
    unittest.main()
