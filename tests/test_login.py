"""Login regression checks against the public SauceDemo training store."""

import pytest
from playwright.sync_api import expect

from pages.inventory_page import InventoryPage


@pytest.mark.regression
def test_standard_user_can_open_inventory(login_page, page, base_url) -> None:
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    expect(page).to_have_url(f"{base_url.rstrip('/')}/inventory.html")
    expect(InventoryPage(page, base_url).title).to_have_text("Products")


@pytest.mark.regression
def test_invalid_password_displays_an_actionable_error(login_page) -> None:
    login_page.open()
    login_page.login("standard_user", "not-the-password")

    expect(login_page.error_message).to_contain_text(
        "Username and password do not match any user in this service"
    )


@pytest.mark.regression
def test_missing_username_is_rejected(login_page) -> None:
    login_page.open()
    login_page.login("", "secret_sauce")

    expect(login_page.error_message).to_contain_text("Username is required")


@pytest.mark.regression
def test_missing_password_is_rejected(login_page) -> None:
    login_page.open()
    login_page.login("standard_user", "")

    expect(login_page.error_message).to_contain_text("Password is required")


@pytest.mark.regression
def test_locked_out_user_cannot_open_inventory(login_page, page, base_url) -> None:
    login_page.open()
    login_page.login("locked_out_user", "secret_sauce")

    expect(login_page.error_message).to_contain_text(
        "Sorry, this user has been locked out"
    )
    expect(page).not_to_have_url(f"{base_url.rstrip('/')}/inventory.html")
