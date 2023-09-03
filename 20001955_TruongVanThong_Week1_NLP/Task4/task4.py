import numpy as np

# Multiplication of two given matrixes (Tích hai ma trận cho trước)
def matrix_multiplication(A, B):
    """Multiply two given matrixes."""
    return np.matmul(A, B)

# Outer product of two given vectors (Tích vô hướng hai vector cho trước)
def outer_product(a, b):
    """Compute the outer product of two given vectors."""
    return np.outer(a, b)

# Cross product of two given vectors (Tích có hướng hai vector cho trước)
def cross_product(a, b):  
    """Compute the cross product of two given vectors.""" 
    return np.cross(a, b)

# Determinant of a given square array (Định thức của một ma trận vuông cho trước)
def determinant(A):
    """Compute the determinant of a given square array."""
    return np.linalg.det(A)

# Determinant of an array (Định thức của một mảng cho trước)
def determinant_array(A):
    """Compute the determinant of an array."""
    if A.ndim == 2:
        return np.linalg.det(A)
    else:
        raise NotImplementedError("Determinant of array of dimension > 2 is not implemented yet.")

# Inner product of vectors for 1-D arrays (without complex conjugation) and in higher dimension (Tích trong hai vector cho trước)
def inner_product(a, b):
    """Compute the inner product of two vectors."""
    if a.ndim == 1 and b.ndim == 1:
        return np.dot(a, b)
    else:
        raise NotImplementedError("Inner product of vectors of dimension > 1 is not implemented yet.")

if __name__ == "__main__":
    A = np.array([[1, 2], [3, 4]]) 
    B = np.array([[5, 6], [7, 8]]) 
    print("Multiplication of two given matrixes:") 
    print(matrix_multiplication(A, B))

    v1 = np.array([1, 2, 3])
    v2 = np.array([4, 5, 6])
    print("Outer product of two given vectors:")
    print(outer_product(v1, v2))

    print("Cross product of two given vectors:")
    print(cross_product(v1, v2))

    print("Determinant of a given square array:")
    print(round(determinant(A), 4))

    print("Determinant of an array:")
    print(round(determinant_array(np.array([[1, 2], [3, 4]])), 4))

    print("Inner product of vectors for 1-D arrays (without complex conjugation):")
    print(inner_product(v1, v2))
