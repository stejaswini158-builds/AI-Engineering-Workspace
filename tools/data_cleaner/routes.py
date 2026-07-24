from fastapi import APIRouter, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
import os

from tools.data_cleaner.schemas import DataCleanerResponse
from tools.data_cleaner.service import clean_data

router = APIRouter(
    prefix="/data-cleaner",
    tags=["Data Cleaner"]
)


@router.post(
    "/clean",
    response_model=DataCleanerResponse
)
def clean_uploaded_file(
    file: UploadFile = File(...)
):

    if file.filename == "":
        raise HTTPException(
            status_code=400,
            detail="No file selected."
        )

    try:
        result = clean_data(file)
        return DataCleanerResponse(**result)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception:
        raise HTTPException(
            status_code=500,
            detail="Internal server error while processing the file."
        )


@router.get("/download/{filename}")
def download_cleaned_file(filename: str):

    filepath = os.path.join(
        "cleaned_files",
        filename
    )

    if not os.path.exists(filepath):
        raise HTTPException(
            status_code=404,
            detail="Cleaned file not found."
        )

    return FileResponse(
        path=filepath,
        filename=filename
    )