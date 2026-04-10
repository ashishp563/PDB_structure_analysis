
class Chain:
    def __init__(self, chain_id):
        self.id = chain_id
        self.residues = []

    def __getitem__(self, resnum):
        for residue in self.residues:
            if residue.resnum == resnum:
                return residue
        return None

    def __iter__(self):
        return iter(self.residues)


    def __repr__(self):
        return f"<Chain {self.id}, Residues={len(self.residues)}>"
