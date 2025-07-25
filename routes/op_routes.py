from flask import Blueprint, request, jsonify
from services.stack_manager import StackManager
from config.operators import OPERATORS

op_bp = Blueprint('op_bp', __name__, url_prefix='/rpn/op')
stacks = StackManager()

@op_bp.route('', methods=['GET'])
def list_operators():
    """
    List all available operators.
    ---
    tags:
      - Operator
    responses:
      200:
        description: A list of available operators.
    """
    operators = list(OPERATORS.keys())
    return jsonify({"operators": operators})

@op_bp.route('/<op>/stack/<stack_id>', methods=['POST'])
def apply_operator(op, stack_id):
    """
    Apply an operator to a stack.
    ---
    tags:
      - Operator
    parameters:
      - name: op
        in: path
        type: string
        required: true
        description: The operator to apply.
      - name: stack_id
        in: path
        type: string
        required: true
        description: The ID of the stack to apply the operator to.
    responses:
      200:
        description: Operator applied successfully.
      400:
        description: Invalid operator.
    """
    if op in OPERATORS:
        result = stacks.apply_operator(stack_id, op)
        return jsonify({"message": "Operator applied", "stack_id": stack_id, "operator": op, "result": result})
    else:
        return jsonify({"error": "Invalid operator"}), 400