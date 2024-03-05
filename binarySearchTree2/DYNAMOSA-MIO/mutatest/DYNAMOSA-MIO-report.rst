Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:01.583181
 - Clean trial 2 run time: 0:00:01.173964
 - Mutation trials total run time: 0:00:43.920062

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 8
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 12:16:54.290849


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 28, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 97, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 97, c: 28) - mutation from None to False
 - binarySearchTree2.py: (l: 97, c: 28) - mutation from None to True
 - binarySearchTree2.py: (l: 104, c: 23) - mutation from None to False
 - binarySearchTree2.py: (l: 104, c: 23) - mutation from None to True


DETECTED
--------
 - binarySearchTree2.py: (l: 10, c: 20) - mutation from None to False
 - binarySearchTree2.py: (l: 10, c: 20) - mutation from None to True
 - binarySearchTree2.py: (l: 28, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 28, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 28, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 28, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - binarySearchTree2.py: (l: 37, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 48, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 124, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - binarySearchTree2.py: (l: 132, c: 12) - mutation from AugAssign_Add to AugAssign_Div