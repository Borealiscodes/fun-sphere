import numpy as np

class Operator:
    """
    Reversible operator algebra for the Fun-Sphere engine.

    Each operator is represented as a pair of matrices:
    - forward:  T
    - inverse:  T^{-1}

    These matrices act on points or tangent vectors in the manifold.
    Operators are intentionally linear to keep the toy model clean,
    predictable, and holonomy-friendly.
    """

    def __init__(self, forward_matrix, inverse_matrix=None):
        """
        Initialize a reversible operator.

        Parameters
        ----------
        forward_matrix : np.ndarray
            A dim x dim matrix representing the forward transform.
        inverse_matrix : np.ndarray, optional
            A dim x dim matrix representing the inverse transform.
            If omitted, the inverse is computed automatically.
        """
        self.forward = forward_matrix
        self.inverse = (
            inverse_matrix if inverse_matrix is not None
            else np.linalg.inv(forward_matrix)
        )

    def apply(self, vec):
        """
        Apply the forward operator to a vector.

        Parameters
        ----------
        vec : np.ndarray

        Returns
        -------
        np.ndarray
        """
        return self.forward @ vec

    def reverse(self, vec):
        """
        Apply the inverse operator to a vector.

        Parameters
        ----------
        vec : np.ndarray

        Returns
        -------
        np.ndarray
        """
        return self.inverse @ vec
