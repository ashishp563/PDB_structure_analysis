class Atom:
    def __init__(self):
        self.serial = None
        self.name = None
        self.resname = None
        self.resnum = None
        self.chain = None
        self.x = self.y = self.z = None
        self.occup = None
        self.bfactor = None

    def set_data(self, line):
        self.serial = int(line[6:11])
        self.name = line[12:16].strip()
        self.resname = line[17:20].strip()
        self.chain = line[21]
        self.resnum = int(line[22:26])
        self.x = float(line[30:38])
        self.y = float(line[38:46])
        self.z = float(line[46:54])
        self.occup = float(line[54:60])
        self.bfactor = float(line[60:66])

    def __repr__(self):
        return f"<Atom {self.name} {self.resname}{self.resnum} Chain {self.chain}>"
