Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree4/binarySearchTree4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.239500
 - Clean trial 2 run time: 0:00:00.195688
 - Mutation trials total run time: 0:00:04.849205

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 1
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-03-09 23:55:08.253035


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree4.py: (l: 30, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - binarySearchTree4.py: (l: 5, c: 20) - mutation from None to True
 - binarySearchTree4.py: (l: 5, c: 20) - mutation from None to False
 - binarySearchTree4.py: (l: 6, c: 21) - mutation from None to False
 - binarySearchTree4.py: (l: 6, c: 21) - mutation from None to True
 - binarySearchTree4.py: (l: 7, c: 22) - mutation from None to True
 - binarySearchTree4.py: (l: 7, c: 22) - mutation from None to False
 - binarySearchTree4.py: (l: 18, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 18, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree4.py: (l: 18, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 20, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 27, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - binarySearchTree4.py: (l: 29, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - binarySearchTree4.py: (l: 30, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree4.py: (l: 37, c: 29) - mutation from None to False
 - binarySearchTree4.py: (l: 37, c: 29) - mutation from None to True