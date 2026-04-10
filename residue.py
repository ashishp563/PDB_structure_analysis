def create_res_id(resname, resnum, chain):
    return f"{resname}.{resnum}.{chain}"


class Residue:
    def __init__(self):
        self.id = None
        self.resname = None
        self.resnum = None
        self.chain = None
        self.atoms = []

    def set_data(self, pdb_line):
        self.resname = pdb_line[17:20].strip()
        self.resnum = int(pdb_line[22:26])
        self.chain = pdb_line[21]
        self.id = create_res_id(self.resname, self.resnum, self.chain)

    def __getitem__(self, atom_name):
        for atom in self.atoms:
            if atom.name == atom_name:
                return atom
        return None

    def __iter__(self):
        return iter(self.atoms)


    def __repr__(self):
        return f"<Residue {self.resname}{self.resnum} chain={self.chain}>"
