Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree1/binarySearchTree1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 67
 - Location sample coverage: 14.93 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.429309
 - Clean trial 2 run time: 0:00:00.301962
 - Mutation trials total run time: 0:00:12.376355

Overall mutation trial summary
==============================
 - DETECTED: 23
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-06 00:04:44.461137


Mutations by result status
==========================


DETECTED
--------
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 35, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree1.py: (l: 35, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree1.py: (l: 35, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree1.py: (l: 35, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree1.py: (l: 35, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree1.py: (l: 64, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 64, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 86, c: 20) - mutation from None to False
 - binarySearchTree1.py: (l: 86, c: 20) - mutation from None to True
 - binarySearchTree1.py: (l: 90, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 90, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 102, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 111, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 111, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 136, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree1.py: (l: 136, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree1.py: (l: 136, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 136, c: 24) - mutation from None to False
 - binarySearchTree1.py: (l: 161, c: 24) - mutation from None to True
 - binarySearchTree1.py: (l: 161, c: 24) - mutation from None to False