Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.294839
 - Clean trial 2 run time: 0:00:00.227784
 - Mutation trials total run time: 0:00:08.084336

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 5
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-06 11:44:02.020067


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 81, c: 38) - mutation from None to False
 - binarySearchTree2.py: (l: 81, c: 38) - mutation from None to True
 - binarySearchTree2.py: (l: 102, c: 31) - mutation from None to True
 - binarySearchTree2.py: (l: 102, c: 31) - mutation from None to False
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 20, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 46, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 46, c: 19) - mutation from None to True
 - binarySearchTree2.py: (l: 47, c: 19) - mutation from False to True
 - binarySearchTree2.py: (l: 47, c: 19) - mutation from False to None
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>