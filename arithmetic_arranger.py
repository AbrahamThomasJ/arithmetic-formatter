import re

def arithmetic_arranger(problems,solve = False):
    
    if len(problems) > 5:
        return "Error: Too many problems."
     
    first = ''
    second = ''
    lines = ''
    res = ''
    string = ''
    
    for problem in problems:


        if(re.search("[^\s0-9.+-]",problem)):                       
            if(re.search("[/]",problem) or re.search("[*]",problem)):  
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."

        firstNumber = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        secondNumber = problem.split(' ')[2]

        if len(firstNumber) > 4 or len(secondNumber) > 4:
            return "Error: Numbers cannot be more than four digits."
        

        length = max(len(firstNumber),len(secondNumber)) + 2
        firstLine = firstNumber.rjust(length)
        secondLine = operator + secondNumber.rjust(length -1)

        line = ''
        for s in range(length):
            line += '-'
        
        result = ''
        if operator == '+':
            result = str(int(firstNumber) + int(secondNumber)).rjust(length)
        elif operator == '-':
            result = str(int(firstNumber) - int(secondNumber)).rjust(length)

        if problem != problems[-1]:
            first += firstLine + '   '
            second += secondLine + '   '
            lines += line + '   '
            res += result + '   '
        else:
            first += firstLine
            second += secondLine
            lines += line
            res += result
        
    if solve:
        string += first + '\n' + second + '\n' + lines + '\n' + res 
    else:
        string += first + '\n' + second + '\n' + lines

    return string















