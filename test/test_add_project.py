from model.project import Project


def test_add_project(app):
    old_projects = app.project.get_project_list()
    random_name = app.project.random_string("name_", 10)
    name = Project(name=random_name)
    app.project.add_new_project(name)
    new_projects = app.project.get_project_list()
    assert len(old_projects) + 1 == len(new_projects)
    old_projects.append(name)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
