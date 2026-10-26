"""Shared browser fixtures for the SauceDemo QA playbook."""

import os

import pytest
from playwright.sync_api import BrowserContext, Page

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("BASE_URL", "https://www.saucedemo.com/").rstrip("/") + "/"


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    yield page
    page.close()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args: dict) -> dict:
    return {
        **browser_context_args,
        "viewport": {"width": 1440, "height": 1000},
        "locale": "en-US",
    }


@pytest.fixture
def login_page(page: Page, base_url: str) -> LoginPage:
    return LoginPage(page, base_url)


@pytest.fixture
def inventory_page(page: Page, base_url: str) -> InventoryPage:
    return InventoryPage(page, base_url)


@pytest.fixture
def cart_page(page: Page, base_url: str) -> CartPage:
    return CartPage(page, base_url)
