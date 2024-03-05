Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 69
 - Location sample coverage: 14.49 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:20.448149
 - Clean trial 2 run time: 0:00:03.344090
 - Mutation trials total run time: 0:01:03.959307

Overall mutation trial summary
==============================
 - SURVIVED: 14
 - DETECTED: 13
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-07-13 23:45:00.855148


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to True
 - binarySearchTree2.py: (l: 89, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 89, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to True
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to False
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to False
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to False
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to True
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 35, c: 29) - mutation from None to False
 - binarySearchTree2.py: (l: 35, c: 29) - mutation from None to True
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to True
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Mult