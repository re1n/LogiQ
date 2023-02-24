import random

# Students in a class scenario
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

def deepest_bracket_level(string):
    stack = []
    max_depth = 0
    depth = 0
    num_occurrences = 0
    for char in string:
        if char == "(":
            stack.append(char)
            depth += 1
            if depth > max_depth:
                max_depth = depth
                num_occurrences = 1
            elif depth == max_depth:
                num_occurrences += 1
        elif char == ")":
            stack.pop()
            depth -= 1
    return max_depth, num_occurrences

def evaluate_truth_values(v1, v2, conn):
    if conn == "∧":
        return v1 and v2
    elif conn == "∨":
        return v1 or v2
    elif conn == "→":
        return not v1 or v2
    elif conn == "↔":
        return v1 == v2

def evaluate_predicates(p1, p2, conn, item={}, variables=[]):
    if not variables:
        if p1 not in ["0", "1"] and p2 not in ["0", "1"]:
            p1_truth = item[p1]
            p2_truth = item[p2]
            return evaluate_truth_values(p1_truth, p2_truth, conn)
        elif p1 not in ["0", "1"] and p2 in ["0", "1"]:
            p1_truth = item[p1]
            p2_truth = False if p2 == "0" else True
            return evaluate_truth_values(p1_truth, p2_truth, conn)
        elif p1 in ["0", "1"] and p2 not in ["0", "1"]:
            p1_truth = False if p1 == "0" else True
            p2_truth = item[p2]
            return evaluate_truth_values(p1_truth, p2_truth, conn)
    else:
        variable1, variable2 = variables
        if p1 not in ["0", "1"] and p2 not in ["0", "1"]:
            p1_truth = True if variable1 in item[p1] else False
            p2_truth = True if variable2 in item[p2] else False
            return evaluate_truth_values(p1_truth, p2_truth, conn)
        elif p1 not in ["0", "1"] and p2 in ["0", "1"]:
            p1_truth = True if variable1 in item[p1] else False
            p2_truth = False if p2 == "0" else True
            return evaluate_truth_values(p1_truth, p2_truth, conn)
        elif p1 in ["0", "1"] and p2 not in ["0", "1"]:
            p1_truth = False if p1 == "0" else True
            p2_truth = True if variable2 in item[p2] else False
            return evaluate_truth_values(p1_truth, p2_truth, conn)
    if p1 in ["0", "1"] and p2 in ["0", "1"]:
        p1_truth = False if p1 == "0" else True
        p2_truth = False if p2 == "0" else True
        return evaluate_truth_values(p1_truth, p2_truth, conn)

