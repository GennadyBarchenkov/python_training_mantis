from selenium.webdriver.common.by import By


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.driver
        self.app.open_home_page()
        wd.find_element(By.NAME, "username").click()
        wd.find_element(By.NAME, "username").clear()
        wd.find_element(By.NAME, "username").send_keys(username)
        wd.find_element(By.NAME, "password").click()
        wd.find_element(By.NAME, "password").clear()
        wd.find_element(By.NAME, "password").send_keys(password)
        wd.find_element(By.XPATH, "//input[@value='Login']").click()

    def logout(self):
        wd = self.app.driver
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def is_logged_in(self):
        wd = self.app.driver
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def is_logged_in_as(self, username):
        wd = self.app.driver
        return self.get_set_logged_user() == username

    def get_set_logged_user(self):
        wd = self.app.driver
        return wd.find_element(By.CSS_SELECTOR, "td.login-info-left span").text

    def ensure_logout(self):
        wd = self.app.driver
        if self.is_logged_in():
            self.logout()

    def ensure_login(self, username, password):
        wd = self.app.driver
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)