import numpy as np

class Connection:
    """
    Parallel transport and frame-transform composition for the Fun-Sphere
    holonomy engine.

    This class defines how vectors move through the manifold under
    operator-induced transformations. It is intentionally minimal:

    - No curvature terms
    - No Christoffel symbols
    - No coordinate dependencies

    The connection is purely algebraic, making it ideal for toy-model
    holonomy experiments and reversible narrative ecology.
    """

    def __init__(self, manifold):
        self.manifold = manifold

    def parallel_transport(self, vec, transform):
        """
        Apply a frame-transform matrix to a vector.

        Parameters
        ----------
        vec : np.ndarray
            A point or tangent vector in the manifold.
        transform : np.ndarray
            A dim x dim matrix representing a frame transform.

        Returns
        -------
        np.ndarray
            The transported vector.
        """
        return transform @ vec

    def compose_transforms(self, transforms):
        """
        Compose a sequence of frame transforms into a single operator.

        Parameters
        ----------
        transforms : list of np.ndarray
            A list of dim x dim matrices.

        Returns
        -------
        np.ndarray
            The composed transform matrix.
        """
        T = np.eye(self.manifold.dim)
        for M in transforms:
            T = M @ T
        return T
