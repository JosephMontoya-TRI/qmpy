from pymatgen.io.vasp.sets import DictSet
from monty.serialization import loadfn


class OQMDInputSet(DictSet):
    CONFIG = loadfn("OQMDStaticSet.yaml")
    def __init__(self, structure):
        self.structure = structure



