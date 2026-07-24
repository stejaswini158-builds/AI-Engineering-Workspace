from services.llm import ask_llm
from tools.website_builder.utils import (
    save_website,
    create_website_zip,
)


def generate_website(
    prompt: str,
    framework: str,
    template: str
):
    """
    Generate a website using the selected framework.
    """

    full_prompt = f"""
You are an expert {framework} web developer.

Generate a professional website.

IMPORTANT RULES:

1. Return ONLY TWO SECTIONS.

===APP===
(Main website code)

===CSS===
(Stylesheet)

2. No explanations.
3. No markdown.
4. No triple backticks.
5. Generate responsive code.
6. Follow the selected template.

Framework:
{framework}

Template:
{template}

Website Requirements:
{prompt}
"""

    response = ask_llm(full_prompt)

    response = response.replace("```html", "")
    response = response.replace("```jsx", "")
    response = response.replace("```css", "")
    response = response.replace("```", "")

    if "===APP===" not in response or "===CSS===" not in response:

        return {
            "app": response.strip(),
            "css": ""
        }

    parts = response.split(
        "===CSS===",
        1
    )

    app_code = (
        parts[0]
        .replace("===APP===", "")
        .strip()
    )

    css_code = parts[1].strip()

    return {
        "app": app_code,
        "css": css_code
    }


def save_generated_website(
    project_name: str,
    framework: str,
    app: str,
    css: str
):
    """
    Save generated website.
    """

    folder = save_website(
        project_name,
        framework,
        app,
        css
    )

    return {
        "message": "Website saved successfully.",
        "folder": str(folder)
    }


def download_generated_website(
    project_name: str
):
    """
    Create ZIP file for generated website.
    """

    zip_file = create_website_zip(
        project_name
    )

    return zip_file