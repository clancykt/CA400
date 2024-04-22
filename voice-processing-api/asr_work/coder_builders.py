from Levenshtein import distance
from word2number import w2n

# Builder for variable code
def build_variable_code(variableText, fixedCommand, templateList):
    # Data Type accepted = ["List", "string", "number "]
    equals_equivalents = ["equals", "equal", "is"]
    tokens = variableText.split(" ")
    variable_type = ""

    for token in tokens:
        if token in equals_equivalents: 
            equals_index = tokens.index(token)
        if token == "type":
            variable_type  =  tokens[(tokens.index(token) + 1)]
   
    # Checks if type == number
    if distance(variable_type, "number") < 5:
        print("Type: " + variable_type)
        variable_name = tokens[(equals_index - 1)]
        varibale_value = w2n.word_to_num(tokens[(equals_index + 1)])
    elif distance(variable_type, "string") < 5:
        # Defaulting to type string
        print("Type: " + variable_type)
        variable_name = tokens[(equals_index - 1)]
        varibale_value = "\"" + tokens[(equals_index + 1)] + "\""
    elif distance(variable_type, "list") < 5:
        print("Type: " + variable_type)
        variable_name = tokens[(equals_index - 1)]
        varibale_value = [token for token in tokens if (token != "and") and tokens.index(token) > equals_index]

    # Fetches correctc code template from template file
    for template in templateList:
        if(template['command'] == fixedCommand):
            correctCode = template['code'].format(variable_name, varibale_value)

    return correctCode

# Builder for if statement code
def build_if_statement_code(variableText, fixedCommand, templateList):
    comparison_mappings = {"less than": "<", "greater than": ">", "greater than or equal to": ">=", "less than or equal to": "<=", "is equal to": "=="}
    
    tmp = variableText.split("condition")
    condition = tmp[1]
    split_condition = condition.split()
    condition_target = split_condition[0]
    condition_value = split_condition[len(split_condition) - 1]

    comparison_operator = ""
    acceptable_distance = 13
    lowest_score_match = ("initial", 1000)

    
    for key in comparison_mappings.keys():
        key_distance = distance(key, condition)
        if(key_distance <= acceptable_distance) and key_distance < lowest_score_match[1]:
            lowest_score_match = (comparison_mappings[key], key_distance)
            
    comparison_operator = lowest_score_match[0]

    for template in templateList:
        if(template['command'] == fixedCommand):
            code = template['code'].format(condition_target, comparison_operator, condition_value)

    return code

# Builder for for loop code
def build_for_loop_code(variableText, fixedCommand, templateList):
    tokens = variableText.split(" ")
    in_index = 0

    for token in tokens:
        if token == "in":
            in_index = tokens.index(token)
    
    iterating_variable = tokens[(in_index - 1)]
    iterated_variable = tokens[(in_index) + 1]

    for template in templateList:
        if(template['command'] == fixedCommand):
            code = template['code'].format(iterating_variable, iterated_variable)

    return code


# Builder for print code
def build_print_statement(variableText, fixedCommand, templateList):
    tokens = variableText.split(" ")
    types = ["variable", "string"]
    print_output = ""

    for token in tokens:
        if token == "string":
            string_key_index = tokens.index(token)
            user_string_tokens = [token for token in tokens if tokens.index(token) > string_key_index]
            print_output = " ".join(user_string_tokens)
            print_output = "\"" + print_output + "\""
        elif token == "variable":
            print_output = tokens[(tokens.index(token) + 1)]
        
    for template in templateList:
        if(template['command'] == fixedCommand):
            code = template['code'].format(print_output)

    return code

# Testing: Acceptable distance = 10
#  x is less than ar equal to four: 23
#  x is less than ar equal to four: 26
#  x is less than ar equal to four: 15
#  x is less than ar equal to four: 12
#  x is less than ar equal to four: 21

# Testing: Acceptable distance = 13
#  x is less than or equal to four: 23
#  x is less than or equal to four: 26
#  x is less than or equal to four: 14
#  x is less than or equal to four: 11
#  x is less than or equal to four: 21