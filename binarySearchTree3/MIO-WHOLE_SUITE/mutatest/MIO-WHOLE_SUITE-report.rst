Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 98
 - Location sample coverage: 10.20 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.441361
 - Clean trial 2 run time: 0:00:00.299867
 - Mutation trials total run time: 0:00:09.175513

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 6
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-09 23:55:02.691723


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 62, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 84, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 87, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 87, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to False
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to True


DETECTED
--------
 - binarySearchTree3.py: (l: 6, c: 55) - mutation from None to True
 - binarySearchTree3.py: (l: 6, c: 55) - mutation from None to False
 - binarySearchTree3.py: (l: 31, c: 20) - mutation from None to False
 - binarySearchTree3.py: (l: 31, c: 20) - mutation from None to True
 - binarySearchTree3.py: (l: 62, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 84, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 97, c: 49) - mutation from None to False
 - binarySearchTree3.py: (l: 97, c: 49) - mutation from None to True
 - binarySearchTree3.py: (l: 241, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 241, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 241, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 258, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 258, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>