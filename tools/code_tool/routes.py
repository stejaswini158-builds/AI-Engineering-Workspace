from fastapi import (
    APIRouter,
    HTTPException
)

from fastapi.responses import FileResponse

import os

from tools.code_tool.schemas import (
    GenerateCodeRequest,
    GenerateCodeResponse,
    SaveCodeRequest,
    SaveCodeResponse,
    RunCodeRequest,
    RunCodeResponse,
    ExplainCodeRequest,
    ExplainCodeResponse,
)

from tools.code_tool.service import (
    generate_code,
    save_generated_code,
    run_generated_code,
    explain_code,
)


router = APIRouter(
    prefix="/code",
    tags=["Code Tool"],
)


@router.post(
    "/generate",
    response_model=GenerateCodeResponse
)
def generate(
    request: GenerateCodeRequest
):

    try:

        code = generate_code(
            request.prompt,
            request.language,
            request.template
        )

        return GenerateCodeResponse(
            code=code
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Code generation failed: {str(e)}"
        )


@router.post(
    "/save",
    response_model=SaveCodeResponse
)
def save(
    request: SaveCodeRequest
):

    try:

        result = save_generated_code(
            request.filename,
            request.code
        )

        return SaveCodeResponse(
            message=result["message"],
            filename=result["filename"]
        )

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


@router.post(
    "/run",
    response_model=RunCodeResponse
)
def run(
    request: RunCodeRequest
):

    try:

        result = run_generated_code(
            request.filename
        )

        return RunCodeResponse(
            output=result["output"]
        )

    except FileNotFoundError as e:

        raise HTTPException(
            status_code=404,
            detail=str(e)
        )

    except TimeoutError:

        raise HTTPException(
            status_code=408,
            detail="Code execution timed out."
        )


@router.get(
    "/download/{filename}"
)
def download_generated_code(
    filename: str
):

    filepath = os.path.join(
        "generated",
        filename
    )

    if not os.path.exists(filepath):

        raise HTTPException(
            status_code=404,
            detail="Generated code file not found."
        )

    return FileResponse(
        path=filepath,
        filename=filename,
        media_type="text/plain"
    )


@router.post(
    "/explain",
    response_model=ExplainCodeResponse
)
def explain(
    request: ExplainCodeRequest
):

    try:

        explanation = explain_code(
            request.code,
            request.language
        )

        return ExplainCodeResponse(
            explanation=explanation
        )

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Code explanation failed: {str(e)}"
        )