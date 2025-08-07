from experta import *
class StudentFacts(Fact):
	pass
class CareerExpertSystem(KnowledgeEngine):
	@Rule(StudentFacts(likes='maths'), StudentFacts(likes='physics'))
	def mechanical(self):
		print("Suggested Career Path: Mechanical Engineering")
	@Rule(StudentFacts(likes='programming'), StudentFacts(likes='maths'))
	def computer(self):
		print("Suggested Career Path: Computer Engineering")
	@Rule(StudentFacts(likes='biology'), StudentFacts(likes='chemistry'))
	def biotech(self):
		print("Suggested Career Path: Biotechnology")
	@Rule(StudentFacts(likes='circuits'), StudentFacts(likes='maths'))
	def electronics(self):
		print("Suggested Career Path: Electronics Engineering")
def main():
	engine = CareerExpertSystem()
	engine.reset()
	print("Welcome to the Career Path Expert System!")
	interests = input("Enter your interests separated by commas (e.g., Maths, Physics, Programming): ").lower().split(',')
	#interests=interest
	for interest in interests:
		engine.declare(StudentFacts(likes=interest.strip()))
	engine.run()
if __name__ == "__main__":
	main()
