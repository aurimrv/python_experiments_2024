Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree4/binarySearchTree4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 21
 - Location sample coverage: 47.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.264084
 - Clean trial 2 run time: 0:00:00.201187
 - Mutation trials total run time: 0:00:04.812242

Overall mutation trial summary
==============================
 - DETECTED: 16
 - SURVIVED: 2
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-06 09:32:59.162357


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree4.py: (l: 30, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree4.py: (l: 37, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree4.py: (l: 7, c: 22) - mutation from None to True
 - binarySearchTree4.py: (l: 7, c: 22) - mutation from None to False
 - binarySearchTree4.py: (l: 14, c: 28) - mutation from None to True
 - binarySearchTree4.py: (l: 14, c: 28) - mutation from None to False
 - binarySearchTree4.py: (l: 18, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 18, c: 19) - mutation from None to True
 - binarySearchTree4.py: (l: 18, c: 19) - mutation from None to False
 - binarySearchTree4.py: (l: 27, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree4.py: (l: 27, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 27, c: 19) - mutation from None to True
 - binarySearchTree4.py: (l: 27, c: 19) - mutation from None to False
 - binarySearchTree4.py: (l: 30, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 30, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 30, c: 28) - mutation from None to False
 - binarySearchTree4.py: (l: 30, c: 28) - mutation from None to True
 - binarySearchTree4.py: (l: 37, c: 12) - mutation from If_Statement to If_False