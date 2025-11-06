from pdb_io import read_pdb

residues = read_pdb("6B1E.pdb")
residue1 = residues[2]
residue2 = residues[55]
min_dist = residue1.minimum_distance(residue2)
print(min_dist)
