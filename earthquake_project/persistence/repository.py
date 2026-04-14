class Repository:
    def __init__(self):
        self.cache = []

    def save(self, records):
        self.cache = records

    def get_all(self):
        return self.cache