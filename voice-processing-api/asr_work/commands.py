target_words = ['print', 'hello', 'world', 'for', 'in', 'range', 'colon', 'indent', 'variable', 'function', 'return', 'add', 'subtract', 'multiply', 'divide', 'arithmetic', 'operation', 'argument', 'if', 'else', 'comparison', 'operator', 'equal', 'not equal', 'less than', 'greater than', 'boolean', 'true', 'false', 'and', 'or', 'comment', 'hashtag', 'quote', 'parenthesis', 'brackets', 'curly brackets', 'integer', 'float', 'string']

def handle_spoken_command(text):
    for word in target_words:
        if word in str(text).lower():
            if word == 'indent':
                print('    ', end='')
            else:
                print(word + ' ', end='')
            return True
    return False
