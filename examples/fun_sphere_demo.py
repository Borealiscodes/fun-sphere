import numpy as np

from src.fun_sphere.manifold import NeutralManifold
from src.fun_sphere.operators import Operator
from src.fun_sphere.holonomy import triggers_fun_sphere
from src.fun_sphere.submanifold import build_fun_sphere
from src.fun_sphere.ecology import NarrativeEcology


def main():
    # Create the ambient manifold
    M = NeutralManifold(dim=50)

    # Starting point
    x0 = M.random_point()

    # Define a reversible operator loop
    # Slight rotation in a 2D subspace of the 50D manifold
    theta = 0.25  # small angle
    R = np.eye(50)
    R[0, 0] = np.cos(theta)
    R[0, 1] = -np.sin(theta)
    R[1, 0] = np.sin(theta)
    R[1, 1] = np.cos(theta)

    # Build operator (inverse auto-computed)
    op = Operator(R)

    # Loop = apply operator 4 times (full rotation)
    loop = [op, op, op, op]

    print("Checking holonomy trigger...")
    if triggers_fun_sphere(x0, loop):
        print("Holonomy detected — Fun-Sphere triggered.")
    else:
        print("No holonomy detected.")

    print("\nConstructing Fun-Sphere...")
    sphere = build_fun_sphere(x0, loop, max_depth=25)

    print(f"Fun-Sphere size: {len(sphere)} points")
    for p in list(sphere)[:5]:
        print("  ", p)

    print("\nRunning reversible narrative ecology...")
    ecology = NarrativeEcology(M)
    forward, backward = ecology.run_reversible(x0, loop)

    print("Forward evolution:")
    print(forward)

    print("\nBackward evolution (should match original):")
    print(backward)


if __name__ == "__main__":
    main()
