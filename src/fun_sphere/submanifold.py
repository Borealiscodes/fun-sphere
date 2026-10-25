from .holonomy import triggers_fun_sphere, apply_loop

def build_fun_sphere(start_vec, operators, max_depth=100):
    """
    Construct the Fun-Sphere as a holonomy-closed region of the manifold.

    The Fun-Sphere is defined as the set of points reachable through
    holonomy-induced transformations. A point belongs to the Fun-Sphere
    if applying the operator loop returns it to itself while producing
    a non-identity frame transform.

    Parameters
    ----------
    start_vec : np.ndarray
        The initial point in the manifold.
    operators : list of Operator
        A reversible operator loop.
    max_depth : int
        Maximum number of expansion steps to avoid infinite traversal.

    Returns
    -------
    set of tuple
        A set of points (as tuples) forming the Fun-Sphere.
    """
    sphere = {tuple(start_vec)}
    frontier = [start_vec]

    depth = 0
    while frontier and depth < max_depth:
        vec = frontier.pop()
        depth += 1

        if triggers_fun_sphere(vec, operators):
            transformed = apply_loop(vec, operators)
            t = tuple(transformed)

            if t not in sphere:
                sphere.add(t)
                frontier.append(transformed)

    return sphere
