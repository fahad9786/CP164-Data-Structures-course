"""
-------------------------------------------------------
[program description]
-------------------------------------------------------
Author:  Fahad Sheikh
ID:      169031080
Email:   shei1080@mylaurier.ca
__updated__ = "2023-02-05"
-------------------------------------------------------
"""

from functions import stack_maze
maze = {'Start': ['A'], 'A':['C', 'B'], 
        'B':[], 'C':['D', 'X']}
path = stack_maze(maze)
print(path)