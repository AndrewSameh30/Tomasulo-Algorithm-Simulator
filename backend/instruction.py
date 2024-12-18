from tabulate import tabulate
class Instruction:

	def __init__(self, op, dest, src1, src2 = 0, issueTime=-1,startTime='not yet', writeBacktime=0, finishExecTime =0, ins="N/A"):
		# in case of L.D and S.D src2 will be 0
		self.op = op
		self.dest = dest
		self.src1 = src1
		self.src2 = src2
		self.issueTime = issueTime
		self.startTime = startTime
		self.writeBacktime = writeBacktime
		self.finishExecTime = finishExecTime
		self.ins = ins
	
	def print(self):
		data = []

		data.append([self.ins, self.issueTime, self.startTime, self.finishExecTime, self.writeBacktime])

		headers = ["Instruction", "Fetch", "Start Exec", "Finish Exec", "Write back"]

		print (tabulate(data, headers=headers))
		print("\n")
		print("\n")

		# print("OP "+ str(self.op))
		# print("Fetch at "+ str(self.issueTime))
		# print("Started Execution at "+ str(self.startTime))
		# print("Finished Execution at "+ str(self.finishExecTime))
		# print("Wrote Back at"+ str(self.writeBacktime))



