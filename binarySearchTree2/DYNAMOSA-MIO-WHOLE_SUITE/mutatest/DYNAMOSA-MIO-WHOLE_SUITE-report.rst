Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 69
 - Location sample coverage: 14.49 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.375444
 - Clean trial 2 run time: 0:00:00.271889
 - Mutation trials total run time: 0:00:08.839698

Overall mutation trial summary
==============================
 - SURVIVED: 11
 - DETECTED: 16
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-12 11:33:11.049593


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 34, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 86, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 86, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 92, c: 13) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 169, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree2.py: (l: 11, c: 21) - mutation from None to True
 - binarySearchTree2.py: (l: 11, c: 21) - mutation from None to False
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to False
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to True
 - binarySearchTree2.py: (l: 34, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to None
 - binarySearchTree2.py: (l: 49, c: 19) - mutation from True to False
 - binarySearchTree2.py: (l: 73, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree2.py: (l: 73, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree2.py: (l: 73, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 166, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 169, c: 8) - mutation from If_Statement to If_True