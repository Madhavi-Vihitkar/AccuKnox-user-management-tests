from playwright.sync_api import Page
def __init__(self, page: Page):
self.page = page
# Locators — update if your OrangeHRM instance uses different attributes
self.menu_admin = "text=Admin"
self.btn_add = "button:has-text('Add')"
self.input_username = "input[name='username']"
self.input_employee = "input[placeholder='Type for hints...']"
self.select_user_role = "select[name='userRole']"
self.select_status = "select[name='status']"
self.input_password = "input[name='password']"
self.input_confirm_password = "input[name='confirmPassword']"
self.btn_save = "button:has-text('Save')"
self.search_username = "input[name='searchSystemUser[userName]']"
self.search_btn = "button:has-text('Search')"
self.result_rows = "table tbody tr"
self.edit_icon = "button[title='Edit']"
self.delete_button = "button:has-text('Delete')"
self.confirm_delete = "button:has-text('Yes, Delete')"


def goto_admin(self):
self.page.click(self.menu_admin)
self.page.wait_for_selector(self.search_username)


def add_user(self, username: str, employee: str, role: str = 'ESS', status: str = 'Enabled', password: Optional[str] = None):
self.page.click(self.btn_add)
self.page.wait_for_selector(self.input_username)
self.page.fill(self.input_username, username)
self.page.fill(self.input_employee, employee)
self.page.select_option(self.select_user_role, label=role)
self.page.select_option(self.select_status, label=status)
if password:
self.page.fill(self.input_password, password)
self.page.fill(self.input_confirm_password, password)
self.page.click(self.btn_save)
# Wait for save to complete — check for success message or the presence in table
self.page.wait_for_timeout(1000)


def search_user(self, username: str):
self.page.fill(self.search_username, username)
self.page.click(self.search_btn)
self.page.wait_for_selector(self.result_rows)
rows = self.page.query_selector_all(self.result_rows)
return rows


def open_first_result_for_edit(self):
# Click first row's Edit (adjust selector if needed)
self.page.click(f"{self.result_rows} >> {self.edit_icon}")
self.page.wait_for_selector(self.input_username)


def update_username(self, new_username: str):
self.page.fill(self.input_username, new_username)
self.page.click(self.btn_save)
self.page.wait_for_timeout(800)


def delete_first_result(self):
# Adjust depending on list UI; here we click delete in the row
self.page.click(f"{self.result_rows} >> button:has-text('Delete')")
self.page.click(self.confirm_delete)
self.page.wait_for_timeout(800)
