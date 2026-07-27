import pytest
from pages.login_page import LoginPage

# Register the custom mark to avoid warnings (or remove @pytest.mark.regression)
@pytest.mark.regression
def test_user_can_login_successfully(page):
    """Test that a user with valid credentials can log in."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "secret_sauce")

    assert login_page.is_logged_in() is True
    assert page.url == "https://www.saucedemo.com/inventory.html"

@pytest.mark.regression
def test_login_fails_with_invalid_password(page):
    """Test that login fails with an invalid password."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("standard_user", "wrong_password")

    error = login_page.get_error_message()
    assert "Username and password do not match" in error

@pytest.mark.regression
def test_login_fails_with_empty_fields(page):
    """Test that login fails when fields are empty."""
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("", "")

    error = login_page.get_error_message()
    assert "Username is required" in error