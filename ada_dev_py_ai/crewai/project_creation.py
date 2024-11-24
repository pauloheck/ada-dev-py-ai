def create_project(project_name: str, description: str):
    """
    Create a new project with the given name and description.

    :param project_name: The name of the project.
    :param description: A brief description of the project.
    :return: A dictionary containing the project details.
    """
    project = {
        "name": project_name,
        "description": description,
        "status": "created"
    }
    return project
