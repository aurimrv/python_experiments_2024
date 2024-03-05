Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 116
 - Location sample coverage: 8.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.528368
 - Clean trial 2 run time: 0:00:00.334196
 - Mutation trials total run time: 0:00:06.955266

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 11
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-06 09:32:53.616598


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 59, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 84, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 100, c: 16) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 104, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree3.py: (l: 104, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree3.py: (l: 104, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree3.py: (l: 177, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>


DETECTED
--------
 - binarySearchTree3.py: (l: 6, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 6, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 59, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 84, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 98, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 98, c: 21) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree3.py: (l: 100, c: 16) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 263, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 263, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to False