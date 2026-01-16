
from pdb_io import read_pdb

chains = read_pdb("6B1E.pdb")


chainA = chains["A"]
chainB = chains["B"]

dist = chainA.minimum_distance(chainB)

print("Distance between chain A and B:", dist)
