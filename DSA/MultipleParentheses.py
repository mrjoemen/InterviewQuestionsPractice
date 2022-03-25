
'''

Check if a string of parentheses/brackets is valid.

Valid Strings: (()), ()[]{}, ({[]})
Invalid Strings: {], ((()), ([{]})

T = o(n)
S = o(n)

YouTube: https://www.youtube.com/watch?v=9kmUaXrjizQ

'''

from sqlalchemy import false


def multipleParenthesis(string: str) -> bool:
    stack = []   
    for i in range(0, len(string)):
        if string[i] == '(' or string[i] == '[' or string[i] == '{':
            stack.append(string[i])
        else:
            if len(stack) == 0:
                return False
            lastItem = stack.pop()
            if string[i] == ')' and lastItem != '(':
                return False
            elif string[i] == ']' and lastItem != '[':
                return False
            elif string[i] == '}' and lastItem != '{':
                return False
    return len(stack) == 0

def main():
    print(multipleParenthesis("(())"))
    print(multipleParenthesis("(({[}]))"))
    print(multipleParenthesis("(()["))
    print(multipleParenthesis(')'))


if __name__ == '__main__':
    main()