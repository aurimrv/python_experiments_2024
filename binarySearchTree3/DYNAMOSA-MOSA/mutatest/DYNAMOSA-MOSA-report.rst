Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:02.733272
 - Clean trial 2 run time: 0:00:02.175289
 - Mutation trials total run time: 0:01:15.268323

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 8
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-05 18:42:55.408560


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 72, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 98, c: 16) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 113, c: 14) - mutation from True to False
 - binarySearchTree3.py: (l: 113, c: 14) - mutation from True to None
 - binarySearchTree3.py: (l: 384, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 384, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 397, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 397, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 70, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 72, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 72, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 72, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 72, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 79, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 79, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 98, c: 16) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 247, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 247, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 262, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree3.py: (l: 262, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree3.py: (l: 262, c: 12) - mutation from AugAssign_Add to AugAssign_Sub