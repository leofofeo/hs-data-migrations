class APIKeys():
    def __init__(self, from_key, to_key):
        self.from_key = from_key
        self.to_key = to_key
    
    def get_from_key(self):
        return self.from_key
    
    def get_to_key(self):
        return self.to_key