class RegisterItem:
    def __init__(self, q, value):
        self.q = q
        self.value = value
    def toJSON(self):
        return {
            "q":self.q,
            "value":self.value
        }