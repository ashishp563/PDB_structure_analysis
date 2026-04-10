# from pdb_io import read_pdb

# models = read_pdb("2MMX.pdb")

# model = models[19]
# chain = model["A"]
# residue = chain[100]
# atom = residue["CA"]

# print(chain)
# print(residue)
# print(atom)
# print(model)

# print("\nIterating over model:")
# for m in models:
#     print(m)
#     for c in m:
#         print(" ", c)
#         for r in c:
#             print("   ", r)
#             for a in r:
#                 print("     ", a)

from pdb_io import read_pdb

models = read_pdb("2MMX.pdb")
print("Models:", len(models))

model = models[2]
chain = model["A"]
residue = chain[100]
atom = residue["CA"]

print(model)
print(chain)
print(residue)
print(atom)
