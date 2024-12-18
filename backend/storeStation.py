class StoreStation:
    def __init__(self, busy=0, address=None, v=None, q=None, time=0, start_time=0, ins=None):
        self.busy = busy
        self.address = address
        self.v = v
        self.q = q
        self.time = time
        self.start_time = start_time
        self.ins = ins

    def toJSON(self):
        return {
            "busy":self.busy,
            "address":self.address,
            "V":self.v,
            "Q":self.q
        }
    def print(self):
        print(" ")
        print("Busy: "+ str(self.busy))
        print("Address: "+ str(self.address))
        print("V" + str(self.v))
        print("Q" + str(self.q))


