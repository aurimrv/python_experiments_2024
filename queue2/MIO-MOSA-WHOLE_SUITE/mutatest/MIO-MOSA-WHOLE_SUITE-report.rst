Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.385701
 - Clean trial 2 run time: 0:00:00.261985
 - Mutation trials total run time: 0:00:08.762835

Overall mutation trial summary
==============================
 - SURVIVED: 6
 - DETECTED: 17
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-06 09:34:15.242536


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_True
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 103, c: 24) - mutation from None to False
 - queue2.py: (l: 103, c: 24) - mutation from None to True
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - queue2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 16, c: 39) - mutation from False to None
 - queue2.py: (l: 16, c: 39) - mutation from False to True
 - queue2.py: (l: 22, c: 15) - mutation from False to None
 - queue2.py: (l: 22, c: 15) - mutation from False to True
 - queue2.py: (l: 47, c: 19) - mutation from None to False
 - queue2.py: (l: 47, c: 19) - mutation from None to True
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_False
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 120, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 129, c: 19) - mutation from None to False
 - queue2.py: (l: 129, c: 19) - mutation from None to True