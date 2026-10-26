"""Cart checks using the real demo storefront's publicly documented test account."""

from playwright.sync_api import expect


def test_added_item_can_be_reviewed_and_removed(
    login_page, inventory_page, cart_page, page
) -> None:
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    inventory_page.add_product("sauce-labs-backpack")
    inventory_page.add_product("sauce-labs-bike-light")

    expect(inventory_page.cart_badge).to_have_text("2")
    inventory_page.open_cart()

    expect(cart_page.items).to_have_count(2)
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()
    expect(page.get_by_text("Sauce Labs Bike Light", exact=True)).to_be_visible()

    cart_page.remove_product("sauce-labs-backpack")

    expect(cart_page.items).to_have_count(1)
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_have_count(0)
    expect(page.get_by_text("Sauce Labs Bike Light", exact=True)).to_be_visible()
