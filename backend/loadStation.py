class LoadStation:
    def __init__(self,id , busy=0, address=None, time=0,start_time=0, src=None, fromCache = False, ins = None):
        self.id = id
        self.busy = busy
        self.address = address
        self.time = 0
        self.start_time = start_time
        self.src = src
        self.fromCache = fromCache
        self.ins = ins
    def toJSON(self):
        return {
            "id":self.id,
            "busy":self.busy,
            "address":self.address,
            "src":self.src,
        }   
    def print(self):
        print(" ")
        print("ID: "+ str(self.id))
        print("Busy: "+ str(self.busy))
        print("Address: "+ str(self.address))



