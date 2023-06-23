from playwright.sync_api import Page

from pages.login import LoginPage


def test_login_email_password(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.sign_in_with_email_and_password("standard_user", "secret_sauce")
    # TODO: add assertion
    page.close()
