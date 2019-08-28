from pattern.fr import conjugate
from pattern.fr import verbs
import random

some_verbs = list(verbs.infinitives.keys())
print(some_verbs)
possible_persons = [1, 2, 3]
possible_plurality = ["sg", "pl"]
verb = random.choice(some_verbs)
pp = str(random.choice(possible_persons)) + random.choice(possible_plurality)
result = conjugate(verb, pp)
print("\n")
attempt = input("Conjugate " + verb + " in " + pp + ": \n")

if (attempt == result):
	print("Correct")
else:
	print("Incorrect - should be " + result) 
