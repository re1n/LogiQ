import random

def generatePets(num):
	pets = ["NULL", "Dog", "Cat"]
	people = ["Man", "Woman"]
	picked_pets_and_people = []
	for i in range(0, num):
		chosen_pet = random.choice(pets)
		chosen_person = random.choice(people)
		picked_pets_and_people.append((chosen_person, chosen_pet))
	return picked_pets_and_people

def sentencesPets(picked_pets_and_people, pets, people):
	def everyPerson(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] != pet:
					if not invert:
						sentence = f"∀x {person}(x) → Has(x, {pet})"
						return (sentence, False)
					else:
						sentence = f"¬∀x {person}(x) → Has(x, {pet})"
						return (sentence, True)
		if not invert:
			sentence = f"∀x {person}(x) → Has(x, {pet})"
			return (sentence, True)
		else:
			sentence = f"¬∀x {person}(x) → Has(x, {pet})"
			return (sentence, False)
	
	def somePerson(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] == pet:
					if not invert:
						sentence = f"∃x {person}(x) → Has(x, {pet})"
						return (sentence, True)
					else:
						sentence = f"¬∃x {person}(x) → Has(x, {pet})"
						return (sentence, False)
		if not invert:
			sentence = f"∃x {person}(x) → Has(x, {pet})"
			return (sentence, False)
		else:
			sentence = f"¬∃x {person}(x) → Has(x, {pet})"
			return (sentence, True)
	
	def everyPet(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] != person and pair[1] == pet:
					if not invert:
						sentence = f"∀x {pet}(x) → Owner({person}, x)"
						return (sentence, False)
					else:
						sentence = f"¬∀x {pet}(x) → Owner({person}, x)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x {pet}(x) → Owner({person}, x)"
			return (sentence, True)
		else:
			sentence = f"¬∀x {pet}(x) → Owner({person}, x)"
			return (sentence, False)
	
	def somePet(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] == pet:
					if not invert:
						sentence = f"∃x {pet}(x) → Owner({person}, x)"
						return (sentence, True)
					else:
						sentence = f"¬∃x {pet}(x) → Owner({person}, x)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x {pet}(x) → Owner({person}, x)"
			return (sentence, False)
		else:
			sentence = f"¬∃x {pet}(x) → Owner({person}, x)"
			return (sentence, True)

	func_list = [everyPerson, somePerson, everyPet, somePet]
	sentences = []
	while len(sentences) < 4:
		sentence = random.choice(func_list)(invert = random.choice([True, False]))
		if sentence not in sentences:
			sentences.append(sentence)
	
	print(sentences)
	return sentences