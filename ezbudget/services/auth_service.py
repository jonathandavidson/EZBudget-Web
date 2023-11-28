import boto3
import os
from flask import current_app

def request_token(authorization_code):
  config = current_app.config
  client_id = config.get('COGNITO_CLIENT_ID')
  client_secret = config.get('COGNITO_CLIENT_SECRET')
  redirect_uri = config.get('COGNITO_REDIRECT_URI')
  user_pool_id = config.get('COGNITO_USER_POOL_ID')
  region_name = config.get('COGNITO_REGION_NAME')

  client = boto3.client('cognito-idp', region_name=region_name)

  response = client.initiate_auth(
    AuthFlow='AUTHORIZATION_CODE',
    AuthParameters={
      'client_id': client_id,
      'client_secret': client_secret,
      'redirect_uri': redirect_uri,
      'code': authorization_code
    },
    ClientMetadata={
      'Authorization': 'Bearer ' + authorization_code
    },
    ClientId=client_id
    # UserPoolId=user_pool_id
    # AuthProvider=auth_provider
  )

  return response['AuthenticationResult']['AccessToken']
