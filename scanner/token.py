class token:
	def __init__(self, name, value=""):
		self.name = name
		self.value = value
		self.dataType = None
		self.scope = None

	def __repr__(self):
		myRepr = ""
		myRepr += "(name=" + str(self.name)
		myRepr += ", value=" + str(self.value)
		myRepr += ")"
		return myRepr
