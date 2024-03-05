Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue5/queue5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.245042
 - Clean trial 2 run time: 0:00:00.202648
 - Mutation trials total run time: 0:00:03.816786

Overall mutation trial summary
==============================
 - DETECTED: 10
 - SURVIVED: 6
 - TOTAL RUNS: 16
 - RUN DATETIME: 2023-03-12 12:48:27.762265


Mutations by result status
==========================


SURVIVED
--------
 - queue5.py: (l: 5, c: 20) - mutation from None to True
 - queue5.py: (l: 5, c: 20) - mutation from None to False
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 26, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue5.py: (l: 27, c: 19) - mutation from None to True
 - queue5.py: (l: 27, c: 19) - mutation from None to False


DETECTED
--------
 - queue5.py: (l: 17, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 17, c: 24) - mutation from None to False
 - queue5.py: (l: 17, c: 24) - mutation from None to True
 - queue5.py: (l: 17, c: 33) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue5.py: (l: 26, c: 24) - mutation from None to False
 - queue5.py: (l: 26, c: 24) - mutation from None to True
 - queue5.py: (l: 30, c: 8) - mutation from If_Statement to If_False
 - queue5.py: (l: 30, c: 8) - mutation from If_Statement to If_True
 - queue5.py: (l: 31, c: 24) - mutation from None to True
 - queue5.py: (l: 31, c: 24) - mutation from None to False