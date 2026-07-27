import pytest
from playwright.sync_api import Page, BrowserContext

@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    """Create a new page for each test."""
    page = context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Set up browser context with custom viewport."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "ignore_https_errors": True,
    }