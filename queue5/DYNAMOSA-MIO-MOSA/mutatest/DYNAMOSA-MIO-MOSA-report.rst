Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue5/queue5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.233497
 - Clean trial 2 run time: 0:00:00.192969
 - Mutation trials total run time: 0:00:03.939761

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 1
 - TOTAL RUNS: 16
 - RUN DATETIME: 2023-03-06 00:07:04.789322


Mutations by result status
==========================


SURVIVED
--------
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>


DETECTED
--------
 - queue5.py: (l: 12, c: 20) - mutation from None to True
 - queue5.py: (l: 12, c: 20) - mutation from None to False
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 17, c: 24) - mutation from None to False
 - queue5.py: (l: 17, c: 24) - mutation from None to True
 - queue5.py: (l: 17, c: 33) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 17, c: 46) - mutation from None to True
 - queue5.py: (l: 17, c: 46) - mutation from None to False
 - queue5.py: (l: 26, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 26, c: 46) - mutation from None to True
 - queue5.py: (l: 26, c: 46) - mutation from None to False
 - queue5.py: (l: 30, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 30, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 32, c: 24) - mutation from None to True
 - queue5.py: (l: 32, c: 24) - mutation from None to False