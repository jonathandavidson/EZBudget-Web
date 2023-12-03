"""This module contains the API views for the EZBudget application."""
from flask import Blueprint
from .decorators.authenticated import auth_required


api = Blueprint('api', __name__)

@api.route('/accounts', methods=['GET'])
@auth_required
def list_accounts():
    """Logic to list all accounts"""
    return {"message": "Accounts listed successfully"}

@api.route('/accounts', methods=['POST'])
@auth_required
def create_account():
    """Logic to create an account"""
    return {"message": "Account created successfully"}

@api.route('/accounts/<account_id>', methods=['GET'])
@auth_required
def read_account(account_id):
    """Logic to read an account"""
    return {"message": f"Reading account with ID: {account_id}"}

@api.route('/accounts/<account_id>', methods=['DELETE'])
@auth_required
def delete_account(account_id):
    """Logic to delete an account"""
    return {"message": f"Deleted account with ID: {account_id}"}
