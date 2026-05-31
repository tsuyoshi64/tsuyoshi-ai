import os
from functions.get_files_info import get_files_info


def run_tests():
    # Test Case 1: Current directory
    print("Result for current directory:")
    res1 = get_files_info("calculator", ".")
    # Indent the multi-line result for presentation matching
    print("\n".join(f"  {line}" for line in res1.splitlines()))
    print()

    # Test Case 2: Subdirectory 'pkg'
    print("Result for 'pkg' directory:")
    res2 = get_files_info("calculator", "pkg")
    print("\n".join(f"  {line}" for line in res2.splitlines()))
    print()

    # Test Case 3: Absolute path breakout attempt
    print("Result for '/bin' directory:")
    res3 = get_files_info("calculator", "/bin")
    print(f"    {res3}")
    print()

    # Test Case 4: Relative path breakout attempt
    print("Result for '../' directory:")
    res4 = get_files_info("calculator", "../")
    print(f"    {res4}")


if __name__ == "__main__":
    run_tests()

