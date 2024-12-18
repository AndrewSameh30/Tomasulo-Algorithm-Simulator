import sys
import random
from instruction import Instruction
from resStation import ResStation
from storeStation import StoreStation
from loadStation import LoadStation
from registerItem import RegisterItem


from tabulate import tabulate

import colorama
from colorama import Fore

class OnlineMain:
	# t = test.Test()
	# t.testo()


	# 3 load and store buffers
	# 3 add/sub 
	# 2 mul
	# reg file 32 reg

	# first, we will take config inputs. latency of each instruction

	# will be array of cycles
	# each cycle contains the following tables (addStation, mulStation, loadStation, storeStation, register file content, instructions Q, status content)
	# each cycle will be object

	response = [
				{
				"addStation":None,
				 "mulStation":None,
				 "loadStation":None,
				 "storeStation":None,
				 "regs":None,
				 "instructionsQ":None,
				 "statusContent":None
				 }
	]
	responseIndex = 0

	instructions = []
	decoded_instructions = []





	mulResStations = []
	addResStations = []

	storeResStations = []
	loadResStations = []

	# issued at 1
	# executnig from 2 to 41
	# writing at 42

	cycle = 1

	
	instructionIndex = 0

	lastExecutedInstruction = 0
	totalInstructionsCount = 0



	#memory size will be 100 element
	memory = [i for i in range(100)]

	registers = []
	for x in range(32):
		registers.append(RegisterItem(0,x+1))






	global busId 
	busId = ''

	mulResS = 2
	while (mulResS > 0):
		mulResStations.append(ResStation('M'+str(2-mulResS+ 1)))
		mulResS -= 1

	addResS = 3
	while (addResS > 0):
		addResStations.append(ResStation('A'+str(3-addResS+ 1)))
		addResS -=1


	storeResS = 3
	while (storeResS > 0):
		storeResStations.append(StoreStation())
		storeResS -=1

	loadResS = 2
	while (loadResS > 0):
		loadResStations.append(LoadStation('L'+ str(2- loadResS + 1)))
		loadResS -=1






	def decode(self, instruction):
		print(f"Decoding instruction: {instruction}")  # Debugging line
		print(f"Decoding: {instruction}")  # Debugging line
		# Add this to track if instructions are decoded
		print(f"Decoded instructions so far: {self.decoded_instructions}")
		ready_format = []
		splitted_instruction = instruction.split(" ",1)
		# now we got the instruction at position 0
		# and a remainging string that contains the arguments 
		print(splitted_instruction)
		ready_format.append(splitted_instruction[0])

		args = splitted_instruction[1]
		args = args.replace(' ', '')
		args = args.split(",")
		ready_format += args

		splitted_instruction = ready_format


		if(not self.validateInastructionFormat(splitted_instruction)):
			print("WRONG INSTRUCTION FORMAT")
			sys.exit()
			return


		#goal is to end up with the following format [instruction, arg1, arg2..]
