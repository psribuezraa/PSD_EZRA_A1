# Function to check if the given character is an operator
def is_operator(char):
    return char in ['+', '-', '*', '/']

# Function to get the precedence of the operator
def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '*' or operator == '/':
        return 2
    else:
        return 0

# Function to convert infix expression to postfix expression
def infix_postfix(infix):
    postfix = ''
    stack = []
    for char in infix:
        if char.isalnum():
            postfix += char
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
                postfix += stack.pop()
            stack.pop()  # Pop '('
        elif is_operator(char):
            while stack and precedence(stack[-1]) >= precedence(char):
                postfix += stack.pop()
            stack.append(char)
    while stack:
        postfix += stack.pop()
    return postfix

# Function to evaluate postfix expression
def evaluate_postfix(postfix):
    stack = []
    for char in postfix:
        if char.isdigit():
            stack.append(int(char))
        elif is_operator(char):
            operand2 = stack.pop()
            operand1 = stack.pop()
            if char == '+':
                stack.append(operand1 + operand2)
            elif char == '-':
                stack.append(operand1 - operand2)
            elif char == '*':
                stack.append(operand1 * operand2)
            elif char == '/':
                stack.append(operand1 / operand2)
    return stack.pop()

# Test the functions
if __name__ == "__main__":
    infix_expression = input("Enter the infix expression: ")
    postfix_expression = infix_to_postfix(infix_expression)
    print("Postfix expression:", postfix_expression)
    result = evaluate_postfix(postfix_expression)
    print("Result:", result)
