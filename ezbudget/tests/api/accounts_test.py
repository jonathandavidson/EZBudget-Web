def test_list_accounts_no_auth(client):
    response = client.get('/api/accounts')
    assert response.status_code == 401
