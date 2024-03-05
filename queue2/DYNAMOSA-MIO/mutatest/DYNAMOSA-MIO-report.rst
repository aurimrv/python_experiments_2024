Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.066562
 - Clean trial 2 run time: 0:00:01.282063
 - Mutation trials total run time: 0:00:34.764272

Overall mutation trial summary
==============================
 - SURVIVED: 8
 - DETECTED: 14
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-05 12:24:13.443224


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 21, c: 32) - mutation from True to None
 - queue2.py: (l: 21, c: 32) - mutation from True to False
 - queue2.py: (l: 37, c: 24) - mutation from None to False
 - queue2.py: (l: 37, c: 24) - mutation from None to True
 - queue2.py: (l: 84, c: 20) - mutation from None to False
 - queue2.py: (l: 84, c: 20) - mutation from None to True
 - queue2.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>


DETECTED
--------
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 53, c: 23) - mutation from True to None
 - queue2.py: (l: 53, c: 23) - mutation from True to False
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 114, c: 19) - mutation from None to True
 - queue2.py: (l: 114, c: 19) - mutation from None to False