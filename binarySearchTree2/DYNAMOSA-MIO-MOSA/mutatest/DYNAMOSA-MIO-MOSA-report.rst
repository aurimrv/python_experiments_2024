Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree2/binarySearchTree2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.360105
 - Clean trial 2 run time: 0:00:00.264684
 - Mutation trials total run time: 0:00:08.600452

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 5
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 00:04:53.966061


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree2.py: (l: 51, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 104, c: 23) - mutation from None to False
 - binarySearchTree2.py: (l: 104, c: 23) - mutation from None to True
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to False
 - binarySearchTree2.py: (l: 169, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - binarySearchTree2.py: (l: 28, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 28, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to False
 - binarySearchTree2.py: (l: 29, c: 28) - mutation from None to True
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - binarySearchTree2.py: (l: 34, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - binarySearchTree2.py: (l: 51, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree2.py: (l: 51, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree2.py: (l: 51, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree2.py: (l: 51, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree2.py: (l: 59, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to False
 - binarySearchTree2.py: (l: 59, c: 34) - mutation from None to True
 - binarySearchTree2.py: (l: 120, c: 40) - mutation from None to True
 - binarySearchTree2.py: (l: 145, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree2.py: (l: 145, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree2.py: (l: 169, c: 8) - mutation from If_Statement to If_True