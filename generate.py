from random import randint, choice

from logic import evaluate_sentence


# Easy difficulty
def generate_classroom():
    # Randomly generate between 3 and 7 students
    # and randomly assign them laptops, calculators, and pencils
    num_students = randint(3, 7)
    students = []
    for i in range(num_students):
        has_laptop = False
        has_calculator = False
        has_pencil = False
        if randint(0, 9) > 3:
            has_laptop = True
        if randint(0, 9) > 3:
            has_calculator = True
        if randint(0, 9) > 3:
            has_pencil = True
        students.append({"name": f"Student{i+1}", "hasLaptop": has_laptop,
                         "hasCalculator": has_calculator,
                         "hasPencil": has_pencil})
    predicates = ["hasLaptop", "hasCalculator", "hasPencil"]
    connectives = ["∧", "∨"]
    quantifiers = ["∃", "∀"]
    sentences = []
    # Generates 4 sentences of easy difficulty
    # each should fall under one of the following two rules:
    # 1. One quantifier, one predicate, no implications and no connectives
    # (Rule 1 in Table 2.1)
    # 2. One quantifier, two predicates, no implications and one connective
    # (Rule 2 in Table 2.1)
    while len(sentences) < 4:
        char = "P"
        sentence_dict = {}
        quantifier = choice(quantifiers)
        sentence_dict["quantifiers"] = [quantifier, "x"]
        # Rule 1
        if randint(0, 1) == 0:
            predicate1 = choice(predicates)
            sentence_dict["predicates"] = {char: [predicate1, "x"]}
            predicate = f"{predicate1}(x)"
            sentence_dict["form"] = char
        # Rule 2
        else:
            predicate1 = choice(predicates)
            predicate2 = choice(predicates)
            while predicate1 == predicate2:
                predicate2 = choice(predicates)
            connective = choice(connectives)
            predicate = f"{predicate1}(x) {connective} {predicate2}(x)"
            sentence_dict["predicates"] = {char: [predicate1, "x"],
                                           chr(ord(char)+1): [predicate2, "x"]}
            sentence_dict["form"] = f"{char}{connective}{chr(ord(char)+1)}"
        sentence = f"{quantifier}x {predicate}"
        if sentence not in [x[0] for x in sentences]:
            sentence_dict["difficulty"] = 0
            sentence_true = evaluate_sentence(sentence_dict, students)
            sentences.append((sentence, sentence_true))
    return sentences, students


# Medium
def generate_favourite_sports():
    # Randomly generate between 3 and 6 people
    # and randomly assign them likes and dislikes
    num_people = randint(3, 6)
    people = []
    sports = ["football", "basketball", "tennis", "rugby",
              "cricket", "golf", "hockey", "athletics"]
    for i in range(num_people):
        pick_sports = sports.copy()
        if randint(0, 9) > 0:
            num_likes = randint(1, 3)
        else:
            num_likes = 0
        if randint(0, 9) > 0:
            num_dislikes = randint(1, 3)
        else:
            num_dislikes = 0
        likes = []
        dislikes = []
        # Avoid duplicates in likes and dislikes
        # by removing the sport from the list of possible sports
        for j in range(num_likes):
            sport = choice(pick_sports)
            likes.append(sport)
            pick_sports.remove(sport)
        for j in range(num_dislikes):
            sport = choice(pick_sports)
            dislikes.append(sport)
            pick_sports.remove(sport)
        people.append({"name": f"Person{i+1}",
                       "likes": likes, "dislikes": dislikes})
    predicates = ["likes", "dislikes"]
    connectives = ["∧", "∨", "→"]
    quantifiers = ["∃", "∀"]
    sentences = []
    # Generates 4 sentences of medium difficulty, each sentence
    # should fall under one of the following 3 rules:
    # 1. a sentence with 1 quantifier, 2 predicates, 1 connective and
    # 1 implication (Rule 3 in Table 2.1)
    # 2. a sentence with 1 quantifier, 3 predicates, 2 connectives and
    # 0 or 1 implication (Rule 4 in Table 2.1)
    # 3. a sentence with 2 quantifiers and 1 predicate (Rule 5 in Table 2.1)
    while len(sentences) < 4:
        pick_sports = sports.copy()
        char = "P"
        sentence_dict = {}
        rule = randint(0, 2)
        # Rule 3
        if rule == 0:
            quantifier = choice(quantifiers)
            sentence_dict["quantifiers"] = [quantifier, "x"]
            predicate1 = choice(predicates)
            sport1 = choice(pick_sports)
            pick_sports.remove(sport1)
            predicate2 = choice(predicates)
            sport2 = choice(pick_sports)
            pick_sports.remove(sport2)
            connective = "→"
            sentence_dict["predicates"] = {char: [predicate1, "x", sport1],
                                           chr(ord(char)+1): [
                                               predicate2, "x", sport2
                                               ]}
            sentence_dict["form"] = f"{char}{connective}{chr(ord(char)+1)}"
            sentence = f"{quantifier}x {predicate1}(x, {sport1}) \
                {connective} {predicate2}(x, {sport2})"
        # Rule 4
        elif rule == 1:
            quantifier = choice(quantifiers)
            sentence_dict["quantifiers"] = [quantifier, "x"]
            predicate1 = choice(predicates)
            sport1 = choice(pick_sports)
            pick_sports.remove(sport1)
            predicate2 = choice(predicates)
            sport2 = choice(pick_sports)
            pick_sports.remove(sport2)
            predicate3 = choice(predicates)
            sport3 = choice(pick_sports)
            pick_sports.remove(sport3)
            connective1 = choice(connectives)
            connective2 = choice(connectives)
            # Ensure no more than one implication
            while connective1 == connective2 == "→":
                connective2 = choice(connectives)
            sentence_dict["predicates"] = {char: [predicate1, "x", sport1],
                                           chr(ord(char)+1): [
                                               predicate2, "x", sport2
                                               ],
                                           chr(ord(char)+2): [
                                               predicate3, "x", sport3
                                               ]}
            # Randomly place parentheses either between first two predicates
            # or last two predicates if the connectives are not the same
            if connective1 != connective2:
                if randint(0, 1) == 0:
                    sentence_dict["form"] = f"({char}{connective1}\
                        {chr(ord(char)+1)}){connective2}{chr(ord(char)+2)}"
                    sentence = f"{quantifier}x ({predicate1}(x, {sport1})\
                        {connective1} {predicate2}(x, {sport2})) {connective2}\
                        {predicate3}(x, {sport3})"
                else:
                    sentence_dict["form"] = f"{char}{connective1}\
                        ({chr(ord(char)+1)}{connective2}{chr(ord(char)+2)})"
                    sentence = f"{quantifier}x {predicate1}(x, {sport1}) \
                        {connective1} ({predicate2}(x, {sport2}) \
                        {connective2} {predicate3}(x, {sport3}))"
            # If connectives are the same (i.e. two and or two or),
            # no need for extra parentheses
            else:
                sentence_dict["form"] = f"{char}{connective1}\
                    {chr(ord(char)+1)}{connective2}{chr(ord(char)+2)}"
                sentence = f"{quantifier}x {predicate1}(x, {sport1})\
                    {connective1} {predicate2}(x, {sport2}) \
                    {connective2} {predicate3}(x, {sport3})"
        # Rule 5
        else:
            quantifier1 = "∀"
            quantifier2 = "∃"
            sentence_dict["quantifiers"] = [quantifier1, "x", quantifier2, "y"]
            predicate1 = choice(predicates)
            sentence_dict["predicates"] = {char: [predicate1, "x", "y"]}
            sentence_dict["form"] = char
            sentence = f"{quantifier1}x {quantifier2}y {predicate1}(x, y)"
        # Check sentence is not a duplicate
        if sentence not in [x[0] for x in sentences]:
            sentence_dict["difficulty"] = 1
            # Check if sentence is true or false in image
            sentence_truth_value = evaluate_sentence(sentence_dict, people)
            sentences.append((sentence, sentence_truth_value))
    return sentences, people


