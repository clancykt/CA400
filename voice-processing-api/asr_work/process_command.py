from Levenshtein import distance

commands = ["create a variable", "create a for loop", "add a print statement", "add an if statement", "close for loop", "close if statement"]

acceptable_distance = 10

# Accepts command that has the first distance less that or equal to acceptable distance
def idCommand(userCommand):
    lowest_score_match = ("initial", 1000)
    command_cutoff = 15

    considered_command = userCommand[:command_cutoff]
    variable_info = userCommand[command_cutoff:]
    # print(considered_command)

    for command in commands:
        textDistance = distance(command, considered_command)
        # print(command + " / " + userCommand + " - Distance from Fixed Command: " + str(textDistance))
        # print(lowest_score_match)
        if textDistance <= acceptable_distance and textDistance < lowest_score_match[1]:
            lowest_score_match = (command, textDistance)

    if lowest_score_match[0] == "initial":
        return "Command Not Recognised"
    
    return lowest_score_match[0] + "-" + variable_info