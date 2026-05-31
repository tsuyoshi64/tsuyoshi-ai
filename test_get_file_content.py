import os
from config import MAX_CHARS
from functions.get_files_content import get_file_content

# Note: Adjust the import statement above if your functions directory
# uses a different folder name (e.g., solutions).


def run_tests():
    print("--- Running get_file_content Tests ---")
    print(f"Configured MAX_CHARS: {MAX_CHARS}\n")

    # Test Case 1: lorem.txt (Truncation and length check)
    print('get_file_content("calculator", "lorem.txt"):')
    res_lorem = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(res_lorem)}")
    print(f"lorem.txt truncated: {'truncated' in res_lorem}")
    print()

    # Test Case 2: main.py
    print('get_file_content("calculator", "main.py"):')
    res_main = get_file_content("calculator", "main.py")
    print("Result contents:")
    print("\n".join(f"  {line}" for line in res_main.splitlines()))
    print()

    # Test Case 3: pkg/calculator.py
    print('get_file_content("calculator", "pkg/calculator.py"):')
    res_calc = get_file_content("calculator", "pkg/calculator.py")
    print("Result contents:")
    print("\n".join(f"  {line}" for line in res_calc.splitlines()))
    print()

    # Test Case 4: /bin/cat (Breakout attempt error)
    print('get_file_content("calculator", "/bin/cat"):')
    res_cat = get_file_content("calculator", "/bin/cat")
    print(f"  {res_cat}")
    print()

    # Test Case 5: pkg/does_not_exist.py (Missing file error)
    print('get_file_content("calculator", "pkg/does_not_exist.py"):')
    res_missing = get_file_content("calculator", "pkg/does_not_exist.py")
    print(f"  {res_missing}")


if __name__ == "__main__":
    run_tests()
