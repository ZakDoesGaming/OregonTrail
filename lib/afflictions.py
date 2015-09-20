class Afflictions():
	def __init__(self, name, chanceToInfect, infectivity, primeSeason, healthChange, recoveryTime):
		self.name = name
		self.chanceToInfect = chanceToInfect
		self.infectivity = infectivity
		self.primeSeason = primeSeason
		self.healthChange = healthChange
		self.recoveryTime = recoveryTime
		
	def __eq__(self, other):
		if (isinstance(other, self.__class__)):
			return (self.name == other.name)
		else:
			return False
			
	def __ne__(self, other):
		return (not __eq__(self, other))