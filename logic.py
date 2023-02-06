import random

def generatePets(num):
	pets = ["NULL", "Dog", "Cat"]
	people = ["Man", "Woman"]
	colours = ["NULL", "Red", "Blue", "Green"]
	picked_pets_and_people = []
	for i in range(0, num):
		chosen_pet = random.choice(pets)
		chosen_person = random.choice(people)
		chosen_colour = random.choice(colours)
		picked_pets_and_people.append((chosen_person, chosen_pet, chosen_colour))
	return picked_pets_and_people

def sentencesPets(picked_pets_and_people, pets, people, colours):
	def everyone(invert = False):
		for pair in picked_pets_and_people:
			if pair[1] == "NULL":
				if not invert:
					sentence = f"∀x∃y HasPet(x, y)"
					return (sentence, False)
				else:
					sentence = f"¬∀x∃y HasPet(x, y)"
					return (sentence, True)
		if not invert:
			sentence = f"∀x∃y HasPet(x, y)"
			return (sentence, True)
		else:
			sentence = f"¬∀x∃y HasPet(x, y)"
			return (sentence, False)

	def everyonePet(invert = False):
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[1] != pet:
					if not invert:
						sentence = f"∀x∃y HasPet(x, y) ∧ {pet}(y)"
						return (sentence, False)
					else:
						sentence = f"¬∀x∃y HasPet(x, y) ∧ {pet}(y)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x∃y HasPet(x, y) ∧ {pet}(y)"
			return (sentence, True)
		else:
			sentence = f"∀x∃y HasPet(x, y) ∧ {pet}(y)"
			return (sentence, False)

	def everyoneColour(invert = False):
		colour = random.choice(colours)
		while colour == "NULL":
			colour = random.choice(colours)
		for pair in picked_pets_and_people:
				if pair[2] != colour:
					if not invert:
						sentence = f"∀x∃y HasPet(x, y) ∧ {colour}(y)"
						return (sentence, False)
					else:
						sentence = f"¬∀x∃y HasPet(x, y) ∧ {colour}(y)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x∃y HasPet(x, y) ∧ {colour}(y)"
			return (sentence, True)
		else:
			sentence = f"¬∀x∃y HasPet(x, y) ∧ {colour}(y)"
			return (sentence, False)

	def everyPersonPet(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] != pet:
					if not invert:
						sentence = f"∀x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
						return (sentence, False)
					else:
						sentence = f"¬∀x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
			return (sentence, True)
		else:
			sentence = f"¬∀x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
			return (sentence, False)
		
	def everyPetPerson(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] != person and pair[1] == pet:
					if not invert:
						sentence = f"∀x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
						return (sentence, False)
					else:
						sentence = f"¬∀x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
			return (sentence, True)
		else:
			sentence = f"¬∀x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
			return (sentence, False)
	
	def everyPersonColour(invert = False):
		person = random.choice(people)
		colour = random.choice(colours)
		while colour == "NULL":
			colour = random.choice(colours)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[2] != colour:
					if not invert:
						sentence = f"∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
						return (sentence, False)
					else:
						sentence = f"¬∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
			return (sentence, True)
		else:
			sentence = f"¬∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
			return (sentence, False)
	
	def everyPersonPetColour(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		colour = random.choice(colours)
		while colour == "NULL":
			colour = random.choice(colours)
		for pair in picked_pets_and_people:
				if pair[0] == person and (pair[1] != pet or pair[2] != colour):
					if not invert:
						sentence = f"∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
						return (sentence, False)
					else:
						sentence = f"¬∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
						return (sentence, True)
		if not invert:
			sentence = f"∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
			return (sentence, True)
		else:
			sentence = f"¬∀x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
			return (sentence, False)
		
	def someone(invert = False):
		for pair in picked_pets_and_people:
			if pair[1] != "NULL":
				if not invert:
					sentence = f"∃x∃y HasPet(x, y)"
					return (sentence, True)
				else:
					sentence = f"¬∃x∃y HasPet(x, y)"
					return (sentence, False)
		if not invert:
			sentence = f"∃x∃y HasPet(x, y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y HasPet(x, y)"
			return (sentence, True)
	
	def someonePet(invert = False):
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[1] == pet:
					if not invert:
						sentence = f"∃x∃y {pet}(y) ∧ HasPet(x, y)"
						return (sentence, True)
					else:
						sentence = f"¬∃x∃y {pet}(y) ∧ HasPet(x, y)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x∃y {pet}(y) ∧ HasPet(x, y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y {pet}(y) ∧ HasPet(x, y)"
			return (sentence, True)

	def someoneColour(invert = False):
		colour = random.choice(colours)
		while colour == "NULL":
			colour = random.choice(colours)
		for pair in picked_pets_and_people:
				if pair[2] == colour:
					if not invert:
						sentence = f"∃x∃y {colour}(y) ∧ HasPet(x, y)"
						return (sentence, True)
					else:
						sentence = f"¬∃x∃y {colour}(y) ∧ HasPet(x, y)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x∃y {colour}(y) ∧ HasPet(x, y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y {colour}(y) ∧ HasPet(x, y)"
			return (sentence, True)
		
	def somePersonPetColour(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		colour = random.choice(colours)
		while colour == "NULL":
			colour = random.choice(colours)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] == pet and pair[2] == colour:
					if not invert:
						sentence = f"∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
						return (sentence, True)
					else:
						sentence = f"¬∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y) ∧ {pet}(y)"
			return (sentence, True)
	
	def somePersonPet(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] == pet:
					if not invert:
						sentence = f"∃x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
						return (sentence, True)
					else:
						sentence = f"¬∃x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y {person}(x) → HasPet(x, y) ∧ {pet}(y)"
			return (sentence, True)
		
	def somePersonColour(invert = False):
		person = random.choice(people)
		colour = random.choice(colours)
		while colour == "NULL":
			colour = random.choice(colours)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[2] == colour:
					if not invert:
						sentence = f"∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
						return (sentence, True)
					else:
						sentence = f"¬∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y {person}(x) → HasPet(x, y) ∧ {colour}(y)"
			return (sentence, True)
	
	def somePetPerson(invert = False):
		person = random.choice(people)
		pet = random.choice(pets)
		for pair in picked_pets_and_people:
				if pair[0] == person and pair[1] == pet:
					if not invert:
						sentence = f"∃x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
						return (sentence, True)
					else:
						sentence = f"¬∃x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
						return (sentence, False)
		if not invert:
			sentence = f"∃x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
			return (sentence, False)
		else:
			sentence = f"¬∃x∃y {pet}(x) → HasOwner(x, y) ∧ {person}(y)"
			return (sentence, True)
		
	def onlyOne(invert = False):
		with_pets = without_pets = picked_pets_and_people.copy()
		for pair in with_pets:
			if pair[1] == "NULL":
				with_pets.remove(pair)
		for pair in without_pets:
			if pair[1] != "NULL":
				without_pets.remove(pair)
		if len(with_pets) == 1:
			# Exactly one person has a pet
			if not invert:
				sentence = f"∃x∃y HasPet(x, y) ∧ ∀w∃z HasPet(w, z) → x==w"
				return (sentence, True)
		else:
			if not invert:
				sentence = f"∃x∃y HasPet(x, y) ∧ ∀w∃z HasPet(w, z) → x==w"
				return (sentence, False)
		if len(without_pets) == 1:
			# Exactly one person does not have a pet
			if invert:
				sentence = f"∃x∃y ¬HasPet(x, y) ∧ ∀w∃z (¬x==w) → HasPet(w, z)"
				return (sentence, True)
		else:
			if invert:
				sentence = f"∃x∃y ¬HasPet(x, y) ∧ ∀w∃z (¬x==w) → HasPet(w, z)"
				return (sentence, False)

	func_list = [everyone, everyoneColour, everyonePet, everyPersonColour, everyPersonPet,
	    everyPetPerson, everyPersonPetColour, someone, someoneColour, someonePet, somePersonPet,
		somePersonColour, somePetPerson, somePersonPetColour, onlyOne]
	sentences = []
	while len(sentences) < 4:
		sentence = random.choice(func_list)(invert = random.choice([True, False]))
		if sentence not in sentences:
			sentences.append(sentence)
	print(sentences)
	print(picked_pets_and_people)
	return sentences

# Students in a class scenario
def generate_classroom():
	def check_predicate(predicate, quantifier, students):
		if quantifier == "∀":
			for student in students:
				if not student[predicate]:
					return False
			return True
		elif quantifier == "∃":
			for student in students:
				if student[predicate]:
					return True
			return False
	
	def create_abstract_sentence(sentence_arr, students):
		truth_values = []
		quantifier = sentence_arr[0]
		abstract_sentence = []
		char = "P"
		for i in range(1, len(sentence_arr)):
			if len(sentence_arr[i]) == 1:
				abstract_sentence.append(sentence_arr[i])
			else:
				abstract_sentence.append(char)
				truth_values.append({char : check_predicate(sentence_arr[i], quantifier, students)})
				char = chr(ord(char) + 1)
	
	num_students = random.randint(4, 7)
	students = []
	for i in range(num_students):
		has_laptop = False
		has_calculator = False
		has_pencil = False
		if random.randint(0, 1) == 0:
			has_laptop = True
		if random.randint(0, 1) == 0:
			has_calculator = True
		if random.randint(0, 1) == 0:
			has_pencil = True
		students.append({"name": f"Student{i+1}", "hasLaptop": has_laptop, "hasCalculator": has_calculator, "hasPencil": has_pencil})
	predicates = ["hasLaptop", "hasCalculator", "hasPencil"]
	connectives = ["∧", "∨"]
	quantifiers = ["∃", "∀"]
	sentences = []
	while len(sentences) < 4:
		sentence_arr = []
		quantifier = random.choice(quantifiers)
		sentence_arr.append(quantifier)
		if random.randint(0, 1) == 0:
			predicate1 = random.choice(predicates)
			sentence_arr.append(predicate1)
			predicate = f"{predicate1}(x)"
			
		else:
			predicate1 = random.choice(predicates)
			predicate2 = random.choice(predicates)
			while predicate1 == predicate2:
				predicate2 = random.choice(predicates)
			connective = random.choice(connectives)
			predicate = f"{predicate1}(x) {connective} {predicate2}(x)"
			sentence_arr.append(predicate1)
			sentence_arr.append(connective)
			sentence_arr.append(predicate2)
		sentence = f"{quantifier}x {predicate}"
		if sentence not in sentences:
			sentences.append(sentence)
			create_abstract_sentence(sentence_arr)
	return students, sentences
		

# General function to check if a sentence is true or false
def check_sentence(sentence, truth_values):
	pass 
	