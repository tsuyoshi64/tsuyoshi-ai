import subprocess
from google.genai import types
import os


schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a local Python (.py) script within the working directory environment and captures its output or errors",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The relative path to the Python file (.py) that needs to be executed",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional list of command-line argument strings to pass into the script execution.",
            ),
        },
        required=["file_path"],
    ),
)


def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
    try:
        working_directory_abs = os.path.abspath(working_directory)
        file_path_norm = os.path.normpath(
            os.path.join(working_directory_abs, file_path)
        )

        if (
            os.path.commonpath([working_directory_abs, file_path_norm])
            != working_directory_abs
        ):
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not file_path_norm.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'
        if not os.path.isfile(file_path_norm):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        command = ["python", file_path_norm]
        if args:
            command.extend(args)

        result = subprocess.run(
            command,
            cwd=working_directory_abs,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            timeout=30,
        )

        output_parts = []
        if result.returncode != 0:
            output_parts.append(f"Process exited with code {result.returncode}")
        if not result.stdout.strip() and not result.stderr.strip():
            output_parts.append("No output produced.")
        else:
            if result.stdout:
                output_parts.append(f"STDOUT: {result.stdout}")
            if result.stderr:
                output_parts.append(f"STDERR: {result.stderr}")

        return "\n".join(output_parts)
    except Exception as e:
        return f"Error: executing Python file: {e}"
