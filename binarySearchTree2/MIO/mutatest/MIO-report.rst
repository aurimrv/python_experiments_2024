Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './MIO']
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
 - Clean trial 1 run time: 0:00:00.245053
 - Clean trial 2 run time: 0:00:00.219237
 - Mutation trials total run time: 0:00:06.214902

Overall mutation trial summary
==============================
 - SURVIVED: 14
 - DETECTED: 13
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-07-14 00:10:54.294758


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to True
 - binarySearchTree2.py: (l: 89, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 89, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to True
 - binarySearchTree2.py: (l: 118, c: 36) - mutation from None to False
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to False
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 186, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>


DETECTED
--------
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to False
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to True
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 29, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 35, c: 29) - mutation from None to False
 - binarySearchTree2.py: (l: 35, c: 29) - mutation from None to True
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to True
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Sub