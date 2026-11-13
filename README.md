<div align="center">
    <picture>
        <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Gustavo-Galvao-e-Silva/panchi/main/docs/assets/logo/panchi_logo_white.png">
        <img src="https://raw.githubusercontent.com/Gustavo-Galvao-e-Silva/panchi/main/docs/assets/logo/panchi_logo_color.png" alt="panchi" width=280>
    </picture>
</div>

# panchi examples

**A guided tour of [panchi](https://github.com/Gustavo-Galvao-e-Silva/panchi) through a first course in linear algebra.**

Concept → code → step-by-step output. One notebook per topic.

<div align="center">
<a href="https://github.com/Gustavo-Galvao-e-Silva/panchi"><img src="https://img.shields.io/badge/built%20with-panchi-A52A2A.svg" alt="Built with panchi"></a>
<a href="https://jupyter.org/"><img src="https://img.shields.io/badge/Jupyter-notebooks-F37626.svg?logo=jupyter&logoColor=white" alt="Jupyter"></a>
<a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/python-3.10+-blue.svg" alt="Python 3.14+"></a>
</div>

---

## Why these notebooks?

panchi optimizes for **understanding**, not speed. These notebooks meet it halfway: instead of an API reference, they walk through the actual material of a first linear algebra course and let panchi do the talking.

Each notebook follows the same rhythm:

> **concept explanation → panchi code → step-by-step output**

The aim is to _see the math happen_: spans you can picture, reductions that show every step, transformations you can watch — rather than to memorize function signatures.

Think of it as a **workbook**, not a manual.

---

## Getting Started

These examples track [`panchi`](https://pypi.org/project/panchi/) and run in plain Jupyter.

```bash
# clone the examples
git clone https://github.com/Gustavo-Galvao-e-Silva/panchi-examples.git
cd panchi-examples

# install with uv (recommended)
uv sync

# ...or with pip
pip install panchi jupyter
```

Then launch the lab and open a notebook:

```bash
jupyter lab notebooks/
```

Requires Python 3.14+. For the Manim-powered visualizations, install panchi's optional extra:

```bash
pip install "panchi[manim]"
```

---

## Showcase

Short clips rendered with panchi's manim backend. Click a preview for the full 1080p60 video.

| | |
| :---: | :---: |
| <a href="showcase/media/01_eigenvectors.mp4"><img src="showcase/media/previews/01_eigenvectors.gif" width="400" alt="Eigenvectors of [[2,1],[1,2]]"></a> | <a href="showcase/media/02_shear.mp4"><img src="showcase/media/previews/02_shear.gif" width="400" alt="A shear transformation"></a> |
| **Eigenvectors.** Under `[[2, 1], [1, 2]]`, the gold and peach vectors stay on their own lines and only stretch, by 3 and by 1. The teal vector turns. | **Shear.** `[[1, 1], [0, 1]]` slides the grid sideways while the x-axis stays fixed. |
| <a href="showcase/media/03_transform_3d.mp4"><img src="showcase/media/previews/03_transform_3d.gif" width="400" alt="A 3D linear transformation"></a> | <a href="showcase/media/04_projection.mp4"><img src="showcase/media/previews/04_projection.gif" width="400" alt="Projection onto a plane"></a> |
| **3D transformation.** A 45° rotation about the z-axis combined with a stretch, acting on vectors in R³. | **Least squares.** `b` isn't on the plane spanned by `a₁, a₂`, so it's projected to the closest point `p = [1, 2, 2]`, solved exactly from the normal equations `AᵀA x̂ = Aᵀb`. |

To re-render them, or to tweak the matrices and render your own:

```bash
pip install "panchi[manim]"        # panchi 3.2 or newer
python showcase/render.py          # every clip, 1080p60
python showcase/render.py low eigen   # one clip, quick preview
```

---

## Notebooks

| #   | Notebook                                                                            | Topics                                                      | Strang reference |
| --- | ----------------------------------------------------------------------------------- | ----------------------------------------------------------- | ---------------- |
| 01  | [Vectors & Linear Combinations](notebooks/01_vectors_and_linear_combinations.ipynb) | vector arithmetic, span, linear independence, `VectorSpace` | §1.2, §2.1       |

### 01 · Vectors & Linear Combinations

Introduces panchi's core `Vector` and `VectorSpace` objects. Starting from simple vector arithmetic, the notebook builds up to span and linear independence, using short code stubs and visualizations to make each idea concrete.

_More notebooks are on the way!_

---

## How to read a notebook

Every notebook is self-contained and meant to be run top to bottom. The prose sets up the concept, the code cell is small enough to read in one sitting, and the output is where panchi earns its keep: full step-by-step walkthroughs rather than a lone answer. Run a cell, read what it prints, then change a number and run it again.

---

## Related

- **[panchi](https://github.com/Gustavo-Galvao-e-Silva/panchi)**: the library these notebooks demonstrate
- **[Documentation](https://gustavo-galvao-e-silva.github.io/panchi/)**: full user guides and API reference

---

## License

MIT License: see [LICENSE](LICENSE) for details.

---

## Acknowledgments

These notebooks follow Gilbert Strang's _Introduction to Linear Algebra_ and draw visual intuition from 3Blue1Brown's _Essence of Linear Algebra_.
