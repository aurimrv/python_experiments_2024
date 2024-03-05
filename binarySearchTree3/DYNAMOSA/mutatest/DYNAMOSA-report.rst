Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 99
 - Location sample coverage: 10.10 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.370668
 - Clean trial 2 run time: 0:00:00.276635
 - Mutation trials total run time: 0:00:05.749902

Overall mutation trial summary
==============================
 - SURVIVED: 9
 - DETECTED: 11
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-07-14 00:08:45.875341


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 58, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 62, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 100, c: 16) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 102, c: 16) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 102, c: 16) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 159, c: 27) - mutation from None to True
 - binarySearchTree3.py: (l: 159, c: 27) - mutation from None to False
 - binarySearchTree3.py: (l: 298, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 342, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree3.py: (l: 58, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 62, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 100, c: 16) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 239, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 239, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 273, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 273, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 298, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 310, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 310, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 342, c: 8) - mutation from If_Statement to If_False