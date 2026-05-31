from functions.write_file import write_file


def run_tests():
    print("--- Running write_file Tests ---")

    # Test Case 1: Overwriting/writing an existing file in the main directory
    print('write_file("calculator", "lorem.txt", "wait, this isn\'t lorem ipsum"):')
    res1 = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(f"  {res1}\n")

    # Test Case 2: Writing a file inside a subdirectory (verifies os.makedirs works)
    print(
        'write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"):'
    )
    res2 = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(f"  {res2}\n")

    # Test Case 3: Breakout attempt to an absolute path outside the working directory
    print('write_file("calculator", "/tmp/temp.txt", "this should not be allowed"):')
    res3 = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(f"  {res3}\n")


if __name__ == "__main__":
    run_tests()
