def build_code(command, templates):
    command_parts = command.split("-")
    command_type = command_parts[0].strip()
    command_data = command_parts[1].strip() if len(command_parts) > 1 else None

    if command_type == "create a variable":
        data_type = command_data.split()[0]
        variable_name = command_data.split()[1]
        variable_value = command_data.split()[3] if len(command_data.split()) > 2 else None
        if variable_value:
            return f"{variable_name} = {variable_value}"
        else:
            return f"{variable_name} = {data_type}()"

    elif command_type == "create a list":
        list_name = command_data.split()[1]
        list_elements = command_data.split()[3:]
        list_elements_str = ", ".join(list_elements)
        return f"{list_name} = [{list_elements_str}]"

    elif command_type == "create a for loop":
        loop_variable = command_data.split()[3]
        loop_range = command_data.split()[5:]
        loop_range_str = " ".join(loop_range)
        loop_code = "\n".join(templates["for_loop"])
        loop_code = loop_code.replace("$variable", loop_variable)
        loop_code = loop_code.replace("$range", loop_range_str)
        return loop_code

    elif command_type == "add an if statement":
        condition = command_data.split(" if ")[1]
        if_code = "\n".join(templates["if_statement"])
        if_code = if_code.replace("$condition", condition)
        return if_code

    elif command_type == "close for loop" or command_type == "close if statement":
        return ""

    else:
        return "Command Not Recognised"
