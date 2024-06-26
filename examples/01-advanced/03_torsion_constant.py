r"""
.. _ref_ex_advanced3:

Torsion Constant of a Rectangle
-------------------------------

Plot the variation of the torsion constant with aspect ratio of a rectangle section.

In this example, the aspect ratio of a rectangular section is varied whilst keeping a constant
cross-sectional area and the torsion constant calculated. The variation of the torsion constant
with the aspect ratio is then plotted.
"""

# sphinx_gallery_thumbnail_number = 1

import numpy as np
import matplotlib.pyplot as plt
import sectionproperties.pre.library.primitive_sections as sections
from sectionproperties.analysis.section import Section

# %%
# Rectangle dimensions
d_list = []
b_list = np.linspace(0.2, 1, 20)
j_list = []  # list holding torsion constant results

# %%
# Number of elements for each analysis
n = 100

# %%
# Loop through all the widths
for b in b_list:
    # calculate d assuming area = 1
    d = 1 / b
    d_list.append(d)

    # compute mesh size
    ms = d * b / n

    # perform a warping analysis on rectangle
    geometry = sections.rectangular_section(d=d, b=b)
    geometry.create_mesh(mesh_sizes=[ms])
    section = Section(geometry)
    section.calculate_geometric_properties()
    section.calculate_warping_properties()

    # get the torsion constant
    j = section.get_j()
    print("d/b = {0:.3f}; J = {1:.5e}".format(d / b, j))
    j_list.append(j)

# %%
# Plot the torsion constant as a function of the aspect ratio
(fig, ax) = plt.subplots()
ax.plot(np.array(d_list) / b_list, j_list, "kx-")
ax.set_xlabel("Aspect Ratio [d/b]")
ax.set_ylabel("Torsion Constant [J]")
ax.set_title("Rectangular Section Torsion Constant")
plt.show()
