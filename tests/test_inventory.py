"""Catalog checks based on the public SauceDemo training store."""

from playwright.sync_api import expect


def sign_in(login_page) -> None:
    login_page.open()
    login_page.login("standard_user", "secret_sauce")


def test_inventory_renders_six_demo_products(login_page, inventory_page) -> None:
    sign_in(login_page)

    expect(inventory_page.title).to_have_text("Products")
    expect(inventory_page.product_cards).to_have_count(6)
    expect(inventory_page.product_cards.filter(has_text="Sauce Labs Backpack")).to_be_visible()


def test_adding_backpack_updates_cart_badge(login_page, inventory_page) -> None:
    sign_in(login_page)
    inventory_page.add_product("sauce-labs-backpack")

    expect(inventory_page.cart_badge).to_have_text("1")
