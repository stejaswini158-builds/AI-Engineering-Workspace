from pydantic import BaseModel, Field


class GenerateWebsiteRequest(BaseModel):
    prompt: str = Field(..., min_length=1)
    framework: str = Field(..., min_length=1)
    template: str = Field(..., min_length=1)


class GenerateWebsiteResponse(BaseModel):
    app: str
    css: str


class SaveWebsiteRequest(BaseModel):
    project_name: str = Field(..., min_length=1)
    framework: str = Field(..., min_length=1)
    app: str = Field(..., min_length=1)
    css: str = Field(..., min_length=1)


class SaveWebsiteResponse(BaseModel):
    message: str
    folder: str