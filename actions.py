class Actions(object):

	def __init__(self, l = []):
		self.actions = l

	def add(verb):
		self.actions.append(verb)

	def total():
		return len(self.actions)

	def __str__(self):
		return self.actions.__str__()

	def __repr__(self):
		return self.actions


def main():
	test = Actions(["tie","punch","look"])
	print(test)

if __name__ == "__main__":
	main()

