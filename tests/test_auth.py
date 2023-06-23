import re

from playwright.sync_api import Page
from playwright.sync_api import expect

from models.login_page import LoginPage
from models.navigation_component import NavigationComponent
from models.sidebar_component import SidebarComponent


def test_authentication_workflow(page: Page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.sign_in_with_email_and_password("standard_user", "secret_sauce")
    expect(page).to_have_url(re.compile(".*inventory.html"))
    navigation = NavigationComponent(page)
    navigation.toggle_sidebar()
    navigation.logout()
    page.close()
