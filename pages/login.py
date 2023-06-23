from playwright.sync_api import Locator, Page


class LoginPage:
    def __init__(self, page):
        self.page: Page = page
        self.url: str = "https://www.saucedemo.com"
        self.username_input: Locator = page.locator('[data-test="username"]')
        self.password_input: Locator = page.locator('[data-test="password"]')
        self.login_button: Locator = page.locator('[data-test="login-button"]')

    def goto(self):
        self.page.goto(self.url)

    def sign_in_with_email_and_password(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
