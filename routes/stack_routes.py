from flask import Blueprint, request, jsonify
from services.stack_manager import StackManager

stack_bp = Blueprint('stack_bp', __name__, url_prefix='/rpn/stack')
stacks = StackManager()

@stack_bp.route('', methods=['GET'])
def list_stacks():
    """
    List all available stacks.
    ---
    tags:
      - Stack
    responses:
      200:
        description: A list of available stacks.
    """
    all_stacks = stacks.list_stacks()
    return jsonify({"Stacks": all_stacks})

@stack_bp.route('', methods=['POST'])
def create_stack():
    """
    Create a new stack.
    ---
    tags:
      - Stack
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: request_body
          required:
            - stack_id
          properties:
            stack_id:
              type: string
              description: The ID of the stack to create.
    responses:
      201:
        description: Stack created successfully.
    """
    stack_id = stacks.create_stack()
    return jsonify({"message" : "Stack created", "stack_id" : stack_id}), 201

@stack_bp.route('/<stack_id>', methods=['GET'])
def get_stack(stack_id):
    """
    Get a stack by ID.
    ---
    tags:
      - Stack
    parameters:
      - name: stack_id
        in: path
        type: string
        required: true
        description: The ID of the stack to retrieve.
    responses:
      200:
        description: Stack retrieved successfully.
    """
    stack = stacks.get_stack(stack_id)
    return jsonify({"stack_id": stack_id, "stack": stack})

@stack_bp.route('/<stack_id>', methods=['DELETE'])
def delete_stack(stack_id):
    """
    Delete a stack by ID.
    ---
    tags:
      - Stack
    parameters:
      - name: stack_id
        in: path
        type: string
        required: true
        description: The ID of the stack to delete.
    responses:
      200:
        description: Stack deleted successfully.
    """
    stacks.delete_stack(stack_id)
    return jsonify({"message": "Stack deleted", "stack_id": stack_id})

@stack_bp.route('/<stack_id>', methods=['POST'])
def push_value_to_stack(stack_id):
    """
    Push a value to a stack.
    ---
    tags:
      - Stack
    parameters:
      - name: stack_id
        in: path
        type: string
        required: true
        description: The ID of the stack to push the value to.
      - name: body
        in: body
        required: true
        schema:
          id: request_body
          required:
            - value
          properties:
            value:
              type: number
              description: The value to push to the stack.
    responses:
      200:
        description: Value pushed successfully.
    """
    value = request.json.get('value')
    stacks.push_value(int(stack_id), value)
    return jsonify({"message": "Value pushed", "stack_id": stack_id, "value": value})