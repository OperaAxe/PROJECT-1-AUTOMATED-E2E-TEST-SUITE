"""Page object for SauceDemo's product inventory."""

from playwright.sync_api import Locator, Page


class InventoryPage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.title: Locator = page.locator('[data-test="title"]')
        self.product_cards: Locator = page.locator('[data-test="inventory-item"]')
        self.cart_badge: Locator = page.locator('[data-test="shopping-cart-badge"]')
        self.cart_link: Locator = page.locator('[data-test="shopping-cart-link"]')

    def add_product(self, product_slug: str) -> None:
        self.page.locator(f'[data-test="add-to-cart-{product_slug}"]').click()

    def open_cart(self) -> None:
        self.cart_link.click()
