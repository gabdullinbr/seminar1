from myclass import MyClass
class MyClass2(MyClass):
	def __init__(self, n=""):
		self.n = n
		super().__init__(self)
	def read(self):
		print(self.n)
		print(self.s)