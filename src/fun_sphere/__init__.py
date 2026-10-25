"""
Fun-Sphere Submanifold Engine
Holonomy-Induced Pocket Universes for Reversible Narrative Ecologies

This package provides:
- NeutralManifold: ambient identity-metric manifold
- Connection: parallel transport + frame-transform composition
- Operator: reversible operator algebra
- holonomy utilities: loop transforms + Fun-Sphere triggers
- build_fun_sphere: holonomy-closed submanifold constructor
- NarrativeEcology: reversible story physics engine
"""

__version__ = "0.1.0"

from .manifold import NeutralManifold
from .connection import Connection
from .operators import Operator
from .holonomy import (
    apply_loop,
    loop_transform,
    triggers_fun_sphere,
)
from .submanifold import build_fun_sphere
from .ecology import NarrativeEcology

__all__ = [
    "NeutralManifold",
    "Connection",
    "Operator",
    "apply_loop",
    "loop_transform",
    "triggers_fun_sphere",
    "build_fun_sphere",
    "NarrativeEcology",
]