#  op, dest, src1, src2 = 0, issueTime=0,startTime=0, writeBacktime=0, finishExecTime =0, ins="N/A"
		try:
			op = splitted_instruction[0]
			if(op == 'L.D' or op =='S.D'):
				# dest/src and imm ( address )
				dest = splitted_instruction[1]
				imm = splitted_instruction[2]
				new_instruction = Instruction(op, dest, imm)
				new_instruction.ins = instruction
				self.decoded_instructions.append(new_instruction)
			else:
				dest = splitted_instruction[1]
				src1 = splitted_instruction[2]
				src2 = splitted_instruction[3]
				new_instruction = Instruction(op, dest, src1, src2)
				new_instruction.ins = instruction
				self.decoded_instructions.append(new_instruction)
		except Exception as e:
			print(e)


	def printInstruction(self, instruction):
		print(" ")

		print("OP: "+ str(instruction.op))
		print("Dest: "+ str(instruction.dest))
		print("Src1: "+ str(instruction.src1))
		print("Src2: "+ str(instruction.src2))

	def validateFunc(self, op):
		OPs = ["ADD.D", "SUB.D", "DIV.D", "MUL.D", "L.D", "S.D"]
		for opi in OPs:
			if(opi == op):
				return op
		print("Function " +str(op) + " is N/A")
		return False


	def validateRegister(self, register):
		regIndex = register.split("F")[1]
		if(int(regIndex) > 32 or int(regIndex) < 0):
			print("Register "+ str(regIndex) +" Is N/A")
			return False

		return True

	def valdiateMemoryAddress(self, address):
		if(int(address) > len(self.memory) or int(address) < 0):
			print("Memory Address "+ str(address) +" Is N/A")
			return False
		return True

	def validateInastructionFormat(self, instruction):

		#validate ins[0]. must be any of ADD.D, SUB.D, MUL.D, DIV,D, L.D, S.D 
		correctOP = self.validateFunc(instruction[0])
		#validate memory ops
		if(correctOP == False):
			return False
		if(correctOP == "L.D" or correctOP == "S.D"):
			#validate memory op
			#instruction[1] contains register
			#instruction[2] contains address

			return self.validateRegister(instruction[1]) and self.valdiateMemoryAddress(instruction[2])
		else:
			# ALU OP
			#all 1,2,3 are registers
			return self.validateRegister(instruction[1]) and self.validateRegister(instruction[2]) and self.validateRegister(instruction[3])


		return False




	def getInput(self, message):
		inputUser = ""
		while True:
			try:
				inputUser = int(input(message))
			except ValueError:
				print("Please enter a valid input")
				continue
			else:
				return inputUser
				break
	def start(self, mul, div, add, sub, l, s, instructions):
		print(f"Instructions received: {instructions}")  # Debugging line
		print(f"Instructions received: {instructions}")  # Debugging line
		f = open("stagesLog.txt", "a")
		f.truncate(0)
		f2 = open("stationsLog.txt", "a")
		f2.truncate(0)

		mul_latency = mul
		add_latency = add
		sub_latency = sub
		div_latency = div

		load_latency = l
		store_latency = s

		print(' ')
		print('Enter your instructions')
		print('Press E to stop writing your instructions')
		print(' ')




		# while(True):
		# 	userInput = input("Enter your instruction ")
		# 	if(userInput == 'E'):
		# 		break
		# 	else:
		# 		# validate the instruction format
		# 		self.instructions.append(userInput)


		for ins in instructions:
			print(ins)
			self.instructions.append(ins)

		#assign the length of the instruction array to totalInstructionsCount
		self.totalInstructionsCount = len(self.instructions)
			
		#decode the instructions
		for ins in self.instructions:
			try:
				# Add this to track if instructions are decoded
				print(f"Decoded instructions so far: {self.decoded_instructions}")
				print(f"Decoding instruction: {ins}")  # Debugging line
				self.decode(ins)
			except:
				print(f"Error in decoding: {e}")
				print("Instruction "+ str(ins) + " is in the wrong format")
				sys.exit()

		# for ins in self.decoded_instructions:
		# 	self.printInstruction(ins)

		def firstEmptyStation(stations):
			index = 0
			for station in stations:
				if(station.busy == 0):
					return index
				index += 1
			return -1

		def getResStationIndex(op):

			if(op == 'ADD.D' or op == 'SUB.D'):
				return firstEmptyStation(self.addResStations)

			if(op == 'MUL.D' or op == 'DIV.D'):
				return firstEmptyStation(self.mulResStations)

			if(op == 'L.D'):
				return firstEmptyStation(self.loadResStations)
			
			if(op == 'S.D'):
				return firstEmptyStation(self.storeResStations)
			return -1

		def getRegisterValue(register):

			# register will be in the following format F1 , F22 ['F', 22]
			registerIndex = register.split("F")[1]
			q = self.registers[int(registerIndex)].q



			if(q == 0):
				return  self.registers[int(registerIndex)].value
			return q # 'A1' 'M1' ..

		def updateQofRegister(stationId, register):
			registerIndex = register.split("F")[1]
			self.registers[int(registerIndex)].q = stationId


		def canWeFetchLoad(address):
			for station in self.storeResStations:
				if(station.busy == 1):
					if(int(station.address) == int(address)):
						print("can't fetch this load. address clash")
						return False # cant fetch load
			return True

		def canWeFetchStore(address):
			for station in self.storeResStations:
				if(station.busy == 1):
					if(int(station.address) == int(address)):
						print("can't fetch this store. address clash")
						return False # cant fetch store

			for station in self.loadResStations:
				if(station.busy == 1):
					if(int(station.address) == int(address)):
						print("can't fetch this store. address clash")
						return False # cant fetch store
			return True

		# #fetch
		# def fetch():
		# 	if not self.instructions:  # Check if there are no instructions left in the queue
		# 		print("Instruction queue is empty. Exiting fetch stage.")
		# 		return  # Exit fetch if no instructions are left

		# 	instruction = self.instructions.pop(0)  # Pop the first instruction from the queue
		# 	print(f"Fetching instruction: {instruction}")
		# 	print(f"Fetching instruction: {self.instructions[self.instructionIndex]}")  # Debugging line
		# 	if(self.instructionIndex >= len(self.decoded_instructions)):
		# 		return
		# 	#Fix Q and V depending on the register file. Update the Q in the register file if an instruction is going to update its value
		# 	print(Fore.WHITE +"fetch "+ str(self.instructions[self.instructionIndex]))
		# 	f.write("Trying to fetch "+ str(self.instructions[self.instructionIndex])+"\n")

		# 	tmpInstruction = self.decoded_instructions[self.instructionIndex]
		# 	op = tmpInstruction.op
		# 	stationIndex = getResStationIndex(op)
		# 	# we wanna see if there is an ava res station. By its OP
		# 	if(stationIndex == -1):
		# 		print('no available station')
		# 		f.write("no available station"+"\n")
		# 		return 

		# 	else:
		# 		tmpInstruction.issueTime = self.cycle

		# 		if(op == 'ADD.D' or op == 'SUB.D' or op == 'MUL.D' or op == 'DIV.D'):

		# 			currentStation = self.addResStations
		# 			station = 'A'
		# 			time = add_latency 
		# 			if(op == 'SUB.D'):
		# 				time = sub_latency
		# 			if(op == 'MUL.D' or op == 'DIV.D'):
		# 				currentStation = self.mulResStations
		# 				station = 'M'
		# 				time = mul_latency
		# 				if(op == 'DIV.D'):
		# 					time = div_latency


						
		# 			currentStation[stationIndex].busy = 1
		# 			currentStation[stationIndex].op = op.replace('.D', '')
		# 			currentStation[stationIndex].ins = tmpInstruction

		# 			if(type(getRegisterValue(tmpInstruction.src1)) is int ):
		# 				currentStation[stationIndex].vj = getRegisterValue(tmpInstruction.src1)
		# 			else:
		# 				currentStation[stationIndex].qj = getRegisterValue(tmpInstruction.src1)

		# 			if(type(getRegisterValue(tmpInstruction.src2)) is int ):
		# 				currentStation[stationIndex].vk = getRegisterValue(tmpInstruction.src2)
		# 			else:
		# 				currentStation[stationIndex].qk = getRegisterValue(tmpInstruction.src2)
		# 			currentStation[stationIndex].time = time
		# 			currentStation[stationIndex].start_time = self.cycle + 1

		# 			updateQofRegister(str(currentStation[stationIndex].id),tmpInstruction.dest)



		# 		if(op == 'L.D'):
		# 			if(not canWeFetchLoad(tmpInstruction.src1)):
		# 				print("Can't fetch this load.")
		# 				return
		# 			givenLatency = load_latency


		# 			self.loadResStations[stationIndex].busy = 1
		# 			self.loadResStations[stationIndex].src = tmpInstruction.dest
		# 			self.loadResStations[stationIndex].address = tmpInstruction.src1
		# 			self.loadResStations[stationIndex].time = givenLatency
		# 			self.loadResStations[stationIndex].start_time = self.cycle + 1
		# 			self.loadResStations[stationIndex].start_time = self.cycle + 1
		# 			self.loadResStations[stationIndex].ins = tmpInstruction


		# 			updateQofRegister(str(self.loadResStations[stationIndex].id),tmpInstruction.dest)



		# 			# self.loadResStations[stationIndex].print()


				
		# 		if(op == 'S.D'):
		# 			if(not canWeFetchStore(tmpInstruction.src1)):
		# 				print("Can't fetch this store.")
		# 				return
		# 			self.storeResStations[stationIndex].busy = 1
		# 			self.storeResStations[stationIndex].address = tmpInstruction.src1
		# 			self.storeResStations[stationIndex].ins = tmpInstruction


		# 			if(type(getRegisterValue(tmpInstruction.dest)) is int ):
		# 				self.storeResStations[stationIndex].v = getRegisterValue(tmpInstruction.dest)
		# 			else:
		# 				self.storeResStations[stationIndex].q = getRegisterValue(tmpInstruction.dest)
		# 			self.storeResStations[stationIndex].time = store_latency
		# 			self.storeResStations[stationIndex].start_time = self.cycle + 1
		# 			# self.storeResStations[stationIndex].print()

		# 		self.instructionIndex += 1

		def fetch():
			# Check if the instruction queue is empty or if the instructionIndex is out of bounds
			if not self.instructions or self.instructionIndex >= len(self.instructions):
				print("Instruction queue is empty or index out of bounds. Exiting fetch.")
				return  # Exit if no instructions or out of bounds

			# Fetch the next instruction from the instruction queue
			instruction = self.instructions[self.instructionIndex]
			print(f"Fetching instruction: {instruction}")

			# Check if the decoded instructions are available
			if self.instructionIndex >= len(self.decoded_instructions):
				print("Decoded instructions not available yet.")
				return  # Exit if the decoded instructions are not available

			# Get the current instruction
			tmpInstruction = self.decoded_instructions[self.instructionIndex]
			op = tmpInstruction.op

			# Get the index for the reservation station
			stationIndex = getResStationIndex(op)
			if stationIndex == -1:
				print(f"No available reservation station for {op}")
				return  # Exit if no available station

			tmpInstruction.issueTime = self.cycle  # Update issue time

			# Handle different operation types (ADD.D, SUB.D, MUL.D, DIV.D)
			if op in ['ADD.D', 'SUB.D', 'MUL.D', 'DIV.D']:
				currentStation = self.addResStations if op in ['ADD.D', 'SUB.D'] else self.mulResStations
				time = add_latency if op == 'ADD.D' else sub_latency if op == 'SUB.D' else mul_latency
				if op == 'DIV.D':
					time = div_latency
				
				# Update the reservation station with the current instruction
				currentStation[stationIndex].busy = 1
				currentStation[stationIndex].op = op.replace('.D', '')
				currentStation[stationIndex].ins = tmpInstruction

				# Set values or queues based on register values
				if isinstance(getRegisterValue(tmpInstruction.src1), int):
					currentStation[stationIndex].vj = getRegisterValue(tmpInstruction.src1)
				else:
					currentStation[stationIndex].qj = getRegisterValue(tmpInstruction.src1)

				if isinstance(getRegisterValue(tmpInstruction.src2), int):
					currentStation[stationIndex].vk = getRegisterValue(tmpInstruction.src2)
				else:
					currentStation[stationIndex].qk = getRegisterValue(tmpInstruction.src2)

				currentStation[stationIndex].time = time
				currentStation[stationIndex].start_time = self.cycle + 1
				updateQofRegister(str(currentStation[stationIndex].id), tmpInstruction.dest)

			elif op == 'L.D':
				if not canWeFetchLoad(tmpInstruction.src1):
					print("Can't fetch this load.")
					return

				self.loadResStations[stationIndex].busy = 1
				self.loadResStations[stationIndex].src = tmpInstruction.dest
				self.loadResStations[stationIndex].address = tmpInstruction.src1
				self.loadResStations[stationIndex].time = load_latency
				self.loadResStations[stationIndex].start_time = self.cycle + 1
				self.loadResStations[stationIndex].ins = tmpInstruction
				updateQofRegister(str(self.loadResStations[stationIndex].id), tmpInstruction.dest)

			elif op == 'S.D':
				if not canWeFetchStore(tmpInstruction.src1):
					print("Can't fetch this store.")
					return

				self.storeResStations[stationIndex].busy = 1
				self.storeResStations[stationIndex].address = tmpInstruction.src1
				self.storeResStations[stationIndex].ins = tmpInstruction

				if isinstance(getRegisterValue(tmpInstruction.dest), int):
					self.storeResStations[stationIndex].v = getRegisterValue(tmpInstruction.dest)
				else:
					self.storeResStations[stationIndex].q = getRegisterValue(tmpInstruction.dest)

			# Move to the next instruction
			self.instructionIndex += 1


		def readyStation(station):
			return station.vk != None and station.vj != None

			
		def execute():
			#check every station.
			#ADD
			for station in self.addResStations:

				if(station.busy == 1 and self.cycle >= station.start_time and readyStation(station)):
					if(station.time > 0):
						if(station.ins.startTime == 'not yet'):
							station.ins.startTime = self.cycle

						print(Fore.WHITE +"Executing "+ station.id)
						f.write("Executing "+ station.id+"\n")

					station.time -= 1
					if(station.time == 0):
						station.ins.finishExecTime = self.cycle
						print("Done executng Add "+ station.id)
						f.write("Done executng Add "+ station.id+"\n")


			#MUL
			for station in self.mulResStations:
				if(station.busy == 1 and self.cycle >= station.start_time and readyStation(station)):
					if(station.time > 0):
						if(station.ins.startTime == 'not yet'):
							station.ins.startTime = self.cycle
						print(Fore.WHITE +"Executing "+ station.id)
						f.write("Executing "+ station.id+"\n")

					station.time -= 1
					if(station.time == 0):
						station.ins.finishExecTime = self.cycle
						print("Done executng MUL "+ station.id)
						f.write("Done executng MUL "+ station.id+"\n")


			#LOAD
			for station in self.loadResStations:
				if(station.busy == 1 and self.cycle >= station.start_time):
					if(station.time > 0):
						if(station.ins.startTime == 'not yet'):
							station.ins.startTime = self.cycle
						print(Fore.WHITE +"Executing "+ station.id)
						f.write("Executing "+ station.id+"\n")

					station.time -= 1
					if(station.time == 0):
						if(station.ins.startTime == 'not yet'):
							station.ins.startTime = self.cycle
						station.ins.finishExecTime = self.cycle
						print("Done executng LOAD "+ station.id)
						f.write("Done executng LOAD "+ station.id+"\n")


			#STORE
			for station in self.storeResStations:
				if(station.busy == 1 and self.cycle >= station.start_time and station.v != None):
					if(station.time > 0):
						if(station.ins.startTime == 'not yet'):
							station.ins.startTime = self.cycle
						print(Fore.WHITE +"Executing Store")
						f.write("Executing Store\n")


					station.time -= 1
					if(station.time == 0):
						station.ins.finishExecTime = self.cycle
						print("Done executng STORE ")
						f.write("Done executng STORE "+"\n")
					



		def add(a, b):
			return a + b
		def sub(a,b):
			return a - b
		def mul(a,b):
			return a*b 
		def div(a,b):
			return int(a/b)

		def load(register, address):
			registerIndex = register.split("F")[1]

			self.registers[int(registerIndex)].q = 0
			self.registers[int(registerIndex)].value = self.memory[int(address)]

		def updateBus(stationId, value):
			#check registers 
			print(Fore.WHITE +"Writing Back "+ str(stationId) +" By "+ str(value))
			f.write("Writing Back "+ str(stationId) +" By "+ str(value)+"\n")


			for reg in self.registers:
				if(reg.q == stationId):
					reg.q = 0
					reg.value = value



			#check add
			for station in self.addResStations:
				if(station.qj == stationId):
					station.qj = None
					station.vj = value
				if(station.qk == stationId):
					station.qk = None
					station.vk = value


			#check mul
			for station in self.mulResStations:
				if(station.qj == stationId):
					station.qj = None
					station.vj = value
				if(station.qk == stationId):
					station.qk = None
					station.vk = value
			#check store 
			for station in self.storeResStations:
				if(station.q == stationId):
					station.q = None
					station.v = value


		def restALUStation(station):
			station.busy = 0
			station.vj = None
			station.vk = None
			station.qj = None
			station.qk = None
			station.op = None

		def writeBackAdd():
			for station in self.addResStations:
				if(station.busy == 1):
					if(station.time <= -1):
						station.ins.writeBacktime = self.cycle
						res = 0
						if(station.op == 'ADD'):
							res = add(station.vj, station.vk)
						if(station.op == 'SUB'):
							res = sub(station.vj, station.vk)
						updateBus(station.id, res)
						restALUStation(station)		
						self.lastExecutedInstruction += 1
						return True
			return False

		def writeBackMul():
			for station in self.mulResStations:
				if(station.busy == 1):
					if(station.time <= -1):
						station.ins.writeBacktime = self.cycle
						
						res = 0
						if(station.op == 'MUL'):
							res = mul(station.vj, station.vk)
						if(station.op == 'DIV'):
							res = div(station.vj, station.vk)
						updateBus(station.id, res)
						restALUStation(station)
						self.lastExecutedInstruction += 1
						return True
			return False

		def writeBackLoad():
			for station in self.loadResStations:
				if(station.busy == 1 ):

					if(station.time <= -1):
						# load(station.src, station.address)
						loadValue = self.memory[int(station.address)]
						updateBus(station.id, loadValue)
						station.busy = 0
						station.address = None
						station.ins.writeBacktime = self.cycle
						self.lastExecutedInstruction += 1
						return True
			return False

		def writeBackStore():
			for station in self.storeResStations:	
				if(station.busy == 1 ):
					if(station.time <= -1):
						print(Fore.WHITE + "Writing back store")
						self.memory[int(station.address)] = station.v
						station.busy = 0
						station.v = None
						station.q = None
						station.ins.writeBacktime = self.cycle
						self.lastExecutedInstruction += 1
						return True
			return False

		def writeBack():
			#check every station.
			options=[0,1,2,3]
			random.shuffle(options)

			for resIndex in options:
				if(resIndex == 0):
					#ADD 
					if(writeBackAdd() == True):
						return
				if(resIndex == 1):
					#MUL
					if(writeBackMul() == True):
						return
				if(resIndex == 2):
					#LOAD
					if(writeBackLoad() == True):
						return
				if(resIndex == 3):
					#STORE
					if(writeBackStore() == True):
						return

		def printRegisters():
			data = []
			reg_index = 0
			for reg in self.registers:
				data.append(["F"+str(reg_index), reg.q, reg.value])
				reg_index += 1
			headers = ["Regitser", "Q", "Value"]

			print (Fore.CYAN + "Register File Content")
			print (Fore.CYAN +tabulate(data, headers=headers))
			f2.write(tabulate(data, headers=headers)+"\n")

			# f.write(tabulate(data, headers=headers))

		def printAddRes():
			data = []
			for station in self.addResStations:
				data.append([station.busy , station.id, station.vj, station.vk, station.qj, station.qk])
			headers = ["Busy", "Id", "Vj", "Vk", "Qj", "Qk" ]

			print (" ")
			print (Fore.BLUE + "Addition Reservation Station")
			print (Fore.BLUE +tabulate(data, headers=headers))
			f2.write(tabulate(data, headers=headers)+"\n")


		def printMulRes():
			data = []
			for station in self.mulResStations:
				data.append([station.busy , station.id, station.vj, station.vk, station.qj, station.qk])
			headers = ["Busy", "Id", "Vj", "Vk", "Qj", "Qk" ]

			print (" ")
			print (Fore.BLUE + "Multiplication Reservation Station")
			print (Fore.BLUE +tabulate(data, headers=headers))
			f2.write(tabulate(data, headers=headers)+"\n")



		def printLoadRes():
			data = []
			for station in self.loadResStations:
				data.append([station.busy , station.id, station.address])
			headers = ["Busy", "Id", "Address" ]

			print (" ")
			print (Fore.RED + "Load Reservation Station")
			print (Fore.RED +tabulate(data, headers=headers))
			f2.write(tabulate(data, headers=headers)+"\n")


		def printMemory():
			data = []
			mem_add = 0
			for memItem in self.memory:
				data.append(["@"+str(mem_add), memItem])
				mem_add += 1
			headers = ["Address", "Value"]

			print (Fore.CYAN + "Memory Content")
			print (Fore.CYAN +tabulate(data, headers=headers))
			f2.write(tabulate(data, headers=headers)+"\n")



		def printStoreRes():
			data = []
			for station in self.storeResStations:
				data.append([station.busy, station.v, station.q])
			headers = ["Busy", "V", "Q" ]

			print (" ")
			print (Fore.GREEN + "Store Reservation Station")
			print (Fore.GREEN +tabulate(data, headers=headers))
			f2.write(tabulate(data, headers=headers)+"\n")


		def printQ():
			data = []
			# for station in self.storeResStations:
			# 	data.append([station.busy, station.v, station.q])
			print (Fore.GREEN + "Instructions Queue")
			f.write("Instructions Queue\n")

			if(len(self.instructions[self.instructionIndex::])<=0):
				print("Empty Instructions Queue")
				f.write("Empty Instructions Queue\n")

			else:
				counter = 1
				for ins in self.instructions[self.instructionIndex::]:
					print (str(counter) + " " +ins)
					f.write(str(counter) + " " +ins+"\n")
					
					counter += 1


			# headers = ["Q", "Instructions"]

			# print (" ")
			# print (Fore.GREEN + "Store Reservation Station")
			# print (Fore.GREEN +tabulate(data, headers=headers))
			# f2.write(tabulate(data, headers=headers)+"\n")


		def printFinalTable():
			# for ins in self.decoded_instructions:
			# 	ins.print()
			data = []

			print("\n")
			print("\n")
			for insto in self.decoded_instructions:
				tmp = insto
				data.append([tmp.ins, tmp.issueTime, tmp.startTime, tmp.finishExecTime, tmp.writeBacktime])


			headers = ["Instruction", "Fetch", "Start Exec", "Finish Exec", "Write back"]

			print (tabulate(data, headers=headers))
			print("\n")
			print("\n")

		def printInfo():
			printRegisters()
			printAddRes()
			printMulRes()
			printLoadRes()
			printStoreRes()
			printQ()
			if(self.lastExecutedInstruction >= self.totalInstructionsCount):
					printFinalTable()
					printMemory()
					f.close()


		def assignValues():

			JSONadds = []
			for station in self.addResStations:
				print("Add Station toJSON:", station.toJSON())  # Debug
				JSONadds.append(station.toJSON())

			JSONmuls = []
			for station in self.mulResStations:
				print("Add Station toJSON:", station.toJSON())  # Debug
				JSONmuls.append(station.toJSON())
			
			JSONstores = []
			for station in self.storeResStations:
				print("Add Station toJSON:", station.toJSON())  # Debug
				JSONstores.append(station.toJSON())

			JSONloads = []
			for station in self.loadResStations:
				print("Add Station toJSON:", station.toJSON())  # Debug
				JSONloads.append(station.toJSON())

			status_table = []
			for insto in self.decoded_instructions:
				tmp = insto
				if(tmp.issueTime >= 0):
					status_table.append([tmp.ins, tmp.issueTime, tmp.startTime, tmp.finishExecTime, tmp.writeBacktime])
			regz = []
			for registerItem in self.registers:
				regz.append(registerItem.toJSON())


			self.response[self.responseIndex]["addStation"] = JSONadds
			self.response[self.responseIndex]["mulStation"] = JSONmuls
			self.response[self.responseIndex]["storeStation"] = JSONstores
			self.response[self.responseIndex]["loadStation"] = JSONloads
			self.response[self.responseIndex]["statusContent"] = status_table
			self.response[self.responseIndex]["regs"] = regz
			self.response[self.responseIndex]["memory"] = self.memory

			print("Updated response for addStation:", self.response[self.responseIndex]["addStation"])  # Debug



			self.response.append(
				{
				"addStation":None,
				 "mulStation":None,
				 "loadStation":None,
				 "storeStation":None,
				 "regs":None,
				 "instructionsQ":None,
				 "statusContent":None
				 }
			)
			self.responseIndex += 1

		def runCycle():
			while self.lastExecutedInstruction < self.totalInstructionsCount:

				print("        ")
				print("============== "+str(self.cycle)+" ==============") 
				print("        ")
				f.write("============== "+str(self.cycle)+" =============="+"\n")
				f2.write("============== "+str(self.cycle)+" =============="+"\n")

				
				fetch()
				execute()
				writeBack()

				assignValues()


				self.cycle += 1

				printInfo();

		#execute
		#write back
		runCycle()
		return self.response

main = OnlineMain()
# main.decode('L.D F1, 233')
# if(main.validateInastructionFormat(["ADD.D", "F1", "F1", "F-1"])):
# 	print("WORKING INSTRUCTION")
# else:
# 	print("INC FORMAT")


# data = [[1, 'Liquid', 24, 12],
# [2, 'Virtus.pro', 19, 14],
# [3, 'PSG.LGD', 15, 19],
# [4,'Team Secret', 10, 20]]
# headers=["Pos", "Team", "Win", "Lose"]
# print(pandas.DataFrame(data, headers, headers))


# for each cycle, we need to show the following
# register file DONE
# ADD Station DONE
# MUL Station DONE
# Load buffer DONE
# Store buffer DONE

#current fetching instruction
#current executing instruction
#current writing back instruction
#handle div by 0