def evaluate_sentence(sentence, scenario):
    # Classroom scenario
    if len(sentence["quantifiers"]) == 2 and sentence["variables"] == 1:
        quantifier = sentence["quantifiers"][0]
        truth_values = []
        for item in scenario:
            formula = sentence["form"]
            max_depth, num_occurrences = deepest_bracket_level(sentence["form"])
            while max_depth > 0:
                depth = 0
                j = 0
                for i in range(num_occurrences):
                    while j+3 < len(formula):
                        if formula[j] == "(":
                            depth += 1
                        if depth == max_depth:
                            p1 = formula[j+1]
                            if p1 != "1" and p1 != "0":
                                predicate1 = sentence["predicates"][p1][0]
                            else:
                                predicate1 = p1
                            p2 = formula[j+3]
                            if p2 != "1" and p2 != "0":
                                predicate2 = sentence["predicates"][p2][0]
                            else:
                                predicate2 = p2
                            conn = formula[j+2]
                            if evaluate_predicates(predicate1, predicate2, conn, item):
                                formula = formula.replace(formula[j:j+5], "1")
                            else:
                                formula = formula.replace(formula[j:j+5], "0")
                            depth -= 1
                        j += 1
                max_depth -= 1
            if len(formula) == 1:
                if item[sentence["predicates"][formula][0]]:
                    formula = "1"
                else:
                    formula = "0"
            else:
                while len(formula) > 1:
                    c1 = formula[0]
                    conn = formula[1]
                    c2 = formula[2]
                    if c1 in ["0", "1"] and c2 in ["0", "1"]:
                        c1_truth = False if c1 == "0" else True
                        c2_truth = False if c2 == "0" else True
                        if evaluate_truth_values(c1_truth, c2_truth, conn):
                            formula = formula.replace(formula[0:3], "1")
                        else:
                            formula = formula.replace(formula[0:3], "0")
                    else:
                        if c1 not in ["0", "1"]:
                            c1 = sentence["predicates"][c1][0]
                        if c2 not in ["0", "1"]:
                            c2 = sentence["predicates"][c2][0]
                        if evaluate_predicates(c1, c2, conn, item):
                            formula = formula.replace(formula[0:3], "1")
                        else:
                            formula = formula.replace(formula[0:3], "0")
            if formula == "1":
                truth_values.append(True)
            else:
                truth_values.append(False)
    # Favourite sports scenario
    elif len(sentence["quantifiers"]) == 2 and sentence["variables"] == 2:
        quantifier = sentence["quantifiers"][0]
        truth_values = []
        for item in scenario:
            formula = sentence["form"]
            max_depth, num_occurrences = deepest_bracket_level(sentence["form"])
            while max_depth > 0:
                depth = 0
                j = 0
                for i in range(num_occurrences):
                    while j+3 < len(formula):
                        if formula[j] == "(":
                            depth += 1
                        if depth == max_depth:
                            p1 = formula[j+1]
                            if p1 != "1" and p1 != "0":
                                predicate1 = sentence["predicates"][p1][0]
                                variable1 = sentence["predicates"][p1][2]
                            else:
                                predicate1 = p1
                            p2 = formula[j+3]
                            if p2 != "1" and p2 != "0":
                                predicate2 = sentence["predicates"][p2][0]
                                variable2 = sentence["predicates"][p2][2]
                            else:
                                predicate2 = p2
                            conn = formula[j+2]
                            if evaluate_predicates(predicate1, predicate2, conn, item, [variable1, variable2]):
                                formula = formula.replace(formula[j:j+5], "1")
                            else:
                                formula = formula.replace(formula[j:j+5], "0")
                            depth -= 1
                        j += 1
                max_depth -= 1
            if len(formula) == 1:
                predicate = sentence["predicates"][formula][0]
                variable = sentence["predicates"][formula][2]
                if variable in item[predicate]:
                    formula = "1"
                else:
                    formula = "0"
            else:
                while len(formula) > 1:
                    c1 = formula[0]
                    conn = formula[1]
                    c2 = formula[2]
                    if c1 in ["0", "1"] and c2 in ["0", "1"]:
                        c1_truth = False if c1 == "0" else True
                        c2_truth = False if c2 == "0" else True
                        if evaluate_truth_values(c1_truth, c2_truth, conn):
                            formula = formula.replace(formula[0:3], "1")
                        else:
                            formula = formula.replace(formula[0:3], "0")
                    else:
                        if c1 not in ["0", "1"]:
                            predicate1 = sentence["predicates"][c1][0]
                            variable1 = sentence["predicates"][c1][2]
                        if c2 not in ["0", "1"]:
                            predicate2 = sentence["predicates"][c2][0]
                            variable2 = sentence["predicates"][c2][2]
                        if evaluate_predicates(predicate1, predicate2, conn, item, [variable1, variable2]):
                            formula = formula.replace(formula[0:3], "1")
                        else:
                            formula = formula.replace(formula[0:3], "0")
            if formula == "1":
                truth_values.append(True)
            else:
                truth_values.append(False)
    
    elif len(sentence["quantifiers"]) == 4 and sentence["variables"] == 2:
        quantifier1 = sentence["quantifiers"][0]
        quantifier2 = sentence["quantifiers"][2]
        # For all x there exists a y
        if quantifier1 == "∀" and quantifier2 == "∃":
            truth_values = []
            formula = sentence["form"]
            max_depth, num_occurrences = deepest_bracket_level(sentence["form"])
            while max_depth > 0:
                depth = 0
                j = 0
                for i in range(num_occurrences):
                    while j+3 < len(formula):
                        if formula[j] == "(":
                            depth += 1
                        if depth == max_depth:
                            p1 = formula[j+1]
                            if p1 != "1" and p1 != "0":
                                predicate1 = sentence["predicates"][p1][0]
                                for item in scenario:
                                    if not item[predicate1]:
                                        predicate1 = "0"
                                        break
                                if predicate1 != "0":
                                    predicate1 = "1"
                            else:
                                predicate1 = p1
                            p2 = formula[j+3]
                            if p2 != "1" and p2 != "0":
                                predicate2 = sentence["predicates"][p2][0]
                                for item in scenario:
                                    if not item[predicate2]:
                                        predicate2 = "0"
                                        break
                                if predicate2 != "0":
                                    predicate2 = "1"
                            else:
                                predicate2 = p2
                            conn = formula[j+2]
                            if evaluate_predicates(predicate1, predicate2, conn, item):
                                formula = formula.replace(formula[j:j+5], "1")
                            else:
                                formula = formula.replace(formula[j:j+5], "0")
                            depth -= 1
                        j += 1
                max_depth -= 1
            if len(formula) == 1:
                predicate = sentence["predicates"][formula][0]
                for item in scenario:
                    if not item[predicate]:
                        formula = "0"
                        break
                if formula != "0":
                    formula = "1"
            else:
                while len(formula) > 1:
                    c1 = formula[0]
                    conn = formula[1]
                    c2 = formula[2]
                    if c1 in ["0", "1"] and c2 in ["0", "1"]:
                        c1_truth = False if c1 == "0" else True
                        c2_truth = False if c2 == "0" else True
                        if evaluate_truth_values(c1_truth, c2_truth, conn):
                            formula = formula.replace(formula[0:3], "1")
                        else:
                            formula = formula.replace(formula[0:3], "0")
                    else:
                        if c1 not in ["0", "1"]:
                            predicate1 = sentence["predicates"][c1][0]
                            for item in scenario:
                                if not item[predicate1]:
                                    c1 = "0"
                                    break
                            if c1 != "0":
                                c1 = "1"
                        if c2 not in ["0", "1"]:
                            predicate2 = sentence["predicates"][c2][0]
                            for item in scenario:
                                if not item[predicate2]:
                                    c2 = "0"
                                    break
                            if c2 != "0":
                                c2 = "1"
                        if evaluate_predicates(predicate1, predicate2, conn, item):
                            formula = formula.replace(formula[0:3], "1")
                        else:
                            formula = formula.replace(formula[0:3], "0")
            if formula == "1":
                return True
            else:
                return False
            
    if quantifier == "∀":
        return False if False in truth_values else True
    elif quantifier == "∃":
        return True if True in truth_values else False


generate_favourite_sports()