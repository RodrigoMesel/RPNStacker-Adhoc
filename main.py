import re

class Regex:

    def isNum(token):
        x = re.findall( "[0-9]", str(token))
        if x:
            return True
        return False

    def isOP(token):
        x = re.findall("[+-/*]", token)
        if x:
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
#file = open("exampleWithError.txt", "r") # Se quiser testar com erro descomenta essa linha
content = file.read() #Le o input
content = content.split() #Trata o input
regex = Regex #Instancia a classe regex
tokenList = [] #Cria uma lista de tokens

#Scanning:
for line in content: 
    if line == '':
        continue

    if (regex.isNum(line) or regex.isOP(line)): #Checagem com regex

        if(line == '+'):
            tokenList.append("type= PLUS")
            tokenList.append("lexeme= +")

        elif(line == '-'):
            tokenList.append("type= MINUS")
            tokenList.append("lexeme= -")    

        elif(line == '*'):
            tokenList.append("type= STAR")
            tokenList.append("lexeme= *")  

        elif(line == '/'):
            tokenList.append("type= SLASH")
            tokenList.append("lexeme= /")  

        else:
            tokenList.append("type= NUM")
            tokenList.append("lexeme= " + str(line))
    
    else:
        print( line + " não é um token válido" )
        raise Exception (" Token Inválido ")


stack = []
for i in range(0, len(tokenList), 2): # Vai fazendo as operações usando a stack
    if tokenList[i] == "type= NUM":
        stack.append(int(tokenList[i+1][8:]))
    else:
        op1 = stack.pop()
        op2 = stack.pop()
        stack.append(doOperation(tokenList[i+1][8:], op2, op1))

print("Resultado final: " + str(stack.pop()))


