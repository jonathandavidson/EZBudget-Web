from flask import Blueprint, request

api = Blueprint('api', __name__)

# Create account route
@api.route('/accounts', methods=['POST'])
def create_account():
    # Logic to create an account
    return {"message": "Account created successfully"}

# Read account route
@api.route('/accounts/<account_id>', methods=['GET'])
def read_account(account_id):
    # Logic to read an account
    return {"message": f"Reading account with ID: {account_id}"}

# Delete account route
@api.route('/accounts/<account_id>', methods=['DELETE'])
def delete_account(account_id):
    # Logic to delete an account
    return {"message": f"Deleted account with ID: {account_id}"}
