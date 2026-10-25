class NarrativeEcology:
    """
    Reversible narrative ecology engine for the Fun-Sphere.

    This module defines how narrative states evolve under reversible
    operators. It provides forward flow, backward flow, and reversible
    loop execution. The ecology is intentionally linear and algebraic,
    making it ideal for toy-model experimentation with reversible
    story physics and holonomy-driven narrative curvature.
    """

    def __init__(self, manifold):
        self.manifold = manifold

    def evolve(self, vec, operator):
        """
        Apply the forward operator to evolve the narrative state.

        Parameters
        ----------
        vec : np.ndarray
            Current narrative state.
        operator : Operator
            Reversible operator.

        Returns
        -------
        np.ndarray
        """
        return operator.apply(vec)

    def reverse(self, vec, operator):
        """
        Apply the inverse operator to reverse the narrative state.

        Parameters
        ----------
        vec : np.ndarray
            Current narrative state.
        operator : Operator
            Reversible operator.

        Returns
        -------
        np.ndarray
        """
        return operator.reverse(vec)

    def run_sequence(self, vec, operators):
        """
        Apply a sequence of forward operators.

        Parameters
        ----------
        vec : np.ndarray
        operators : list of Operator

        Returns
        -------
        np.ndarray
        """
        for op in operators:
            vec = op.apply(vec)
        return vec

    def run_reversible(self, vec, operators):
        """
        Apply a sequence of forward operators, then reverse them.

        Parameters
        ----------
        vec : np.ndarray
        operators : list of Operator

        Returns
        -------
        (np.ndarray, np.ndarray)
            forward_state, reversed_state
        """
        forward = self.run_sequence(vec, operators)
        backward = self.run_sequence(forward, [op.inverse for op in operators])
        return forward, backward
