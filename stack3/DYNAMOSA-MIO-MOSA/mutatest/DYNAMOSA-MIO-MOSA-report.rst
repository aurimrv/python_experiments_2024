Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 24
 - Location sample coverage: 41.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.286543
 - Clean trial 2 run time: 0:00:00.236983
 - Mutation trials total run time: 0:00:07.089104

Overall mutation trial summary
==============================
 - DETECTED: 14
 - SURVIVED: 7
 - TIMEOUT: 1
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-06 00:07:32.866177


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 19, c: 31) - mutation from None to False
 - stack3.py: (l: 19, c: 31) - mutation from None to True
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 39, c: 19) - mutation from None to True
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_True
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_False


TIMEOUT
-------
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - stack3.py: (l: 15, c: 31) - mutation from None to True
 - stack3.py: (l: 15, c: 31) - mutation from None to False
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 75, c: 45) - mutation from False to True
 - stack3.py: (l: 75, c: 45) - mutation from False to None
 - stack3.py: (l: 125, c: 15) - mutation from True to None
 - stack3.py: (l: 125, c: 15) - mutation from True to False
 - stack3.py: (l: 125, c: 56) - mutation from False to None
 - stack3.py: (l: 125, c: 56) - mutation from False to True