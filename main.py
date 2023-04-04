def doOperation(operator, operand1, operand2): 
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2

stack = []
print("Se você quiser encerrar digite 'fim'")

while True:
    x = input()
    if x == 'fim':
        print("Resultado final: " + str(stack.pop()))
        break
    elif(x.isnumeric()):
        stack.append(int(x))
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(doOperation(x, op2, op1))

