Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.281720
 - Clean trial 2 run time: 0:00:00.239598
 - Mutation trials total run time: 0:00:07.367685

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 8
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-09 23:54:52.511113


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 28, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to True
 - binarySearchTree2.py: (l: 86, c: 19) - mutation from None to False
 - binarySearchTree2.py: (l: 129, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 169, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to True
 - binarySearchTree2.py: (l: 21, c: 26) - mutation from None to False
 - binarySearchTree2.py: (l: 28, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 35, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 35, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 35, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 35, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 35, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 35, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 59, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 67, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 129, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 163, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 163, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 169, c: 8) - mutation from If_Statement to If_True