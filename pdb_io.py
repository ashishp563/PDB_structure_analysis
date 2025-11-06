from atom import Atom
from residue import Residue, create_res_id

def read_pdb(filename):
    residues = []
    curr_residues = None
    with open(filename) as f:
        for line in f:
            line = line.lstrip().rstrip()
            if not line:
                continue
            if line.startswith("ATOM") or line.startswith("HETATM"):
                atom = Atom()
                atom.set_data(line)

                atom_res_id = create_res_id(atom.resname, atom.resnum, atom.chain)
                
                if curr_residues is None or curr_residues.id != atom_res_id:
                    residue = Residue()
                    residue.set_data(line)
                    residue.atoms.append(atom)
                    curr_residues = residue
                    residues.append(residue)
                    print(line)
                else:
                    curr_residues.atoms.append(atom)                  


    return residues

                
                
        
              

