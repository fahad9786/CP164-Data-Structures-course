
"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-02"
-------------------------------------------------------
"""

from Stack_array import Stack


def stack_split_alt(source):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks.
    When finished source stack is empty. Values are
    pushed alternately onto the returned target stacks.
    Use: target1, target2 = stack_split_alt(source)
    -------------------------------------------------------
    Parameters:
        source - the stack to split into two parts (Stack)
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    
    target1 = []
    target2 = []
    i = 2
    
    while(not source.is_empty()):
      
        if ((i % 2) == 0):
            target1.append(source.pop())
        else:
            target2.append(source.pop())
        
        i += 1
    return target1, target2



def split_alt(self):
    """
    -------------------------------------------------------
    Splits the source stack into separate target stacks with values
    alternating into the targets. At finish source stack is empty.
    Use: target1, target2 = source.split_alt()
    -------------------------------------------------------
    Returns:
        target1 - contains alternating values from source (Stack)
        target2 - contains other alternating values from source (Stack)
    -------------------------------------------------------
    """
    
    # not 100% sure if its right
    i = 2
    target1 = Stack()
    target2 = Stack()    
    
    while(not self._values.is_empty()):
      
        if ((i % 2) == 0):
            target1.append(self._values.pop())
        else:
            target2.append(self._values.pop())
        
        i += 1
    return target1, target2
    
# Constants
    
def is_palindrome_stack(string):
    """
    -------------------------------------------------------
    Determines if string is a palindrome. Ignores case, digits, spaces, and
    punctuation in string.
    Use: palindrome = is_palindrome_stack(string)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
    Returns:
        palindrome - True if string is a palindrome, False otherwise (bool)
    -------------------------------------------------------
    """
    
    palindrome = False
    
    # making sure all cases are met
    # create a stack
   # 1 2 3 4
    s = Stack()
    # 4 3 2 1
    for i in string:
        if(i.isalpha()):
            s.push(i.lower())
    
    # 1 2 3 4
    strings = ""
    for i in string:
        if(i.isalpha()):
            strings += i.lower()
    
    # 4 3 2 1
    reverse = ""
    while not s.is_empty():
        reverse += s.pop()
    
    if reverse == strings:
        palindrome = True
    
    return palindrome




# Constants
OPERATORS = "+-*/"


def postfix(string):
    
    """
    -------------------------------------------------------
    Evaluates a postfix expression.
    Use: answer = postfix(string)
    -------------------------------------------------------
    Parameters:
        string - the postfix string to evaluate (str)
    Returns:
        answer - the result of evaluating string (float)
    -------------------------------------------------------
    """
    s = Stack()
    
    result = 0
    strings = string.split()
    # 125-
    #
    # checks each elemt in string if its number
    # or operator and then will pussh it to have them in order
    for i in strings:
        
        if(i not in OPERATORS):
            s.push((i))
        
        # pop the 
        elif(i in OPERATORS):
            a = float(s.pop())
            b = float(s.pop())
            
        if i == "+":
            result = b + a
            s.push(result)
        if i == "-":
            result = b - a
            s.push(result)
        if i == "*":
            result = b * a
            s.push(result)
        if i == "/":
            result = b / a
            s.push(result)
        
           
    return s.pop()
    
def stack_maze(maze):
    """
    -------------------------------------------------------
    Solves a maze using Depth-First search.
    Use: path = stack_maze(maze)
    -------------------------------------------------------
    Parameters:
        maze - dictionary of points in a maze, where each point
            represents a corridor end or a branch. Dictionary
            keys are the name of the point followed by a list of
            branches, if any. First point is named 'Start', exit
            is named 'X' (dict)
    Returns:
        path - list of points visited before the exit is reached,
            None if there is no exit (list of str)
    -------------------------------------------------------
    maze = {'Start': ['A'], 'A':['C', 'B'], 
        'B':[], 'C':['D', 'X']}
    """
    
    
    # initalize two different lists
    visited = []
    stack = Stack()
    current = "Start"
    stack.push(current)
   
   
    # stack = start
    # stack =  b c  start
    # current = b
    # VISITED a B 
    # visited a b 
    # current = c
    # stack = x c
    # current = x 
    # visitd ab c x
    
    
    while not stack.is_empty():
        current = stack.pop()
        visited.append(current)
        
        if current == "X":
            break
        
        for branch in maze.get(current, []):
            if branch not in visited:
                stack.push(branch)
        
        
        
        
        
        
        
    return visited










# Imports
from enum import Enum

# Enumerated constant
MIRRORED = Enum('MIRRORED',
                {'IS_MIRRORED': "is a mirror", 'TOO_MANY_LEFT': "too many characters in L",
                 'TOO_MANY_RIGHT': "too many characters in R", 'MISMATCHED': "L and R don't match",
                 'INVALID_CHAR': "invalid character", 'NOT_MIRRORED': "no mirror character"})

def is_mirror_stack(string, valid_chars, m):
    """
    -------------------------------------------------------
    Determines if string is a mirror of characters in valid_chars around the pivot m.
    A mirror is of the form LmR, where L is the reverse of R, and L and R
    contain only characters in valid_chars.
    Use: mirror = is_mirror_stack(string, valid_chars, m)
    -------------------------------------------------------
    Parameters:
        string - a string (str)
        valid_chars - a string of valid characters (str)
        m - the mirror pivot string (str - one character not in valid_chars)
    Returns:
        mirror - the state of the string (Enum MIRRORED)
    -------------------------------------------------------
    """
    
    assert m not in valid_chars, \
        f"cannot use '{m}' as the mirror character"
    
    mirror = MIRRORED.IS_MIRRORED
    stack = Stack()
    n = len(string)
    i = 0
    
    while i < n and string[i] != m:
        if string[i] in valid_chars:
            stack.push(string[i])
            i += 1
        else:
            mirror = MIRRORED.INVALID_CHAR
    
    # skip  the mirror char
    i += 1
    
    while mirror and MIRRORED.IS_MIRRORED and i < n and not stack.is_empty():
        c = stack.pop()
            
        if string[i] != c:
            mirror = MIRRORED.MISTMACH
        else:
            i += 1
    
    # if its less than n that means we have too many right 
    if i < n:
        mirror = MIRRORED.TOO_MANY_RIGHT
    # if stack not empty too many lefts
    elif not stack.is_empty():
        mirror = MIRRORED.TOO_MANY_LEFT
            
    return mirror
        
        
        
        
    
    
    