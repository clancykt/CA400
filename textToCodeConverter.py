import ast

def text_to_code(text):

    # parse the spoken text into an abstract syntax tree
    tree = ast.parse(text)

    # extract the first statement from the tree
    statement = tree.body[0]

    # evaluate the statement and return the result
    # eval() is a built in python function for evaluating strings as python expressions
    return eval(compile(ast.Expression(statement.value), '', 'eval'))

