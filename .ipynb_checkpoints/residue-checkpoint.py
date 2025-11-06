

def create_res_id(resname, resnum, chain):
    return f"{resname}.{resnum}.{chain}"
class Residue:
    def __init__(self):
        self.id = None
        self.atoms = []
        self.resnum = None
        self.resname = None
        self.chain = None

    def set_data(self, pdb_line):
        self.resname=pdb_line[17:20].lstrip().rstrip()
        self.resnum=pdb_line[22:26].lstrip().rstrip()
        self.chain = pdb_line[21]
        self.id = create_res_id(self.resname,self.resnum,self.chain)

    def minimum_distance(self, otherRes):
        min_dist=None
        for a1 in self.atoms:
            for a2 in otherRes.atoms:
                dist = a1.distance(a2)
                if min_dist is None:
                    min_dist= dist
                    continue
                if dist < min_dist:
                    min_dist = dist
        return dist

    def __repr__(self):
        return f"<name={self.resname}, num={self.resnum}, chain={self.chain}, numAtoms={len(self.atoms)}>"