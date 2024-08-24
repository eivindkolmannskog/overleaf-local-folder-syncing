from ...overleaf_syncing.api_requests import sanitize_path    

def test_sanitize_path():
    # Test case 1: Path with backslashes
    path = "C:\\Users\\Documents\\file.txt"
    expected_output = "/C:/Users/Documents/file.txt"
    assert sanitize_path(path) == expected_output

    # Test case 2: Path with redundant './'
    path = "./folder/./file.txt"
    expected_output = "/folder/file.txt"
    assert sanitize_path(path) == expected_output

    # Test case 3: Path without leading slash
    path = "folder/file.txt"
    expected_output = "/folder/file.txt"
    assert sanitize_path(path) == expected_output

    # Test case 4: Path with trailing slashes
    path = "/folder/subfolder/"
    expected_output = "/folder/subfolder"
    assert sanitize_path(path) == expected_output

    # Test case 5: Path with multiple slashes
    path = "/folder//subfolder///file.txt"
    expected_output = "/folder/subfolder/file.txt"
    assert sanitize_path(path) == expected_output

    # Test case 6: Path with special characters
    path = "/folder@#$%^&*()_+-=[]{}|;':,.<>/?~`"
    expected_output = "/folder@#$%^&*()_+-=[]{}|;':,.<>/?~`"
    assert sanitize_path(path) == expected_output

    print("All test cases passed!")

test_sanitize_path()