"""Tests for the accounts API endpoints."""

def test_list_accounts_no_auth(client):
    """Test that the list accounts endpoint returns 401 when no auth is provided."""
    response = client.get('/api/accounts')
    assert response.status_code == 401
