"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
Section: CP164 B
__updated__ = "2023-01-13"
-------------------------------------------------------
"""

def clean_list(values):
    """
    -------------------------------------------------------
    Removes all duplicate values from a list: values contains
    only one copy of each of its integers. The order of values
    must be preserved.
    Use: clean_list(values)
    -------------------------------------------------------
    Parameters:
        values - a list of integers (list of int)
    Returns:
        None
    -------------------------------------------------------
    """
    
    new_list = []
    for i in values:
        if i not in new_list:
            new_list.append(i)
    return new_list



def file_analyze(fv):
    """
    -------------------------------------------------------
    Analyzes the characters in a file.
    The contents of the file must be unchanged.
    Use: u, l, d, w, r = file_analyze(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file reference (file variable)
    Returns:
        u - the number of uppercase letters in the file (int)
        l - the number of lowercase letters in the file (int)
        d - the number of digits in the file (int)
        w - the number of whitespace characters in the file (int)
        r - the number of remaining characters in the file (int)
    -------------------------------------------------------
    """
    u = 0
    l = 0
    d = 0 
    w = 0
    r = 0
    for line in fv:
        for letter in line:
            if letter.isupper():
                u = u + 1
            elif letter.islower():
                l = l + 1
            elif letter.isdigit():
                d = d + 1
            elif letter.isspace():
                w = w + 1
            else:
                r = r + 1
            
    return u, l, d, w, r



def find_subs(string, sub):
    """
    -------------------------------------------------------
    Finds the indices of the locations of sub within string,
        left to right.
    Use: locations = find_subs(string, sub)
    -------------------------------------------------------
    Parameters:
        string - a string to evaluate (str)
        sub - a substring to locate in string (str)
    Returns:
        locations - an ordered list of the indices of the locations
            of sub within string (list of int)
    -------------------------------------------------------
    """
    locations = []
    i = string.find(sub)
    while i >= 0:
        locations.append(i)
        i = string.find(sub, i+1)
        
    
    return locations
    
    
def is_leap_year(year):
    """
    -------------------------------------------------------
    Leap year determination.
    Use: leap_year = is_leap_year(year)
    -------------------------------------------------------
    Parameters:
        year - year to determine if it is a leap year (int > 0)
    Returns:
        leap_year - True if year is a leap year, False otherwise (boolean)
    -------------------------------------------------------
    """
    
    x = False
    if( year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
        x = True
    return x
    
    
def is_valid(name):
    """
    -------------------------------------------------------
    Determines if name is a valid Python variable name.
    Variables names must start with a letter or an underscore.
    The rest of the variable name may consist of letters, numbers
    and underscores.
    Use: valid = is_valid(name)
    -------------------------------------------------------
    Parameters:
        name - a string to test as a Python variable name (str)
    Returns:
        valid - True if name is a valid Python variable name,
            False otherwise (boolean)
    -------------------------------------------------------
    """
    valid = True
    if len(name) == 0:
        valid = False
    
    s = name[0]
    
    if not s.isalpha() or s == '_':
        valid = False
        
    for each in name[1:]:
        if not each.isalnum() or each == "_":
            valid = False
                
    return valid
    
def matrix_transpose(a):
    """
    -------------------------------------------------------
    Transpose the contents of matrix a.
    Use: b = matrix_transpose(a):
    -------------------------------------------------------
    Parameters:
        a - a 2D list (list of lists of ?)
    Returns:
        b - the transposed matrix (list of lists of ?)
    -------------------------------------------------------
    """
    
    # initlaize new matrix 
    b = []

    
    # store the num of rows in a
    rows = len(a)
    
   
    
    for i in range(len(a[0])):
        # new list
        z = []
        for j in range(rows):
            z.append(a[j][i])
        # append z to b
        b.append(z)
        
    return b
    
    
def pig_latin(word):
    """
    -------------------------------------------------------
    Converts a word to Pig Latin. The conversion is:
    - if a word begins with a vowel, add "way" to the end of the word.
    - if the word begins with consonants, move the leading consonants to
    the end of the word and add "ay" to the end of that.
    "y" is treated as a consonant if it is the first character in the word,
    and as a vowel for anywhere else in the word.
    Preserve the case of the word - i.e. if the first character of word
    is upper-case, then the new first character should also be upper case.
    Use: pl = pig_latin(word)
    -------------------------------------------------------
    Parameters:
        word - a string to convert to Pig Latin (str)
    Returns:
        pl - the Pig Latin version of word (str)
    ------------------------------------------------------
    """
    VOWELS = ['A','E','I','O','U','a','e','i','o','u']
    pl = ""
    capital = False
    
    # check to see if its upper or lower case
    # ad on way t oend of the word if begins with vowel
    
    
    if word[0].isupper():
        capital = True
        
    if word[0] in VOWELS:
        pl += word + "way"
    
    
    elif not word[0] in VOWELS:
        if capital == True:
            pl += word[1].upper() +word[2:].lower() + word[0].lower() + "ay"
        else:
            pl += word[1:].lower() + word[0].lower() + "ay"

    return pl



def matrixes_multiply(a, b):
    """
    -------------------------------------------------------
    Multiplies the contents of matrixes a and b.
    If a is mxn in size, and b is nxp in size, then c is mxp.
    a and b must be unchanged.
    Use: c = matrixes_multiply(a, b)
    -------------------------------------------------------
    Parameters:
        a - a 2D list (2D list of int/float)
        b - a 2D list (2D list of int/float)
    Returns:
        c - the matrix multiple of a and b (2D list of int/float)
    -------------------------------------------------------
    """
    
    
    
    new = list(zip(a,b))
    c = []
    for i in range(len(new)):
        row = []
        for j in range(len(new[0])):
            row.append(0)
        c.append(row)
     
     
    for i in range(len(a)):   
        # row for mat a 
        for j in range(len(b[0])): 
            # col for b matrix 
            for k in range(len(b)): 
                # finds the row for matrix a
                c[i][j] += a[i][k] * b[k][j]  
        
    
    
    return c
            
        
    
    
    
def shift(string, n):
    """
    -------------------------------------------------------
    Encipher a string using a shift cipher.
    Only letters are enciphered, and the returned string is
    in upper case.
    Use: estring = shift(string, n):
    -------------------------------------------------------
    Parameters:
        string - string to encipher (str)
        n - the number of letters to shift (int)
    Returns:
        estring - the enciphered string (str)
    -------------------------------------------------------
    """
    estring = ""
    for each in string:
        if each.isalpha():
            each = each.upper()
            estring += chr((ord(each) + n - 65) % 26 + 65)
    return estring
    
    
    
    
    