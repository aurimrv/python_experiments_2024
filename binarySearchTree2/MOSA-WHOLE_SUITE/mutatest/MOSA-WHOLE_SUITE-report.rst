Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.292996
 - Clean trial 2 run time: 0:00:00.239771
 - Mutation trials total run time: 0:00:06.785273

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 6
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-06 14:07:28.589733


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 97, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree2.py: (l: 157, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 157, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 166, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree2.py: (l: 19, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 19, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to None
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to False
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree2.py: (l: 69, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree2.py: (l: 145, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 145, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 166, c: 8) - mutation from If_Statement to If_True