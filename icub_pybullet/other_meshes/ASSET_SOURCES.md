# Manipulation-object asset sources

These assets support the iCub VLA manipulation dataset-generation tasks. Rita
Alexandra da Costa Mota adapted the downloaded meshes for simulation, including
rescaling, file-format conversion, URDF creation, and generation of convex
collision meshes where required.

| Repository directories | Source |
| --- | --- |
| `box/`, `box_base/`, `box_top/` | [Box](https://www.tinkercad.com/things/8yjRacH0qjW-box) |
| `sponge/` | [Sponge](https://www.tinkercad.com/things/a8gxdHrw8D8-sponge) |
| `other_box/` | [Box Cat Box](https://www.tinkercad.com/things/cgUpiKGREtu-box-cat-box) |
| `bottle/` | [Bottle](https://www.tinkercad.com/things/fmGaWOqRl2o-bottle) |
| `computer/` | [Computer](https://www.tinkercad.com/things/0dR9j9to1St-computer) |
| `cube/` | Original cube meshes created by Rita Alexandra da Costa Mota |

The Tinkercad source designs were publicly shared when retrieved. Section I of
the [Autodesk Special Service Terms for Tinkercad](https://www.autodesk.com/company/legal-notices-trademarks/terms-of-service-autodesk360-web-services/special-service-terms-for-tinkercad)
states that publicly shared user content is licensed to other service users on
a non-exclusive, worldwide, royalty-free, fully paid, perpetual basis to copy,
display, share, distribute, use, and create derivative works, subject to those
terms.

The downloaded and adapted meshes remain subject to the applicable Tinkercad
terms and any additional rights stated by their original creators. They are not
relicensed by this repository under pyCub's CC BY 4.0 license. The source links
above are retained for provenance and attribution; downstream users should
retain this notice and review the current terms before redistribution.

Generated files use the following naming conventions:

- `*.urdf`: simulator descriptions;
- `*_vhacd.obj`: convex-decomposed collision geometry;
- `*_vhacd.urdf`: simulator descriptions that reference the collision
  geometry.

The repository stores these lightweight assets because they are necessary to
reproduce the task scenes. Dataset recordings, rendered images, and videos are
not included.
