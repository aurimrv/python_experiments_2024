Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.453266
 - Clean trial 2 run time: 0:00:00.282696
 - Mutation trials total run time: 0:00:07.996640

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 5
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-06 14:07:37.592946


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 29, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 358, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 358, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 394, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 394, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 29, c: 28) - mutation from None to True
 - binarySearchTree3.py: (l: 72, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 72, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 74, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 74, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 74, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 98, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 259, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 264, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 264, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 264, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 288, c: 15) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to False
 - binarySearchTree3.py: (l: 374, c: 28) - mutation from None to True