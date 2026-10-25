import numpy as np

class NeutralManifold:
    """
    A neutral n-dimensional manifold with identity metric.
    This acts as the ambient space in which the Fun-Sphere
    submanifold is constructed.

    The manifold is intentionally structure-free:
    - no curvature
    - no semantics
    - no constraints
    - no operator bias

    It is a clean geometric substrate for holonomy experiments.
    """

    def __init__(self, dim=50):
        self.dim = dim
        self.metric = np.eye(dim)

    def zero(self):
        """Return the origin point of the manifold."""
        return np.zeros(self.dim)

    def random_point(self):
        """Generate a random point in the manifold."""
        return np.random.randn(self.dim)

    def project(self, vec):
        """
        Project a vector into the manifold's coordinate system.
        (Identity projection for a neutral manifold.)
        """
        return np.array(vec, dtype=float)
