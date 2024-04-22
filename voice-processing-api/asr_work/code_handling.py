from asr_work.coder_builders import build_variable_code, build_if_statement_code, build_print_statement, build_for_loop_code


def build_code(command, templateList):
    code = ""
    
    tmp = command.split("-")
    fixed_command = tmp[0]
    variableText = tmp[1]

    print(fixed_command)

    if(fixed_command == "create a variable"):
        code = build_variable_code(variableText, fixed_command, templateList)
    elif(fixed_command == "add an if statement"):
        code = build_if_statement_code(variableText, fixed_command, templateList)
    elif(fixed_command == "create a for loop"):
        code = build_for_loop_code(variableText, fixed_command, templateList)
    elif(fixed_command == "add a print statement"):
        code = build_print_statement(variableText, fixed_command, templateList)
    else:
        for template in templateList:
            if(template['command'] == fixed_command):
                code = template['code']

    return code


