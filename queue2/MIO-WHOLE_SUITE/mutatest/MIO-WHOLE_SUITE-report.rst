Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.322102
 - Clean trial 2 run time: 0:00:00.234643
 - Mutation trials total run time: 0:00:06.043040

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 4
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-09 23:56:11.413067


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 107, c: 24) - mutation from None to True
 - queue2.py: (l: 107, c: 24) - mutation from None to False
 - queue2.py: (l: 120, c: 24) - mutation from None to True
 - queue2.py: (l: 120, c: 24) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 7, c: 37) - mutation from None to True
 - queue2.py: (l: 7, c: 37) - mutation from None to False
 - queue2.py: (l: 16, c: 39) - mutation from False to None
 - queue2.py: (l: 16, c: 39) - mutation from False to True
 - queue2.py: (l: 49, c: 27) - mutation from None to True
 - queue2.py: (l: 49, c: 27) - mutation from None to False
 - queue2.py: (l: 55, c: 15) - mutation from False to None
 - queue2.py: (l: 55, c: 15) - mutation from False to True
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 60, c: 19) - mutation from None to False
 - queue2.py: (l: 60, c: 19) - mutation from None to True
 - queue2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 91, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 91, c: 8) - mutation from If_Statement to If_False