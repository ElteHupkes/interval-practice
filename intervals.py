#!/usr/bin/python
"""
Simple program to practice the semitone distance
corresponding to interval names.
"""
import random

intervals = [
	["unison"],
	["flat 2nd"],
	["2nd"],
	['minor 3rd'],
	['major 3rd'],
	['perfect 4th'],
	['flat 5th', 'diminished 5th', 'augmented 4th'],
	['perfect 5th'],
	['minor 6th', 'sharp 5th', 'augmented 5th'],
	['major 6th'],
	['minor 7th', 'flat 7th'],
	['major 7th'],
	['octave']
]

l = len(intervals)

quit = False
while not quit:
	dist = random.randint(0, l-1)

	question = "%s = " % " / ".join(intervals[dist])
	correct = False

	while not correct:
		answer = raw_input(question).strip()
		if answer.lower() == "q":
			quit = True
			break

		if answer == '?':
			print "Answer is %s" % dist
			break

		if int(answer) == dist:
			correct = True
			print "Correct!"
		else:
			print "Try again..."
