from logic import evaluate_sentence
import unittest

class TestEasy(unittest.TestCase):
	def test_easy(self):
		# Represents the sentence "Every student has a pencil and a laptop"
		# i.e. ∀x hasPencil(x) ∧ hasLaptop(x)
		sentence1 = {
			"quantifiers": ["∀", "x"],
			"predicates": {
				"P": ["hasPencil", "x"],
				"Q": ["hasLaptop", "x"]
			},
			"form": "P∧Q",
			"difficulty": 0
		}
		# Represents four students, all of whom have both a pencil and a laptop
		scenario1 = [
			{
				"hasPencil": True,
				"hasLaptop": True,
				"hasCalculator": False
			},
			{
				"hasPencil": True,
				"hasLaptop": True,
				"hasCalculator": True
			},
			{
				"hasPencil": True,
				"hasLaptop": True,
				"hasCalculator": False
			},
			{
				"hasPencil": True,
				"hasLaptop": True,
				"hasCalculator": True
			}
		]
		self.assertEqual(evaluate_sentence(sentence1, scenario1), True)

		# Update scenario1 to have a student without a laptop
		scenario1[0]["hasLaptop"] = False
		self.assertEqual(evaluate_sentence(sentence1, scenario1), False)

		# Update sentence to use "∃" instead of "∀"
		sentence1["quantifiers"][0] = "∃"
		self.assertEqual(evaluate_sentence(sentence1, scenario1), True)

		# Update scenario1 to have no students with a laptop
		for student in scenario1:
			student["hasLaptop"] = False
		self.assertEqual(evaluate_sentence(sentence1, scenario1), False)

class TestMedium(unittest.TestCase):
	def test_medium(self):
		# Represents the sentence "Everyone likes rugby and football and dislikes golf"
		# i.e. ∀x likes(x, rugby) ∧ likes(x, football) ∧ dislikes(x, golf)
		sentence1 = {
			"quantifiers": ["∀", "x"],
			"predicates": {
				"P": ["likes", "x", "rugby"],
				"Q": ["likes", "x", "football"],
				"R": ["dislikes", "x", "golf"]
			},
			"form": "P∧Q∧R",
			"difficulty": 1
		}
		# Represents four people, all of whom like rugby and football and dislike golf
		scenario1 = [
			{
				"likes": ["rugby", "football"],
				"dislikes": ["golf"]
			},
			{
				"likes": ["athletics", "football", "rugby"],
				"dislikes": ["basketball", "golf"]
			},
			{
				"likes": ["football", "tennis", "rugby"],
				"dislikes": ["hockey", "golf", "athletics"]
			},
			{
				"likes": ["rugby", "baseball", "football"],
				"dislikes": ["golf", "tennis"]
			}
		]
		self.assertEqual(evaluate_sentence(sentence1, scenario1), True)
		
		# Update scenario1 to have a person who does not like rugby
		scenario1[0]["likes"].remove("rugby")
		self.assertEqual(evaluate_sentence(sentence1, scenario1), False)
		
		# Update sentence to use "∃" instead of "∀"
		sentence1["quantifiers"][0] = "∃"
		self.assertEqual(evaluate_sentence(sentence1, scenario1), True)

		# Update scenario1 to have no people who like football
		for person in scenario1:
			person["likes"].remove("football")
		self.assertEqual(evaluate_sentence(sentence1, scenario1), False)

		# Represents the sentence "There exists someone who, if they like tennis, they dislike football"
		# i.e. ∃x likes(x, tennis) → dislikes(x, football)
		sentence2 = {
			
			"quantifiers": ["∃", "x"],
			"predicates": {
				"P": ["likes", "x", "tennis"],
				"Q": ["dislikes", "x", "football"]
			},
			"form": "P→Q",
			"difficulty": 1
		}
		
		scenario2 = [
			{
				"likes": ["tennis", "football"],
				"dislikes": ["rugby"]
			},
			{
				"likes": ["athletics", "football", "rugby"],
				"dislikes": ["basketball", "golf"]
			},
			{
				"likes": ["football", "tennis", "rugby"],
				"dislikes": ["hockey", "golf", "athletics"]
			},
			{
				"likes": ["rugby", "baseball", "football"],
				"dislikes": ["golf", "tennis"]
			}
		]

		self.assertEqual(evaluate_sentence(sentence2, scenario2), True)

		# Use "∀" instead of "∃"
		sentence2["quantifiers"][0] = "∀"
		self.assertEqual(evaluate_sentence(sentence2, scenario2), False)
	
class TestHard(unittest.TestCase):
	def test_hard(self):
		sentence1 = {
			"quantifiers": ["∀", "x", "∃", "y"],
			"predicates": {
				"P": ["owns", "x", "y"],
				"Q": ["large", "y"]
			},
			"form": "P∧Q",
			"difficulty": 2
		}
		scenario1 = [
			{
				"pets": [
					{
						"type": "dog",
						"size": "large"
					},
					{
						"type": "cat",
						"size": "small"
					}
				]
			},
			{
				"pets": [
					{
						"type": "goldfish",
						"size": "small"
					}
				]
			},
			{
				"pets": [
					{
						"type": "hamster",
						"size": "large"
					}
				]
			}
		]
		self.assertEqual(evaluate_sentence(sentence1, scenario1), False)

		# Update scenario1 to have the second person owning a large pet
		scenario1[1]["pets"][0]["size"] = "large"
		self.assertEqual(evaluate_sentence(sentence1, scenario1), True)

		sentence2 = {
			"quantifiers": ["∀", "x", "∃", "y"],
			"predicates": {
				"P": ["owns", "x", "y"],
				"Q": ["small", "y"],
				"R": ["cat", "y"]
			},
			"form": "P→(Q∧R)",
			"difficulty": 2
		}
		scenario2 = [
			{
				"pets": [
					{
						"type": "dog",
						"size": "large"
					},
					{
						"type": "cat",
						"size": "small"
					}
				]
			},
			{
				"pets": [
					{
						"type": "goldfish",
						"size": "small"
					}
				]
			},
			{
				"pets": [
					{
						"type": "bird",
						"size": "large"
					},
					{
						"type": "cat",
						"size": "small"
					}
				]
			}
		]

		self.assertEqual(evaluate_sentence(sentence2, scenario2), False)

		# Update scenario2 to have the second person owning a small cat
		scenario2[1]["pets"][0]["type"] = "cat"
		self.assertEqual(evaluate_sentence(sentence2, scenario2), True)

unittest.main()
