import string
class ceaser:
	def __init__(self, plain):
		self.plain = plain
	def shift(self,n):
		al = "-"+string.ascii_lowercase+string.ascii_lowercase
		cal = "-"+string.ascii_uppercase+string.ascii_uppercase
		ans = ""
		for i in range(0,len(self.plain)):
			if self.plain[i] in al:
				ans = ans + al[al.index(self.plain[i])+n]
			elif self.plain[i] in cal:
				ans = ans + cal[cal.index(self.plain[i])+n]
			else:
				ans += self.plain[i]
		print(ans)
	def decrypt(self, n):
		al = "-"+string.ascii_lowercase+string.ascii_lowercase
		cal = "-"+string.ascii_uppercase+string.ascii_uppercase
		ans = ""
		for i in range(0,len(self.plain)):
			if self.plain[i] in al:
				ans = ans + al[al.index(self.plain[i])-n]
			elif self.plain[i] in cal:
				ans = ans + cal[cal.index(self.plain[i])-n]
			else:
				ans += self.plain[i]
		print(ans)
# K = ceaser("Hello,_World!")
# K.shift(4)
string = "Tkmu Pvyboi sc."
obj = ceaser(string)
obj.decrypt(10)