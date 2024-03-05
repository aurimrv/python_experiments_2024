Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 99
 - Location sample coverage: 10.10 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.579014
 - Clean trial 2 run time: 0:00:00.333476
 - Mutation trials total run time: 0:00:11.526138

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 5
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-12 12:46:42.870441


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 87, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 87, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 150, c: 19) - mutation from None to False
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to False
 - binarySearchTree3.py: (l: 298, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 38, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 45, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 45, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 62, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 88, c: 24) - mutation from None to False
 - binarySearchTree3.py: (l: 88, c: 24) - mutation from None to True
 - binarySearchTree3.py: (l: 150, c: 19) - mutation from None to True
 - binarySearchTree3.py: (l: 264, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree3.py: (l: 264, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 264, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to True
 - binarySearchTree3.py: (l: 298, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 325, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 325, c: 8) - mutation from If_Statement to If_False