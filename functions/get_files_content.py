from config import MAX_CHARS
import os
from google.genai import types


schema_get_files_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Retrieves the full text or binary content of a specific file located within the permitted working directory",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path of the file to read, including its file name and extension",
            ),
        },
        required=["file_path"],
    ),
)


def get_file_content(working_directory: str, file_path: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_norm = os.path.normpath(
            os.path.join(working_directory_abs, file_path)
        )
        if (
            os.path.commonpath([working_directory_abs, file_path_norm])
            != working_directory_abs
        ):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(file_path_norm):
            return f'Error: File not found or is not a regular file: "{file_path}"'

        with open(file_path_norm, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return file_content_string
    except Exception as e:
        return f"Error: {str(e)}"
