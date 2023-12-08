#!/usr/bin/python3
def fizzbuzz():
	for i in range(101):
		if i % 3 & i % 5:
			print("FizzBuzz")
		elif i % 3 & i !% 5:
			print("Fizz")
		elif i % 5 & i !% 3:
			print("Buzz")