import numpy as np

def apply_loop(vec, operators):
    """
    Apply a sequence of reversible operators to a vector.

    Parameters
    ----------
    vec : np.ndarray
        A point or tangent vector in the manifold.
    operators : list of Operator
        A list of reversible operators.

    Returns
    -------
    np.ndarray
        The transformed vector after applying the loop.
    """
    for op in operators:
        vec = op.apply(vec)
    return vec


def loop_transform(operators):
    """
    Compute the combined forward transform matrix for a loop.

    Parameters
    ----------
    operators : list of Operator

    Returns
    -------
    np.ndarray
        The composed transform matrix T = T_n ... T_1
    """
    dim = operators[0].forward.shape[0]
    T = np.eye(dim)
    for op in operators:
        T = op.forward @ T
    return T


def triggers_fun_sphere(vec, operators, tol=1e-6):
    """
    Determine whether a loop triggers Fun-Sphere formation.

    A loop triggers the Fun-Sphere when:
    1. The loop returns to the same point:
       apply_loop(vec, operators) == vec
    2. The frame is transformed:
       loop_transform(operators) != identity

    Parameters
    ----------
    vec : np.ndarray
        Starting point in the manifold.
    operators : list of Operator
        Reversible operators forming a loop.
    tol : float
        Numerical tolerance for equality checks.

    Returns
    -------
    bool
        True if the loop triggers Fun-Sphere formation.
    """
    final = apply_loop(vec, operators)
    T = loop_transform(operators)

    same_point = np.allclose(final, vec, atol=tol)
    non_identity = not np.allclose(T, np.eye(T.shape[0]), atol=tol)

    return same_point and non_identity
