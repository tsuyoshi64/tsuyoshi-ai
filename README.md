# Tsuyoshi AI Agent

An AI coding agent built in Python that can read, write, and execute files to autonomously fix bugs in a codebase.

> [!WARNING]
> This project is just for my study, so it may not be suitable for production use!

## Requirements

- Python 3.x
- [uv](https://docs.astral.sh/uv/)
- An OpenAI API key

## Setup

1. Clone the repo
2. Install dependencies:
   ```bash
   uv sync
   ```
3. Create a .env file:
  ```
  OPENAI_API_KEY = "your_key"
  ```
## Usage
Run the agent:
  ```
  uv run main.py "your prompt here"
  ```
Example:
  ```
  uv run main.py "Fix the bug: 3 + 7 * 2 shouldn't be 20"
  ```

## Running Tests
  ```
  uv run pytest
  ```

*My name is Tsuyoshi*