# Hard
def generate_pets():
    num_people = randint(3, 6)
    people = []
    pets_list = ["dog", "cat", "rabbit", "hamster",
                 "goldfish", "bird", "snake", "turtle"]
    sizes = ["small", "medium", "large"]
    for i in range(num_people):
        rand = randint(0, 9)
        pets = []
        if rand < 1:
            num_pets = 0
        elif rand < 8:
            num_pets = 1
        else:
            num_pets = 2
        for j in range(num_pets):
            pet = {}
            pet["type"] = choice(pets_list)
            pet["size"] = choice(sizes)
            pets.append(pet)
        people.append({"name": f"Person{i+1}", "pets": pets})
    predicates_x = ["owns"]
    connectives = ["∧", "∨"]
    quantifiers = ["∃", "∀"]
    sentences = []
    # Generates 4 sentences of hard difficulty,
    # each sentence should fall under one of the following 2 rules:
    # 1. a sentence with 2 quantifiers, 2 predicates and one implication
    # (Rule 6 in Table 2.1)
    # 2. a sentence with 2 quantifiers, 3 predicates, two connectives and
    # one implication
    # (Rule 7 in Table 2.1)
    while len(sentences) < 4:
        char = "P"
        sentence_dict = {}
        rule = randint(0, 1)
        # Rule 6
        if rule == 0:
            quantifier1 = choice(quantifiers)
            quantifier2 = "∃"
            sentence_dict["quantifiers"] = [quantifier1, "x", quantifier2, "y"]
            predicate1 = choice(predicates_x)
            connective = "∧"
            predicate2 = choice(sizes)
            sentence_dict["predicates"] = {char: [predicate1, "x", "y"],
                                           chr(ord(char)+1): [predicate2, "y"]}
            sentence_dict["form"] = f"{char}{connective}{chr(ord(char)+1)}"
            sentence = f"{quantifier1}x {quantifier2}y {predicate1}(x, y)\
                {connective} {predicate2}(y)"
        # Rule 7
        elif rule == 1:
            quantifier1 = choice(quantifiers)
            quantifier2 = "∃"
            sentence_dict["quantifiers"] = [quantifier1, "x", quantifier2, "y"]
            predicate1 = choice(predicates_x)
            connective1 = "→"
            connective2 = choice(connectives)
            predicate2 = choice(pets_list)
            predicate3 = choice(sizes)
            sentence_dict["predicates"] = {char: [predicate1, "x", "y"],
                                           chr(ord(char)+1): [predicate2, "y"],
                                           chr(ord(char)+2): [predicate3, "y"]}
            sentence_dict["form"] = f"{char}{connective1}({chr(ord(char)+1)}\
                {connective2}{chr(ord(char)+2)})"
            sentence = f"{quantifier1}x {quantifier2}y {predicate1}(x, y)\
                {connective1} ({predicate2}(y) {connective2} {predicate3}(y))"
        # Check sentence is not a duplicate
        if sentence not in [x[0] for x in sentences]:
            sentence_dict["difficulty"] = 2
            # Check if sentence is true or false in image
            sentence_truth_value = evaluate_sentence(sentence_dict, people)
            sentences.append((sentence, sentence_truth_value))
    return sentences, people
