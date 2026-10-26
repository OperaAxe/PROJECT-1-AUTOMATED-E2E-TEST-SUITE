"""Page object for the public SauceDemo login form."""

from playwright.sync_api import Locator, Page


class LoginPage:
    def __init__(self, page: Page, base_url: str) -> None:
        self.page = page
        self.base_url = base_url.rstrip("/")
        self.username_input: Locator = page.locator('[data-test="username"]')
        self.password_input: Locator = page.locator('[data-test="password"]')
        self.login_button: Locator = page.locator('[data-test="login-button"]')
        self.error_message: Locator = page.locator('[data-test="error"]')

    def open(self) -> None:
        self.page.goto(self.base_url)

    def login(self, username: str, password: str) -> None:
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    def error_text(self) -> str:
        return (self.error_message.text_content() or "").strip()
