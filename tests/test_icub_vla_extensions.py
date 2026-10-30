"""Lightweight checks for the iCub VLA publication extensions."""

from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

import numpy as np

from icub_pybullet.pycub import Joint, pyCub
from icub_pybullet.visualizer import Visualizer


REPOSITORY_ROOT = Path(__file__).resolve().parents[1]
MESH_ROOT = REPOSITORY_ROOT / "icub_pybullet" / "other_meshes"
REQUIRED_ASSET_DIRECTORIES = {
    "bottle",
    "box",
    "box_base",
    "box_top",
    "computer",
    "cube",
    "other_box",
    "sponge",
}


class JointHandleTests(unittest.TestCase):
    def setUp(self):
        self.joint = Joint("neck_yaw", 3, 2, -1.0, 1.0, 10.0, 2.0)
        self.client = type("Client", (), {"joints": [self.joint]})()

    def test_returns_matching_joint(self):
        self.assertIs(pyCub.get_joint_handle(self.client, "neck_yaw"), self.joint)

    def test_unknown_joint_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "missing_joint"):
            pyCub.get_joint_handle(self.client, "missing_joint")


class FixedCameraTests(unittest.TestCase):
    def test_pose_update_preserves_numeric_values(self):
        camera = object.__new__(Visualizer.FixedCameraWindow)
        camera.set_camera_pose([1, 2, 3], [4, 5, 6])

        np.testing.assert_array_equal(camera.eye_pos, [1.0, 2.0, 3.0])
        np.testing.assert_array_equal(camera.eye_target, [4.0, 5.0, 6.0])


class AssetTests(unittest.TestCase):
    def test_required_asset_directories_are_present(self):
        present = {path.name for path in MESH_ROOT.iterdir() if path.is_dir()}
        self.assertTrue(REQUIRED_ASSET_DIRECTORIES <= present)

    def test_urdf_mesh_references_are_relative_and_resolve(self):
        urdf_paths = [
            path
            for directory in REQUIRED_ASSET_DIRECTORIES
            for path in (MESH_ROOT / directory).rglob("*.urdf")
        ]
        self.assertTrue(urdf_paths)

        for urdf_path in urdf_paths:
            root = ET.parse(urdf_path).getroot()
            for mesh in root.iter("mesh"):
                filename = mesh.attrib["filename"]
                with self.subTest(urdf=urdf_path.name, mesh=filename):
                    self.assertFalse(Path(filename).is_absolute())
                    self.assertTrue((urdf_path.parent / filename).is_file())


if __name__ == "__main__":
    unittest.main()
