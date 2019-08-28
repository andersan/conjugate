from pattern.fr import conjugate
from pattern.fr import verbs
import random

some_verbs = list(verbs.infinitives.keys())
possible_persons = [1, 2, 3]
possible_plurality = ["sg", "pl"]

def get_verb():
	verb = random.choice(some_verbs)
	pp = str(random.choice(possible_persons)) + random.choice(possible_plurality)
	return conjugate(verb, pp), verb, pp


if __name__== "__main__":
	while True:
		result, verb, pp = get_verb()
		attempt = input("Conjugate " + verb + " in " + pp + ": \n")

		if (attempt == result):
			print("Correct")
		else:
			print("Incorrect - should be " + result)
