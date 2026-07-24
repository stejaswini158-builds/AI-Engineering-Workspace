from pathlib import Path
import shutil


GENERATED_WEBSITES_DIR = Path("generated_websites")


def save_website(
    project_name: str,
    framework: str,
    app: str,
    css: str
):
    """
    Save generated website files.
    """

    project_folder = GENERATED_WEBSITES_DIR / project_name

    project_folder.mkdir(
        parents=True,
        exist_ok=True
    )

    framework = framework.lower()

    if framework == "react":

        app_file = project_folder / "App.jsx"
        css_file = project_folder / "App.css"

    else:

        app_file = project_folder / "index.html"
        css_file = project_folder / "style.css"

    with open(
        app_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(app)

    with open(
        css_file,
        "w",
        encoding="utf-8"
    ) as file:

        file.write(css)

    return project_folder


def create_website_zip(
    project_name: str
):
    """
    Create a ZIP file for the generated website.
    """

    project_folder = GENERATED_WEBSITES_DIR / project_name

    if not project_folder.exists():
        raise FileNotFoundError(
            f"{project_name} does not exist."
        )

    zip_path = GENERATED_WEBSITES_DIR / project_name

    shutil.make_archive(
        str(zip_path),
        "zip",
        project_folder
    )

    return f"{zip_path}.zip"