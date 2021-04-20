class Computer:

	def __init__(self,prosesor,memory,os,keyboard,mouse):
		self.__prosesor = 'intel Core 6700k'
		self.__memory = '16GB DDR4'
		self.os = 'Windows 10 prosesor'
		self.keyboard = 'Razer'
		self.mouse = 'Logitech'

	def tampilData(self):
		print("prosesor:",self.__prosesor)
		print("memory:",self.__memory)
		print("os:",self.os)
		print("keyboard:",self.keyboard)
		print("mouse:",self.mouse)

kom1 = Computer('','','','','')

pros = input("Prosesor: ")
mem = input("memory: ")
o = input("os: ")
keb = input("keyboard: ")
mos = input("mouse: ")

setattr(kom1,'prosesor',pros)
setattr(kom1,'memory',mem)
setattr(kom1,'os',o)
setattr(kom1,'keyboard',keb)
setattr(kom1,'mouse',mos)

print()
kom1.tampilData()
