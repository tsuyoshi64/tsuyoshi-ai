from functions.run_python_file import run_python_file


def run_tests():
    print("--- Running run_python__file test ---")
    # 1
    print('-- [run_python_file("calculator", "main.py")] --')
    print(f"Result case 1: {run_python_file('calculator', 'main.py')}\n")
    # 2
    print('-- [run_python_file("calculator", "main.py", ["3 + 5"])] --')
    print(f"Result case 2: {run_python_file('calculator', 'main.py', ['3 + 5'])}\n")
    # 3
    print('-- [run_python_file("calculator", "tests.py")] --')
    print(f"Result case 3: {run_python_file('calculator', 'tests.py')}\n")
    # 4
    print('-- [run_python_file("calculator", "../main.py")] --')
    print(f"Result case 4: {run_python_file('calculator', '../main.py')}\n")
    # 5
    print('-- [run_python_file("calculator", "nonexistent.py")] --')
    print(f"Result case 5: {run_python_file('calculator', 'nonexistent.py')}\n")
    # 6
    print('-- [run_python_file("calculator", "lorem.txt")] --')
    print(f"Result case 6: {run_python_file('calculator', 'lorem.txt')}\n")


if __name__ == "__main__":
    run_tests()
