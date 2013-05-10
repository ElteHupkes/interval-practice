#!/usr/bin/python
"""
Simple program to practice semitone intervals. Each
question consists of a note and a number of semitones
up or down from that note, and should be answered
with the correct note at that interval.
"""
import random
from notes import notes
l = len(notes)

# The maximum distance value asked
maxDist = 11

print "Type 'q' to quit, or '?' to get the answer and continue."

quit = False
while not quit:
	base = random.randint(0, l - 1)
	dist = random.randint(-maxDist, maxDist)
	if dist == 0:
		continue

	baseNote = notes[base]
	answer = notes[(base + dist) % l]
	random.shuffle(answer)

	sign = "+" if dist > 0 else "-"
	question = "%s %s %s = " % (random.choice(baseNote), sign, abs(dist))
	correct = False

	while not correct:
		guess = raw_input(question).strip().capitalize()

		if guess[-1] == "s":
			# Allow "s" for sharp
			guess[-1] = "#"

		if guess == "Q":
			quit = True
			break

		if guess == "?":
			print "Should have been %s" % answer
			break
		
		if guess in answer:
			print "Correct!"
			correct = True
		else:
			print "Try again.."
