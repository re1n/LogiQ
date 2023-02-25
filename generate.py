import random

from logic import evaluate_sentence

# Easy
def generate_classroom():
    num_students = random.randint(4, 7)
    students = []
    for i in range(num_students):
        has_laptop = False
        has_calculator = False
        has_pencil = False
        if random.randint(0, 9) > 3:
            has_laptop = True
        if random.randint(0, 9) > 3:
            has_calculator = True
        if random.randint(0, 9) > 3:
            has_pencil = True
        students.append({"name": f"Student{i+1}", "hasLaptop": has_laptop, "hasCalculator": has_calculator, "hasPencil": has_pencil})
    predicates = ["hasLaptop", "hasCalculator", "hasPencil"]
    connectives = ["∧", "∨"]
    quantifiers = ["∃", "∀"]
    sentences = []
    while len(sentences) < 4:
        char = "P"
        sentence_dict = {}
        quantifier = random.choice(quantifiers)
        sentence_dict["quantifiers"] = [quantifier, "x"]
        if random.randint(0, 1) == 0:
            predicate1 = random.choice(predicates)
            sentence_dict["predicates"] = {char: [predicate1, "x"]}
            predicate = f"{predicate1}(x)"
            sentence_dict["form"] = char
        else:
            predicate1 = random.choice(predicates)
            predicate2 = random.choice(predicates)
            while predicate1 == predicate2:
                predicate2 = random.choice(predicates)
            connective = random.choice(connectives)
            predicate = f"{predicate1}(x) {connective} {predicate2}(x)"
            sentence_dict["predicates"] = {char: [predicate1, "x"], chr(ord(char)+1): [predicate2, "x"]}
            sentence_dict["form"] = f"{char}{connective}{chr(ord(char)+1)}"
        sentence = f"{quantifier}x {predicate}"
        if sentence not in [x[0] for x in sentences]:
            sentence_dict["variables"] = 1
            sentence_true = evaluate_sentence(sentence_dict, students)
            sentences.append((sentence, sentence_true))
    for pair in sentences:
        print(f"{pair[0]} is {pair[1]}")
    return sentences, students

# Medium
def generate_favourite_sports():
    num_people = random.randint(4, 7)
    people = []
    sports = ["football", "basketball", "tennis", "rugby", "cricket", "golf", "hockey", "athletics"]
    for i in range(num_people):
        pick_sports = sports.copy()
        if random.randint(0, 9) > 2:
            num_likes = random.randint(1, 3)
        else:
            num_likes = 0
        if random.randint(0, 9) > 2:
            num_dislikes = random.randint(1, 3)
        else:
            num_dislikes = 0
        likes = []
        dislikes = []
        for j in range(num_likes):
            sport = random.choice(pick_sports)
            likes.append(sport)
            pick_sports.remove(sport)
        for j in range(num_dislikes):
            sport = random.choice(pick_sports)
            dislikes.append(sport)
            pick_sports.remove(sport)
        people.append({"name": f"Person{i+1}", "likes": likes, "dislikes": dislikes})
    predicates = ["likes", "dislikes"]
    connectives = ["∧", "∨", "→"]
    quantifiers = ["∃", "∀"]
    sentences = []
    # generate 4 sentences of medium difficulty, each sentence should fall under one of the following 3 rules:
    # 1. a sentence with 1 quantifier, 2 predicates, 1 connective and 1 implication
    # 2. a sentence with 1 quantifier, 3 predicates, 2 connectives and 1 implication
    # 3. a sentence with 2 quantifiers, 1 or 2 predicates, 0 or 1 connectives and no implication
    while len(sentences) < 4:
        pick_sports = sports.copy()
        char = "P"
        sentence_dict = {}
        rule = random.randint(0, 2)
        if rule == 0:
            quantifier = random.choice(quantifiers)
            sentence_dict["quantifiers"] = [quantifier, "x"]
            predicate1 = random.choice(predicates)
            sport1 = random.choice(pick_sports)
            pick_sports.remove(sport1)
            predicate2 = random.choice(predicates)
            sport2 = random.choice(pick_sports)
            pick_sports.remove(sport2)
            connective = random.choice(connectives)
            sentence_dict["predicates"] = {char: [predicate1, "x", sport1], chr(ord(char)+1): [predicate2, "x", sport2]}
            sentence_dict["form"] = f"{char}{connective}{chr(ord(char)+1)}"
            sentence = f"{quantifier}x {predicate1}(x, {sport1}) {connective} {predicate2}(x, {sport2})"
        elif rule == 1:
            quantifier = random.choice(quantifiers)
            sentence_dict["quantifiers"] = [quantifier, "x"]
            predicate1 = random.choice(predicates)
            sport1 = random.choice(pick_sports)
            pick_sports.remove(sport1)
            predicate2 = random.choice(predicates)
            sport2 = random.choice(pick_sports)
            pick_sports.remove(sport2)
            predicate3 = random.choice(predicates)
            sport3 = random.choice(pick_sports)
            pick_sports.remove(sport3)
            connective1 = random.choice(connectives)
            connective2 = random.choice(connectives)
            while connective1 == connective2 == "→":
                connective2 = random.choice(connectives)
            sentence_dict["predicates"] = {char: [predicate1, "x", sport1], chr(ord(char)+1): [predicate2, "x", sport2], chr(ord(char)+2): [predicate3, "x", sport3]}
            if connective1 != connective2:
                if random.randint(0, 1) == 0:
                    sentence_dict["form"] = f"({char}{connective1}{chr(ord(char)+1)}){connective2}{chr(ord(char)+2)}"
                    sentence = f"{quantifier}x ({predicate1}(x, {sport1}) {connective1} {predicate2}(x, {sport2})) {connective2} {predicate3}(x, {sport3})"
                else:
                    sentence_dict["form"] = f"{char}{connective1}({chr(ord(char)+1)}{connective2}{chr(ord(char)+2)})"
                    sentence = f"{quantifier}x {predicate1}(x, {sport1}) {connective1} ({predicate2}(x, {sport2}) {connective2} {predicate3}(x, {sport3}))"
            else:
                sentence_dict["form"] = f"{char}{connective1}{chr(ord(char)+1)}{connective2}{chr(ord(char)+2)}"
                sentence = f"{quantifier}x {predicate1}(x, {sport1}) {connective1} {predicate2}(x, {sport2}) {connective2} {predicate3}(x, {sport3})"
        else:
            quantifier1 = "∀"
            quantifier2 = "∃"
            sentence_dict["quantifiers"] = [quantifier1, "x", quantifier2, "y"]
            predicate1 = random.choice(predicates)
            sentence_dict["predicates"] = {char: [predicate1, "x", "y"]}
            sentence_dict["form"] = char
            sentence = f"{quantifier1}x {quantifier2}y {predicate1}(x, y)"
        if sentence not in [x[0] for x in sentences]:
            sentence_dict["variables"] = 2
            sentence_true = evaluate_sentence(sentence_dict, people)
            sentences.append((sentence, sentence_true))
    for pair in sentences:
        print(f"{pair[0]} is {pair[1]}")
    for person in people:
        print(f"{person['name']} likes {person['likes']}, dislikes {person['dislikes']}")
    return sentences, people
