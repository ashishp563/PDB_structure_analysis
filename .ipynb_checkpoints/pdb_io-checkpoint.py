from atom import Atom
from residue import Residue, create_res_id
from chain import Chain

def read_pdb(filename):
    chains = {}
    residues = {}
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
                
                if atom.chain not in chains:
                    chains[atom.chain] = Chain(atom.chain)
                if atom_res_id not in residues:
                    residue = Residue()
                    residue.set_data(line)
                    residues[atom_res_id] = residue
                    chains[atom.chain].add_residue(residue)
                residues[atom_res_id].atoms.append(atom)

    return chains
            

                
                
        
              

