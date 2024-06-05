class Room:

	def __init__(self, description):
		self.__description = description
		self.__northExit = None
		self.__southExit = None
		self.__eastExit = None
		self.__westExit = None
		self.__upExit = None
		self.__downExit = None
		

	def setExits(self, north, east, south, west, up, down):
		if north != None:
			self.__northExit = north
		if east != None:
			self.__eastExit = east
		if south != None:
			self.__southExit = south
		if west != None:
			self.__westExit = west
		if up != None:
			self.__upExit = up
		if down != None:
			self.__downExit = down
	
	def getDescription(self):
		return self.__description
	
	def getExit(self, direction):
		if direction == 'north':
			return self.__northExit
		if direction == 'east':
			return self.__eastExit
		if direction == 'south':
			return self.__southExit
		if direction == 'west':
			return self.__westExit
		if direction == 'up':
			return self.__upExit
		if direction == 'down':
			return self.__downExit