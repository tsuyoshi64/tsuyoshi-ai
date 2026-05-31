import os


def write_file(working_directory: str, file_path: str, content: str) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_norm = os.path.normpath(
            os.path.join(working_directory_abs, file_path)
        )

        if (
            os.path.commonpath([working_directory_abs, file_path_norm])
            != working_directory_abs
        ):
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(file_path_norm):
            return f'Error: Cannot write to "{file_path}" as it is a directory'

        parent_directory = os.path.dirname(file_path_norm)
        os.makedirs(parent_directory, exist_ok=True)

        with open(file_path_norm, "w") as f:
            f.write(content)

        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )

    except Exception as e:
        return f"Error: {str(e)}"
