Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 77
 - Location sample coverage: 12.99 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.327317
 - Clean trial 2 run time: 0:00:00.246460
 - Mutation trials total run time: 0:00:06.030058

Overall mutation trial summary
==============================
 - DETECTED: 10
 - SURVIVED: 10
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-03-05 22:19:41.489171


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 86, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to True
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 97, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree2.py: (l: 157, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 157, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 186, c: 0) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 186, c: 0) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 23, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to True
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to False
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to True
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to False