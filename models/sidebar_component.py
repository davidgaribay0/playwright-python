from playwright.sync_api import Locator, Page


class SidebarComponent:
    def __init__(self, page: Page):
        self.page: Page = page
        self.logout_button: Locator = page.get_by_text("Logout")

    def logout(self):
        self.logout_button.click()
