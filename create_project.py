import os

def create_file(file_path, content=""):
    """Creates a file with optional content."""
    with open(file_path, "w") as file:
        file.write(content)

def create_project_structure():
    """Creates the specified project structure."""
    structure = {
        "app.py": "",
        "config.py": "",
        "models.py": "",
        "utils.py": "",
        "routes/__init__.py": "",
        "routes/auth.py": "",
        "templates/login.html": "",
        "templates/color_auth.html": "",
        "templates/otp_verification.html": "",
        "templates/success.html": "",
        "static/styles.css": "",
        "migrations/": None,
        "tests/test_auth.py": "",
    }

    for path, content in structure.items():
        if path.endswith("/"):
            os.makedirs(path, exist_ok=True)  # Create directories
        else:
            dir_path = os.path.dirname(path)
            if dir_path:  # Check if a parent directory exists
                os.makedirs(dir_path, exist_ok=True)
            create_file(path, content)

if __name__ == "__main__":
    create_project_structure()
    print("Project structure created successfully!")
