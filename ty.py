class computer:


		def __init__(self,prosesor,memory,os,keyboard,mouse):
			self.__prosesor = 'intel Core 6700k'
			self.__memory = '16GB DDR4'
			self.os = 'Windows 10 prosesor'
			self.keyboard = 'Razer'
			self.mouse = 'Logitech'

		def tampilData(self):
			print('Prosesor:',self.__prosesor)
			print('Memory:',self.__memory)
			print('Os:',self.os)
			print('Keyboard:',self.keyboard)
			print('Mouse:',self.mouse)

		def __ubahmemory(self,ram):
			self.__memory = ram

		def __ubahProsesor(self,pro):
			self.__prosesor = pro

pc = computer('','','','','')

pc._computer__ubahProsesor(input("Prosesor: "))
pc._computer__ubahmemory(input("Memory: "))
o = input("os: ")
keb = input("keyboard: ")
mos = input("Mouse: ")

setattr(pc,'Prosesor',pc._computer__ubahProsesor)
setattr(pc,'Memory',pc._computer__ubahmemory)
setattr(pc,'Os',o)
setattr(pc,'Keyboard',keb)
setattr(pc,'Mouse',mos)

print()
pc.tampilData()