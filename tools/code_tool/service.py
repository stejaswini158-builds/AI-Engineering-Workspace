from services.llm import ask_llm
from tools.code_tool.utils import save_code, run_python_file


def generate_code(
    prompt: str,
    language: str,
    template: str
):
    """
    Generate code based on language and template.
    """

    full_prompt = f"""
You are an expert {language} software developer.

IMPORTANT RULES:

1. Generate ONLY {language} code.
2. Do NOT generate explanations.
3. Do NOT generate markdown.
4. Do NOT use triple backticks.
5. Return executable code only.

Programming Language:
{language}

Template:
{template}

Task:
{prompt}

Generate a professional {template}.
"""

    code = ask_llm(full_prompt)

    code = code.replace(f"```{language}", "")
    code = code.replace("```", "")
    code = code.strip()

    return code


def save_generated_code(
    filename: str,
    code: str
):
    """
    Save generated code to a file.
    """

    save_code(
        filename,
        code
    )

    return {
        "message": "Code saved successfully.",
        "filename": filename
    }


def run_generated_code(
    filename: str
):
    """
    Currently supports Python execution only.
    """

    if not filename.endswith(".py"):

        return {
            "output": "Running is currently supported only for Python files."
        }

    output = run_python_file(filename)

    return {
        "output": output
    }


def explain_code(
    code: str,
    language: str
):
    """
    Explain code using the LLM.
    """

    full_prompt = f"""
You are an expert {language} programming teacher.

Explain the following {language} code clearly.

Include:

1. What the code does
2. How the code works
3. Important functions, classes, or logic
4. Input and output behavior
5. Time and space complexity, if applicable

Do not modify the code.
Do not generate new code.
Return only the explanation in plain text.

Programming Language:
{language}

Code:
{code}
"""

    explanation = ask_llm(full_prompt)

    return explanation.strip()