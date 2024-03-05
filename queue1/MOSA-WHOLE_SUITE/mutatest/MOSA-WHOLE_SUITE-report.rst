Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue1/queue1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 17
 - Location sample coverage: 58.82 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.251924
 - Clean trial 2 run time: 0:00:00.205576
 - Mutation trials total run time: 0:00:04.197413

Overall mutation trial summary
==============================
 - SURVIVED: 5
 - DETECTED: 13
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-06 14:08:34.988811


Mutations by result status
==========================


SURVIVED
--------
 - queue1.py: (l: 11, c: 14) - mutation from None to False
 - queue1.py: (l: 11, c: 14) - mutation from None to True
 - queue1.py: (l: 23, c: 2) - mutation from If_Statement to If_True
 - queue1.py: (l: 45, c: 10) - mutation from None to False
 - queue1.py: (l: 45, c: 10) - mutation from None to True


DETECTED
--------
 - queue1.py: (l: 10, c: 15) - mutation from None to False
 - queue1.py: (l: 10, c: 15) - mutation from None to True
 - queue1.py: (l: 23, c: 2) - mutation from If_Statement to If_False
 - queue1.py: (l: 23, c: 5) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue1.py: (l: 23, c: 19) - mutation from None to False
 - queue1.py: (l: 23, c: 19) - mutation from None to True
 - queue1.py: (l: 35, c: 2) - mutation from If_Statement to If_False
 - queue1.py: (l: 35, c: 2) - mutation from If_Statement to If_True
 - queue1.py: (l: 44, c: 2) - mutation from If_Statement to If_True
 - queue1.py: (l: 44, c: 2) - mutation from If_Statement to If_False
 - queue1.py: (l: 44, c: 5) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue1.py: (l: 56, c: 14) - mutation from None to True
 - queue1.py: (l: 56, c: 14) - mutation from None to False