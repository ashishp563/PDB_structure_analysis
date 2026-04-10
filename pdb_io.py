from atom import Atom
from chain import Chain
from model import Model
from residue import Residue, create_res_id


def read_pdb(filename):
    models = []
    curr_model = None
    curr_chain = None
    curr_residue = None

    with open(filename) as fh:
        for line in fh:
            line = line.rstrip()
            if not line:
                continue

      
            if line.startswith("MODEL"):
                curr_model = Model()
                curr_model.set_data(line)
                curr_model.chains = []
                models.append(curr_model)
                curr_chain = None
                curr_residue = None
                continue

          
            if line.startswith("ATOM") or line.startswith("HETATM"):
                if curr_model is None:
                    curr_model = Model()
                    models.append(curr_model)

                atom = Atom()
                atom.set_data(line)

                # CHAIN (create once per chain)
                if curr_chain is None or curr_chain.id != atom.chain:
                    curr_chain = Chain(atom.chain)
                    curr_model.chains.append(curr_chain)
                    curr_residue = None

             
                res_id = create_res_id(atom.resname, atom.resnum, atom.chain)
                if curr_residue is None or curr_residue.id != res_id:
                    curr_residue = Residue()
                    curr_residue.set_data(line)
                    curr_chain.residues.append(curr_residue)

       
                curr_residue.atoms.append(atom)

    return models

    for model in models:
        print(model)


