#!/usr/bin/python
"""
Simple program to practice associating the
notes A to Ab with the numbers 0 to 11.
Simply run and start answering.
"""
from notes import notes
import random

l = len(notes)
quit = False

while not quit:
	choice = random.randint(0, l-1)
	answer = notes[choice]

	swap = random.randint(0, 1) == 1
	
	if swap:
		question = "%s = " % random.choice(answer)
	else:
		question = "%s = " % choice

	correct = False

	while not correct:
		guess = raw_input(question).strip()

		if guess == "Q" or guess == "q":
			quit = True
			break

		if swap:
			guess = int(guess)
			correct = guess == choice
		else:
			correct = guess.capitalize() in answer

		if correct:
			print "Correct!"
		else:
			print "Try again.."
		
