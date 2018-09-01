.. _label-post:

Viewing the Results
===================

Printing a List of the Section Properties
-----------------------------------------

A list of section properties that have been calculated by various analyses can
be printed to the terminal using the :func:`~sectionproperties.analysis.cross_section.CrossSection.display_results`
method that belongs to every
:class:`~sectionproperties.analysis.cross_section.CrossSection` object.

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.display_results
    :noindex:

Getting Specific Section Properties
-----------------------------------

Alternatively, there are a number of methods that can be called on the
:class:`~sectionproperties.analysis.cross_section.CrossSection` object to return
a specific section property:

Cross Section Area
^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_area
    :noindex:

First Moments of Area (Global Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_q
    :noindex:

Second Moments of Area (Global Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_ig
    :noindex:

Elastic Centroid
^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_c
    :noindex:

Second Moments of Area (Centroidal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_ic
    :noindex:

Section Moduli (Centroidal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_z
    :noindex:

Radii of Gyration (Centroidal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_rc
    :noindex:

Second Moments of Area (Principal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_ip
    :noindex:

Principal Axis Angle
^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_phi
    :noindex:

Section Moduli (Principal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_zp
    :noindex:

Radii of Gyration (Principal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_rp
    :noindex:

Torsion Constant
^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_j
    :noindex:

Shear Centre (Global Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_sc
    :noindex:

Shear Centre (Principal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_sc_p
    :noindex:

Trefftz's Shear Centre (Global Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_sc_t
    :noindex:

Warping Constant
^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_gamma
    :noindex:

Shear Area (Global Axis)
^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_As
    :noindex:

Shear Area (Principal Axis)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.get_As_p
    :noindex:


Section Property Centroids Plots
--------------------------------

A plot of the centroids (elastic, plastic and shear centre) can be produced with
the finite element mesh in the background:

..  automethod:: sectionproperties.analysis.cross_section.CrossSection.plot_centroids
    :noindex:

Plotting Cross-Section Stresses
-------------------------------

There are a number of methods that can be called from a :class:`~sectionproperties.analysis.cross_section.StressResult`
object to plot the various cross-section stresses. These methods take the following form:

  :class:`~sectionproperties.analysis.cross_section.StressResult`.plot_(*stress/vector*)_(*action*)_(*stresstype*)

where:

- *stress* denotes a contour plot and *vector* denotes a vector plot.
- *action* denotes the type of action causing the stress e.g. *mxx* for bending moment about the x-axis. Note that the action is omitted for stresses caused by the application of all actions.
- *stresstype* denotes the type of stress that is being plotted e.g. *zx* for the *x*-component of shear stress.

Primary Stress Plots
^^^^^^^^^^^^^^^^^^^^

Axial Stress (:math:`\sigma_{zz,N}`)
""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_n_zz
    :noindex:

Bending Stress (:math:`\sigma_{zz,Mxx}`)
""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_mxx_zz
    :noindex:

Bending Stress (:math:`\sigma_{zz,Myy}`)
""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_myy_zz
    :noindex:

Bending Stress (:math:`\sigma_{zz,M11}`)
""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_m11_zz
    :noindex:

Bending Stress (:math:`\sigma_{zz,M22}`)
""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_m22_zz
    :noindex:

Bending Stress (:math:`\sigma_{zz,\Sigma M}`)
"""""""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_m_zz
    :noindex:

Torsion Stress (:math:`\sigma_{zx,Mzz}`)
""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_mzz_zx
    :noindex:

Torsion Stress (:math:`\sigma_{zy,Mzz}`)
""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_mzz_zy
    :noindex:

Torsion Stress (:math:`\sigma_{zxy,Mzz}`)
"""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_mzz_zxy
    :noindex:

..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_vector_mzz_zxy
    :noindex:

Shear Stress (:math:`\sigma_{zx,Vx}`)
"""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vx_zx
    :noindex:

Shear Stress (:math:`\sigma_{zy,Vx}`)
"""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vx_zy
    :noindex:

Shear Stress (:math:`\sigma_{zxy,Vx}`)
""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vx_zxy
    :noindex:

..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_vector_vx_zxy
    :noindex:

Shear Stress (:math:`\sigma_{zx,Vy}`)
"""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vy_zx
    :noindex:

Shear Stress (:math:`\sigma_{zy,Vy}`)
"""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vy_zy
    :noindex:

Shear Stress (:math:`\sigma_{zxy,Vy}`)
""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vy_zxy
    :noindex:

..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_vector_vy_zxy
    :noindex:

Shear Stress (:math:`\sigma_{zx,\Sigma V}`)
"""""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_v_zx
    :noindex:

Shear Stress (:math:`\sigma_{zy,\Sigma V}`)
"""""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_v_zy
    :noindex:

Shear Stress (:math:`\sigma_{zxy,\Sigma V}`)
""""""""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_v_zxy
    :noindex:

..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_vector_v_zxy
    :noindex:

Combined Stress Plots
^^^^^^^^^^^^^^^^^^^^^

Normal Stress (:math:`\sigma_{zz}`)
""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_zz
    :noindex:

Shear Stress (:math:`\sigma_{zx}`)
"""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_zx
    :noindex:

Shear Stress (:math:`\sigma_{zy}`)
"""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_zy
    :noindex:

Shear Stress (:math:`\sigma_{zxy}`)
""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_zxy
    :noindex:

..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_vector_zxy
    :noindex:

von Mises Stress (:math:`\sigma_{vM}`)
"""""""""""""""""""""""""""""""""""""""
..  automethod:: sectionproperties.analysis.cross_section.StressResult.plot_stress_vm
    :noindex: