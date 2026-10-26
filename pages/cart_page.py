"""Page object for the SauceDemo cart."""

from playwright.sync_api import Locator, Page


class CartPage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.items: Locator = page.locator(".cart_item")
        self.cart_badge: Locator = page.locator('[data-test="shopping-cart-badge"]')

    def remove_product(self, product_slug: str) -> None:
        self.page.locator(f'[data-test="remove-{product_slug}"]').click()
