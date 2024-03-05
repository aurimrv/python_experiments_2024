Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 116
 - Location sample coverage: 8.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.458184
 - Clean trial 2 run time: 0:00:00.301583
 - Mutation trials total run time: 0:00:08.110356

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 14
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-06 11:44:11.157562


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 102, c: 16) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 102, c: 16) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 173, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to False
 - binarySearchTree3.py: (l: 376, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 376, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 70, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 96, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 98, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - binarySearchTree3.py: (l: 256, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 256, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to True
 - binarySearchTree3.py: (l: 328, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 328, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 342, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 342, c: 8) - mutation from If_Statement to If_False