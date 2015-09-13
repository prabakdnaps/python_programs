
import random
import time

print "Test for your math skills: \n "
user_time = int(raw_input("Enter the total test time (mins): "))
user_time=user_time*60
user_score=0;
test=0;
denom=int(raw_input("\n Enter Range for Denominator: "))
nu=int(raw_input("\n Enter Range for Numerator: "))

while time.clock()<user_time:
	test = test+1
	print "Test Number: ", test
	print "Current Time (mins): ",time.clock()/60
	random_de = int(random.random()*denom)+1
	random_nu = int(random.random()*nu)+1
	print random_de, '/', random_nu
	ratio = float(random_de)/random_nu
	user_answer = float(raw_input("\n Enter the result: "))
	if ratio/user_answer>1.1:
		print "user lost"
	elif ratio/user_answer<0.9:
		print "user lost"
	else:
		print "user won"
		user_score = user_score+1

print "User Final Score: ", user_score
print "Total Number of tests: ", test
print "Success Percentage: ", float(user_score)/test*100



