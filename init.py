import os

def create_structure(base_dir, structure):
    for key, value in structure.items():
        path = os.path.join(base_dir, key)
        os.makedirs(path, exist_ok=True)
        if isinstance(value, dict):
            create_structure(path, value)
        else:
            for file_name in value:
                with open(os.path.join(path, file_name), 'w') as f:
                    pass  # Create empty file

def main():
    base_dir = "ai-environmental-monitoring-platform"
    structure = {
        "backend": {
            "app": {
                "__init__.py": [],
                "models": {"__init__.py": []},
                "serializers": {"__init__.py": []},
                "views": {"__init__.py": []},
                "urls": {"__init__.py": []},
                "utils": {"__init__.py": []},
            },
            "api": {
                "__init__.py": [],
                "serializers.py": [],
                "views.py": [],
                "urls.py": [],
            },
            "tests": {"test_models.py": []},
            "requirements.txt": [],
            "manage.py": [],
        },
        "frontend": {
            "public": {},
            "src": {
                "components": {},
                "pages": {},
                "services": {},
                "App.js": [],
            },
            "package.json": [],
            "README.md": [],
        },
        "data": {
            "raw": {},
            "processed": {},
            "models": {},
        },
        "docs": {
            "user_guides": {},
            "developer_docs": {},
            "API_documentation": {},
        },
        ".gitignore": [],
        "README.md": [],
        "LICENSE": [],
    }

    create_structure(base_dir, structure)
    print(f"Directory structure for '{base_dir}' has been created.")

if __name__ == "__main__":
    main()
