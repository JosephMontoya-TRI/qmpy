"""This is intended to test the python 3 functionality of the TRI fork of qmpy"""

import unittest
import os
import tempfile
import shutil

from qmpy.materials.structure import Structure
TEST_DIR = os.path.dirname(os.path.abspath(__file__))


# Stub for testing phases
class PhaseTest(unittest.TestCase):
    def test_phases(self):
        pass

class VaspIOTest(unittest.TestCase):
    def setUp(self):
        self.cwd = os.getcwd()
        self.temp_dir = tempfile.mkdtemp()
        os.chdir(self.temp_dir)

    def tearDown(self):
        os.chdir(self.cwd)
        shutil.rmtree(self.temp_dir)

    def test_vasp_io(self):
        # Get structure from CIF
        # Write VASP files from structure
        pass

if __name__ == '__main__':
    unittest.main()
