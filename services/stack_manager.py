from config.operators import OPERATORS

class StackManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(StackManager, cls).__new__(cls)
            cls._instance.stacks = {}
            cls._instance.counter = 0
        return cls._instance

    def create_stack(self):
        stack_id = self.counter
        self.counter += 1
        self.stacks[stack_id] = []
        return stack_id
    
    def list_stacks(self):
        return {k: v for k, v in self.stacks.items()}
    
    def get_stack(self, stack_id):
        return self.stacks.get(stack_id)
    
    def delete_stack(self, stack_id):
        return self.stacks.pop(stack_id, None) is not None
    
    def push_value(self, stack_id, value):
        print(self.stacks.keys())
        if stack_id not in self.stacks:
            raise ValueError("Stack not found.")
        self.stacks[stack_id].append(value)

    def apply_operator(self, stack_id, op):
        if stack_id not in self.stacks:
            raise ValueError("Stack not found.")
        stack = self.stacks[stack_id]
        if len(stack) < 2 :
            raise ValueError("Stack doesn't contain enough values.")
        if op not in OPERATORS:
            raise ValueError("Operator not recognized.")
        value_one = stack.pop()
        value_two = stack.pop()
        result = OPERATORS[op](value_one, value_two)
        stack.append(result)
        return result
