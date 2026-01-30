def generate_pom(project_name):
    if not project_name:
        raise ValueError("Project name is required")
    return f"<project>{project_name}</project>"