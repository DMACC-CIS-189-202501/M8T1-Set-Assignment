import pytest
import ast
import importlib

# Test to check for file docstring
def test_file_docstring():
    with open('assignment.py', 'r') as file:
        tree = ast.parse(file.read())
    docstring = ast.get_docstring(tree)
    assert docstring is not None, "DMACC Student, there does not appear to be a docstring at the top of your file. Please add a docstring explaining what your code does."

# Test to check the presence of the in_set function
def test_in_set_function():
    from assignment import in_set
    assert callable(in_set), "DMACC Student, the function 'in_set' does not appear to be defined. Please define the function."

# Test to check the docstring of the in_set function
def test_in_set_docstring():
    from assignment import in_set
    docstring = in_set.__doc__
    assert docstring is not None, "DMACC Student, the function 'in_set' does not have a docstring. Please add a reST style docstring explaining the parameters and return type."

# Tests for the in_set function
def test_in_set_case_1():
    from assignment import in_set
    result = in_set({'apple', 'banana', 'cherry'}, 'apple')
    expected = True
    assert result == expected, f"DMACC Student, the function 'in_set' did not return the expected value for inputs ({'apple', 'banana', 'cherry'}, 'apple').\nExpected: {expected}\nActual: {result}\nPlease check your logic."

def test_in_set_case_2():
    from assignment import in_set
    result = in_set({'apple', 'banana', 'cherry'}, 'Apple')
    expected = False
    assert result == expected, f"DMACC Student, the function 'in_set' did not return the expected value for inputs ({'apple', 'banana', 'cherry'}, 'Apple').\nExpected: {expected}\nActual: {result}\nPlease check your logic."

def test_in_set_case_3():
    from assignment import in_set
    result = in_set({'apple', 'banana', 'cherry'}, 'date')
    expected = False
    assert result == expected, f"DMACC Student, the function 'in_set' did not return the expected value for inputs ({'apple', 'banana', 'cherry'}, 'date').\nExpected: {expected}\nActual: {result}\nPlease check your logic."

def test_in_set_case_4():
    from assignment import in_set
    result = in_set({1, 3, 5, 7, 9}, 9)
    expected = True
    assert result == expected, f"DMACC Student, the function 'in_set' did not return the expected value for inputs ({1, 3, 5, 7, 9}, 9).\nExpected: {expected}\nActual: {result}\nPlease check your logic."

def test_in_set_case_5():
    from assignment import in_set
    result = in_set({1, 3, 5, 7, 9}, 2)
    expected = False
    assert result == expected, f"DMACC Student, the function 'in_set' did not return the expected value for inputs ({1, 3, 5, 7, 9}, 2).\nExpected: {expected}\nActual: {result}\nPlease check your logic."

if __name__ == "__main__":
    pytest.main()