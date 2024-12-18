class ResStation:
    def __init__(self, id, busy=0,op=None, vj=None, vk=None, qj=None, qk=None, time =0, start_time=0, ins=None):
        self.id = id
        self.busy = busy
        self.op = op
        self.vj = vj
        self.vk = vk
        self.qj = qj
        self.qk = qk
        self.time = time
        self.start_time = start_time
        self.ins = ins

    def toJSON(self):
        return {
            "id":self.id,
            "busy":self.busy,
            "op":self.op,
            "Vj":self.vj,
            "Vk":self.vk,
            "Qj":self.qj,
            "Qk":self.qk
        }
    def print(self):
        print(" ")
        print("ID "+ str(self.id))
        print("Time "+ str(self.time))
        print("Busy "+ str(self.busy))
        print("OP "+ str(self.op))
        print("Vj " + str(self.vj))
        print("Vk " + str(self.vk))
        print("Qj " + str(self.qj))
        print("Qk " + str(self.qk))

