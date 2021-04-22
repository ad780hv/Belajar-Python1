class komputer:
	'perangkat pada komputer'
	jmlKom = 0

	def __init__(self,prosesor,memory,os,keyboard,mouse):
		self.__prosesor = 'Intel Core 17-6700K'
		self.__memory = '16GB DDR4'
		self.os = 'Windows 10 Pro'
		self.keyboard = 'Razer'
		self.mouse ='Logitech'

	def tampilData(self):
		print('Prosesor:',self.__prosesor)
		print('Memory:',self.__memory)
		print('OS:',self.os)
		print('Keyboard:',self.keyboard)
		print('Mouse:',self.mouse)

pc = komputer("","","","","")
a = input('prosesor: ')
s = input('memory: ')
d = input('os: ')
f = input('keyboard: ')
g = input('mouse: ')

print('prosesor:',getattr(pc,'prosesor',a))
print('memory:',getattr(pc,'memory',s))
print(getattr(pc,'os',d))
print(getattr(pc,'keyboard',f))
print(getattr(pc,'mouse',g))

setattr(pc,'prosesor',a)
setattr(pc,'memory',s)
setattr(pc,'os',d)
setattr(pc,'keyboard',f)
setattr(pc,'mouse',g)

#pc = Computer()
pc.tampilData()