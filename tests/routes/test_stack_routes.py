
import unittest
from unittest.mock import patch
from app import create_app

class TestStackRoutes(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()

    @patch('services.stack_manager.StackManager.list_stacks')
    def test_list_stacks(self, mock_list_stacks):
        mock_list_stacks.return_value = ['stack1', 'stack2']
        response = self.client.get('/rpn/stack')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'Stacks': ['stack1', 'stack2']})

    @patch('services.stack_manager.StackManager.create_stack')
    def test_create_stack(self, mock_create_stack):
        mock_create_stack.return_value = 'new_stack'
        response = self.client.post('/rpn/stack')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': 'Stack created', 'stack_id': 'new_stack'})

    @patch('services.stack_manager.StackManager.get_stack')
    def test_get_stack(self, mock_get_stack):
        mock_get_stack.return_value = [1, 2, 3]
        response = self.client.get('/rpn/stack/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'stack_id': '123', 'stack': [1, 2, 3]})

    @patch('services.stack_manager.StackManager.delete_stack')
    def test_delete_stack(self, mock_delete_stack):
        response = self.client.delete('/rpn/stack/123')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Stack deleted', 'stack_id': '123'})
        mock_delete_stack.assert_called_with('123')

    @patch('services.stack_manager.StackManager.push_value')
    def test_push_value_to_stack(self, mock_push_value):
        response = self.client.post('/rpn/stack/123', json={'value': 10})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'Value pushed', 'stack_id': '123', 'value': 10})
        mock_push_value.assert_called_with(123, 10)

if __name__ == '__main__':
    unittest.main()
