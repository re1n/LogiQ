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
