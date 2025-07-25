
import unittest
from services.stack_manager import StackManager

class TestStackManager(unittest.TestCase):

    def setUp(self):
        # Reset the singleton instance for each test
        StackManager._instance = None
        self.stack_manager = StackManager()

    def test_create_stack(self):
        stack_id = self.stack_manager.create_stack()
        self.assertEqual(stack_id, 0)
        self.assertIn(0, self.stack_manager.stacks)
        stack_id_2 = self.stack_manager.create_stack()
        self.assertEqual(stack_id_2, 1)

    def test_list_stacks(self):
        self.stack_manager.create_stack()
        self.stack_manager.create_stack()
        self.assertEqual(self.stack_manager.list_stacks(), {0: [], 1: []})

    def test_get_stack(self):
        stack_id = self.stack_manager.create_stack()
        self.stack_manager.push_value(stack_id, 10)
        self.assertEqual(self.stack_manager.get_stack(stack_id), [10])

    def test_delete_stack(self):
        stack_id = self.stack_manager.create_stack()
        self.assertTrue(self.stack_manager.delete_stack(stack_id))
        self.assertNotIn(stack_id, self.stack_manager.stacks)
        self.assertFalse(self.stack_manager.delete_stack(999))

    def test_push_value(self):
        stack_id = self.stack_manager.create_stack()
        self.stack_manager.push_value(stack_id, 10)
        self.assertEqual(self.stack_manager.get_stack(stack_id), [10])
        self.stack_manager.push_value(stack_id, 20)
        self.assertEqual(self.stack_manager.get_stack(stack_id), [10, 20])

    def test_push_value_to_nonexistent_stack(self):
        with self.assertRaises(ValueError):
            self.stack_manager.push_value(999, 10)

    def test_apply_operator(self):
        stack_id = self.stack_manager.create_stack()
        self.stack_manager.push_value(stack_id, 10)
        self.stack_manager.push_value(stack_id, 20)
        result = self.stack_manager.apply_operator(stack_id, '+')
        self.assertEqual(result, 30)
        self.assertEqual(self.stack_manager.get_stack(stack_id), [30])

    def test_apply_operator_to_nonexistent_stack(self):
        with self.assertRaises(ValueError):
            self.stack_manager.apply_operator(999, '+')

    def test_apply_operator_with_insufficient_values(self):
        stack_id = self.stack_manager.create_stack()
        self.stack_manager.push_value(stack_id, 10)
        with self.assertRaises(ValueError):
            self.stack_manager.apply_operator(stack_id, '+')

    def test_apply_unrecognized_operator(self):
        stack_id = self.stack_manager.create_stack()
        self.stack_manager.push_value(stack_id, 10)
        self.stack_manager.push_value(stack_id, 20)
        with self.assertRaises(ValueError):
            self.stack_manager.apply_operator(stack_id, 'invalid_op')

    def test_singleton(self):
        sm1 = StackManager()
        sm2 = StackManager()
        self.assertIs(sm1, sm2)

if __name__ == '__main__':
    unittest.main()
