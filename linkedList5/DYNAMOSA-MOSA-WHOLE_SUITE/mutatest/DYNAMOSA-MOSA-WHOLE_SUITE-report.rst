Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 55
 - Location sample coverage: 18.18 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.726496
 - Clean trial 2 run time: 0:00:00.299560
 - Mutation trials total run time: 0:00:09.361305

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 5
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-12 12:47:44.510778


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 33, c: 19) - mutation from None to False
 - linkedList5.py: (l: 33, c: 19) - mutation from None to True
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 32, c: 19) - mutation from None to False
 - linkedList5.py: (l: 32, c: 19) - mutation from None to True
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 45, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 48, c: 31) - mutation from None to False
 - linkedList5.py: (l: 48, c: 31) - mutation from None to True
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 52, c: 15) - mutation from None to True
 - linkedList5.py: (l: 52, c: 15) - mutation from None to False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_True