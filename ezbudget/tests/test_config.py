"""Test configuration."""

COGNITO_CLIENT_ID = '54fe56543d9e3509c8a54a7ebe'
COGNITO_CLIENT_SECRET = '6ca1b60483b600d67bc3a3b2acf74b2c40a46556b64bc7bee37'
COGNITO_DOMAIN = 'ez-budget.auth.us-west-2.amazoncognito.com'
COGNITO_REDIRECT_URI = 'http://localhost:8080/authenticate'
COGNITO_USER_POOL_ID = 'us-west-2_b2C40a465'
COGNITO_REGION_NAME = 'us-west-2'
# pylint: disable-next=line-too-long
COGNITO_JWK_URL = 'https://cognito-idp.us-west-2.amazonaws.com/us-west-2_b2C40a465/.well-known/jwks.json'
