from prompt import system_prompt
import os
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.call_functions import available_functions, call_function


def generate_content(client: genai.Client, messages: list[types.Content]):
    return client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt
        ),
    )


def main():
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("GEMINI_API_KEY was not found")

    parser = argparse.ArgumentParser(description="Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    args = parser.parse_args()

    client = genai.Client(api_key=api_key)

    messages: list[types.Content] = [
        types.Content(
            role="user",
            parts=[types.Part(text=args.user_prompt)],
        )
    ]

    response = generate_content(client, messages)

    if response.usage_metadata is None:
        raise RuntimeError("Failed requesting API")

    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls is not None:
        function_call_parts = []
        for funcs in response.function_calls:
            function_call_result = call_function(funcs, verbose=args.verbose)

            if not function_call_result.parts:
                raise ValueError("Function call returned an empty parts list.")

            if function_call_result.parts[0].function_response is None:
                raise ValueError(
                    "The first part mssing a valid function_response object mapping."
                )

            if function_call_result.parts[0].function_response.response is None:
                raise ValueError(
                    "The function response field property container evaluates to None."
                )

            function_call_parts.append(function_call_result.parts[0])

            if args.verbose:
                print(f"-> {function_call_result.parts[0].function_response.response}")

    else:
        print(response.text)


if __name__ == "__main__":
    main()
