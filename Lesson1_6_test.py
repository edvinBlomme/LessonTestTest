import math
import pytest

# ============================ EXERCISE 1 ============================


# A function that is supposed to return the
# volume of a sphere given a radius
def volume_of_sphere(radius):
    if radius > 0:
        return (4/3) * math.pi * (radius ** 3)
    else:
        return "radius must be positive"


def test_correct_input():
    assert volume_of_sphere(1) == 4.1887902047863905
    assert volume_of_sphere(10) > 10


def test_incorrect_input():
    assert volume_of_sphere(0) == "radius must be positive"
    assert volume_of_sphere(-3) == "radius must be positive"


def test_types():
    with pytest.raises(TypeError):
        volume_of_sphere("hello")


# ============================ EXERCISE 2 ============================
test_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


# Function supposed to insert a given element into a given matrix at a given position in the matrix
def insert_element_into_matrix(matrix, element, row, column):
    matrix[row][column] = element


# Tests here below the function

# ============================ EXERCISE 3 ============================


# A sorting algorithm that is supposed to sort lists of integers
def bubble_sort(arr):
    # Check the input
    if len(arr) == 0:
        raise Exception("Can not sort an empty list")
    elif type(arr[0]) != int:
        raise Exception("This algorithm can only sort integers")

    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Tests here below the function



a_list = ['T', 'o', 'm', 'B', 'o', 'm', 'b', 'a', 'd', 'i', 'l']
