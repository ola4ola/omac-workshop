class Member():
	"""editing the member information"""
	def __init__(self, name, age):
		self.member_name = name
		self.member_age = age
	def __str__(self):
		return self.member_name + str(self.member_age)

class Post():
	def __init__(self, title, body):
		self.post_title = title
		self.post_body = body
	def __str__(self):
		return (self.post_title + ',' + self.post_body)
