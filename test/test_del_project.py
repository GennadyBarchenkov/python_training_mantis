from model.project import Project
import random


def test_del_project(app):
    if len(app.project.get_project_list()) == 0:
        app.project.add_new_project(Project(name="test"))
    old_projects = app.project.get_project_list()
    select_project = random.choice(old_projects)
    app.project.delete_project_by_id(select_project.id)
    new_projects = app.project.get_project_list()
    assert len(old_projects) - 1 == len(new_projects)
    old_projects.remove(select_project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
