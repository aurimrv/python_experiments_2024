Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:01.818877
 - Clean trial 2 run time: 0:00:01.857773
 - Mutation trials total run time: 0:00:56.414793

Overall mutation trial summary
==============================
 - SURVIVED: 8
 - DETECTED: 22
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-05 18:41:32.579460


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to True
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 92, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree2.py: (l: 11, c: 21) - mutation from None to False
 - binarySearchTree2.py: (l: 11, c: 21) - mutation from None to True
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 51, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 51, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 73, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - binarySearchTree2.py: (l: 73, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - binarySearchTree2.py: (l: 73, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - binarySearchTree2.py: (l: 163, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 163, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 163, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 163, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 163, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 169, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 169, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 169, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 169, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 169, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>