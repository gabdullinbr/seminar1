class MyClass:
	def __init__(self, s=""):
		self.s = s
	def read(self):
		print(self.s)
	def change(self,new_s):
		self.s = new_s
