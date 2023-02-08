import random

# Students in a class scenario
def generate_classroom():
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
            sentence_true = evaluate_sentence(sentence_dict, students)
            sentences.append((sentence, sentence_true))
    for pair in sentences:
        print(f"{pair[0]} is {pair[1]}")
    return sentences, students

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

def evaluate_predicates(p1, p2, conn, item={}):
    print(f"p1: {p1}, p2: {p2}, conn: {conn}, item: {item}")
    if p1 not in ["0", "1"] and p2 not in ["0", "1"]:
        if conn == "∧":
            return item[p1] and item[p2]
        elif conn == "∨":
            return item[p1] or item[p2]
        elif conn == "→":
            return not item[p1] or item[p2]
        elif conn == "↔":
            return item[p1] == item[p2]
    elif p1 not in ["0", "1"] and p2 in ["0", "1"]:
        p2 = False if p2 == "0" else True
        if conn == "∧":
            return item[p1] and p2
        elif conn == "∨":
            return item[p1] or p2
        elif conn == "→":
            return not item[p1] or p2
        elif conn == "↔":
            return item[p1] == p2
    elif p1 in ["0", "1"] and p2 not in ["0", "1"]:
        p1 = False if p1 == "0" else True
        if conn == "∧":
            return p1 and item[p2]
        elif conn == "∨":
            return p1 or item[p2]
        elif conn == "→":
            return not p1 or item[p2]
        elif conn == "↔":
            return p1 == item[p2]
    elif p1 in ["0", "1"] and p2 in ["0", "1"]:
        p1 = False if p1 == "0" else True
        p2 = False if p2 == "0" else True
        if conn == "∧":
            return p1 and p2
        elif conn == "∨":
            return p1 or p2
        elif conn == "→":
            return not p1 or p2
        elif conn == "↔":
            return p1 == p2

def evaluate_sentence(sentence, scenario):
    if len(sentence["quantifiers"]) == 2:
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
                        if evaluate_predicates(c1, c2, conn, item):
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
    if quantifier == "∀":
        return False if False in truth_values else True
    elif quantifier == "∃":
        return True if True in truth_values else False