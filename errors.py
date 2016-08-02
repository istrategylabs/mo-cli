
class MalformedMoYaml(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)


class UnknownEnvironment(Exception):
	def __init__(self, value):
		self.value = value

	def __str__(self):
		return repr(self.value)
