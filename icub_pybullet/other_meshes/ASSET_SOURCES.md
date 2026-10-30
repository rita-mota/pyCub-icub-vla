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

The Tinkercad source designs were publicly accessible when retrieved. Their use
and redistribution remain subject to the applicable Autodesk Tinkercad terms
and any rights stated by the original creators. They are not relicensed by this
repository under the pyCub CC BY 4.0 license unless the relevant rights holder
has authorized that licensing.

Generated files use the following naming conventions:

- `*.urdf`: simulator descriptions;
- `*_vhacd.obj`: convex-decomposed collision geometry;
- `*_vhacd.urdf`: simulator descriptions that reference the collision
  geometry.

The repository stores these lightweight assets because they are necessary to
reproduce the task scenes. Dataset recordings, rendered images, and videos are
not included.

If you redistribute these assets, retain this notice and verify the current
terms at the linked source pages.
