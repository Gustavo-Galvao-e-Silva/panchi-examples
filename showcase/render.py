"""Render the panchi showcase clips with the manim backend.

Usage:
    python showcase/render.py                 # every clip, 1080p60
    python showcase/render.py low eigen       # one clip, quick preview

Requires panchi>=3.2 with the manim extra: pip install "panchi[manim]"
"""

import sys
from pathlib import Path

from panchi import Matrix, Vector, exact_matrix, exact_vector
from panchi.algorithms import solve
from panchi.visualizations import Animator2D, Animator3D

MEDIA = Path(__file__).parent / "media"


def eigenvectors(quality: str) -> None:
    Animator2D(backend="manim", save_path=MEDIA, quality=quality).animate_transform(
        Matrix([[2, 1], [1, 2]]),
        vectors=[Vector([1, 1]), Vector([1, -1]), Vector([1, 0])],
        colors=["#D4A15E", "#FFB592", "#3E7C7B"],
        show_labels=False,
        name="01_eigenvectors",
    )


def shear(quality: str) -> None:
    Animator2D(backend="manim", save_path=MEDIA, quality=quality).animate_transform(
        Matrix([[1, 1], [0, 1]]),
        vectors=[Vector([1, 0]), Vector([0, 1]), Vector([2, 1])],
        colors=["#FFB592", "#D4A15E", "#3E7C7B"],
        show_labels=False,
        name="02_shear",
    )


def transform_3d(quality: str) -> None:
    Animator3D(backend="manim", save_path=MEDIA, quality=quality).animate_transform(
        Matrix([[1, -1, 0], [1, 1, 0], [0, 0, 1]]),
        vectors=[
            Vector([1, 0, 0]),
            Vector([0, 1, 0]),
            Vector([0, 0, 1]),
            Vector([1, 1, 1]),
        ],
        name="03_transform_3d",
    )


def projection(quality: str) -> None:
    A = exact_matrix([[1, 0], [0, 1], [0, 1]])
    b = exact_vector([1, 0, 4])
    x_hat = solve(A.T @ A, A.T @ b).solution
    p = A @ x_hat
    Animator3D(backend="manim", save_path=MEDIA, quality=quality).plot_span(
        [exact_vector([1, 0, 0]), exact_vector([0, 1, 1])],
        labels=["a_1", "a_2"],
        vectors=[b, p],
        vector_labels=["b", "p"],
        gaps=[(b, p)],
        name="04_projection",
    )


CLIPS = {
    "eigen": eigenvectors,
    "shear": shear,
    "transform_3d": transform_3d,
    "projection": projection,
}


def main() -> None:
    quality = sys.argv[1] if len(sys.argv) > 1 else "high"
    selected = sys.argv[2:] or list(CLIPS)
    for key in selected:
        CLIPS[key](quality)
        print(f"rendered {key} ({quality}) -> {MEDIA}")


if __name__ == "__main__":
    main()
