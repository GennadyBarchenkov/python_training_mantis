from selenium.webdriver.common.by import By
from model.project import Project
import string
import random


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    project_cache = None

    def get_project_list(self):
        if self.project_cache is None:
            wd = self.app.driver
            self.open_manage_project_page()
            self.project_cache = []
            for element in wd.find_elements(By.XPATH, "//td/a[contains(@href,'manage_proj_edit_page.php?project_id=')]"):
                id = element.get_attribute("href").replace(self.app.base_url + 'manage_proj_edit_page.php?project_id=', '')
                name_text = element.text
                self.project_cache.append(Project(id=id, name=name_text))
        return list(self.project_cache)

    def open_manage_project_page(self):
        wd = self.app.driver
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element(By.LINK_TEXT, "Manage").click()
            wd.find_element(By.LINK_TEXT, "Manage Projects").click()

    def add_new_project(self, project):
        wd = self.app.driver
        self.open_manage_project_page()
        wd.find_element(By.CSS_SELECTOR, "input[value='Create New Project']").click()
        self.fill_project_form(project)
        wd.find_element(By.CSS_SELECTOR, "input[value='Add Project']").click()
        self.open_manage_project_page()
        self.project_cache = None

    def fill_project_form(self, project):
        self.change_field_value("name", project.name)

    def change_field_value(self, field_name, text):
        wd = self.app.driver
        if text is not None:
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return prefix + "".join((random.choice(symbols) for i in range(random.randrange(maxlen))))

    def delete_project_by_id(self, id):
        wd = self.app.driver
        self.open_manage_project_page()
        self.select_project_by_id(id)
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        wd.find_element(By.CSS_SELECTOR, "input[value='Delete Project']").click()
        self.open_manage_project_page()
        self.project_cache = None

    def select_project_by_id(self, id):
        wd = self.app.driver
        wd.get(self.app.base_url + "manage_proj_edit_page.php?project_id=" + str(id))
