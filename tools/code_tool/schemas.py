from pydantic import BaseModel, Field


class GenerateCodeRequest(BaseModel):

    prompt: str = Field(
        ...,
        min_length=1,
        description="Task description for code generation"
    )

    language: str = Field(
        ...,
        min_length=1,
        description="Programming language"
    )

    template: str = Field(
        ...,
        min_length=1,
        description="Code template"
    )


class GenerateCodeResponse(BaseModel):

    code: str


class SaveCodeRequest(BaseModel):

    filename: str = Field(
        ...,
        min_length=1
    )

    code: str = Field(
        ...,
        min_length=1
    )


class SaveCodeResponse(BaseModel):

    message: str
    filename: str


class RunCodeRequest(BaseModel):

    filename: str = Field(
        ...,
        min_length=1
    )


class RunCodeResponse(BaseModel):

    output: str


class ExplainCodeRequest(BaseModel):

    code: str = Field(
        ...,
        min_length=1
    )

    language: str = Field(
        ...,
        min_length=1
    )


class ExplainCodeResponse(BaseModel):

    explanation: str