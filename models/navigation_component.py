from playwright.sync_api import Locator, Page

from models.sidebar_component import SidebarComponent


class NavigationComponent:
    def __init__(self, page: Page):
        self.page: Page = page
        self.sidebar_button: Locator = page.get_by_role("button", name="Open Menu")
        self.sidebar_component = SidebarComponent(page)

    def toggle_sidebar(self):
        self.sidebar_button.click()

    def logout(self):
        self.sidebar_component.logout()


