class LoginPage:
    def __init__(self, page):
        self.page = page
        # SauceDemo selectors
        self.username_input = "#user-name"
        self.password_input = "#password"
        self.login_button = "#login-button"
        self.error_message = '[data-test="error"]'
        self.welcome_message = ".app_logo"   # the logo appears after login

    def goto(self):
        # Navigate to the demo site
        self.page.goto("https://www.saucedemo.com/")

    def login(self, username: str, password: str):
        self.page.fill(self.username_input, username)
        self.page.fill(self.password_input, password)
        self.page.click(self.login_button)

    def get_error_message(self):
        return self.page.text_content(self.error_message)

    def is_logged_in(self):
        # After successful login, we are on the inventory page
        return self.page.url == "https://www.saucedemo.com/inventory.html"