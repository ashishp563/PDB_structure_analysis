class Model:
    def __init__(self):
        self.id = 0
        self.chains = []

    def set_data(self, line):
        if line.startswith("MODEL"):
            self.id = int(line.split()[1])

    def __getitem__(self, chain_id):
        for chain in self.chains:
            if chain.id == chain_id:
                return chain
        return None

    def __iter__(self):
        return iter(self.chains)


    def __repr__(self):
        return f"<Model id={self.id}, NumChains={len(self.chains)}>"
