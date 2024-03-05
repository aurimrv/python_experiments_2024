Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 50
 - Location sample coverage: 20.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.220572
 - Clean trial 2 run time: 0:00:01.125960
 - Mutation trials total run time: 0:00:36.972751

Overall mutation trial summary
==============================
 - DETECTED: 11
 - SURVIVED: 7
 - TOTAL RUNS: 18
 - RUN DATETIME: 2023-03-05 18:54:38.462903


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 102, c: 59) - mutation from None to False
 - queue4.py: (l: 102, c: 59) - mutation from None to True
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 114, c: 14) - mutation from True to False
 - queue4.py: (l: 114, c: 14) - mutation from True to None


DETECTED
--------
 - queue4.py: (l: 33, c: 20) - mutation from None to True
 - queue4.py: (l: 33, c: 20) - mutation from None to False
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>