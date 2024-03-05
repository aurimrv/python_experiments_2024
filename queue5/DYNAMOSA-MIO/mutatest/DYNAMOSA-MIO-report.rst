Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue5/queue5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 20
 - Location sample coverage: 50.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.945592
 - Clean trial 2 run time: 0:00:00.994162
 - Mutation trials total run time: 0:00:21.070083

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 5
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-05 12:25:54.180341


Mutations by result status
==========================


SURVIVED
--------
 - queue5.py: (l: 5, c: 20) - mutation from None to False
 - queue5.py: (l: 5, c: 20) - mutation from None to True
 - queue5.py: (l: 26, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 27, c: 19) - mutation from None to False
 - queue5.py: (l: 27, c: 19) - mutation from None to True


DETECTED
--------
 - queue5.py: (l: 11, c: 20) - mutation from None to True
 - queue5.py: (l: 11, c: 20) - mutation from None to False
 - queue5.py: (l: 12, c: 20) - mutation from None to True
 - queue5.py: (l: 12, c: 20) - mutation from None to False
 - queue5.py: (l: 17, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 17, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 17, c: 24) - mutation from None to True
 - queue5.py: (l: 17, c: 24) - mutation from None to False
 - queue5.py: (l: 26, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 26, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 32, c: 24) - mutation from None to False
 - queue5.py: (l: 32, c: 24) - mutation from None to True