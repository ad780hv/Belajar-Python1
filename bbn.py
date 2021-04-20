class Computer:

	def __init__(self):
		self.__prosesor = 'Intel Core i7-6700K'
		self.__memory = '16GB DDR4'
		self.os = 'Windows 10 Pro'
		self.keyboard = 'Razer'
		self.mouse = 'Logitech'

	def tampilData(self):
		print('Prosesor:',self.__prosesor)
		print('Memory:',self.__memory)
		print('OS:',self.os)
		print('Keyboard:',self.keyboard)
		print('Mouse:',self.mouse)

pc = Computer()
pc.tampilData()