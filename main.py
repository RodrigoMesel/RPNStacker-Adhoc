def isValidToken(token): # Checagem se o token é valido
    if(token == '+' or token == '-' or token == '*' or token == '/' or token.isnumeric()):
        return True 
    return False

def doOperation(operator, operand1, operand2): # Faz a operação
    if operator == '+':
        return operand1 + operand2
    if operator == '-':
        return operand1 - operand2
    if operator == '*':
        return operand1 * operand2
    if operator == '/':
        return operand1 / operand2


file = open("example.txt", "r")
content = file.read()
content = content.strip() #Le o input

tokenList = []
#Scanning:
for lines in content: #trata o input e ccria a lista de tokens
    lines = lines.rstrip()
    if lines == '':
        continue
    elif (not isValidToken(lines)):
        print("Token Invalido: " + lines)
    else: 
        if(lines == '+'):
            tokenList.append("type= PLUS")
            tokenList.append("lexeme= +")

        elif(lines == '-'):
            tokenList.append("type= MINUS")
            tokenList.append("lexeme= -")    

        elif(lines == '*'):
            tokenList.append("type= STAR")
            tokenList.append("lexeme= *")  

        elif(lines == '/'):
            tokenList.append("type= SLASH")
            tokenList.append("lexeme= /")  

        else:
            tokenList.append("type= NUM")
            tokenList.append("lexeme= " + str(lines))


stack = []
for i in range(0, len(tokenList), 2): # Vai fazendo as operações usando a stack
    if tokenList[i] == "type= NUM":
        stack.append(int(tokenList[i+1][8:]))
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(doOperation(tokenList[i+1][8:], op2, op1))

print("Resultado final: " + stack.pop())
