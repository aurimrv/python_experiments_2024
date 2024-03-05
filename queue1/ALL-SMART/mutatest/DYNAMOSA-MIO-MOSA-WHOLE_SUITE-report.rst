Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue1/queue1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 17
 - Location sample coverage: 58.82 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.260327
 - Clean trial 2 run time: 0:00:00.211710
 - Mutation trials total run time: 0:00:04.644288

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 4
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-07-14 00:18:55.718265


Mutations by result status
==========================


SURVIVED
--------
 - queue1.py: (l: 11, c: 14) - mutation from None to False
 - queue1.py: (l: 11, c: 14) - mutation from None to True
 - queue1.py: (l: 45, c: 10) - mutation from None to False
 - queue1.py: (l: 45, c: 10) - mutation from None to True


DETECTED
--------
 - queue1.py: (l: 32, c: 2) - mutation from AugAssign_Add to AugAssign_Mult
 - queue1.py: (l: 32, c: 2) - mutation from AugAssign_Add to AugAssign_Div
 - queue1.py: (l: 32, c: 2) - mutation from AugAssign_Add to AugAssign_Sub
 - queue1.py: (l: 35, c: 2) - mutation from If_Statement to If_True
 - queue1.py: (l: 35, c: 2) - mutation from If_Statement to If_False
 - queue1.py: (l: 35, c: 19) - mutation from None to True
 - queue1.py: (l: 35, c: 19) - mutation from None to False
 - queue1.py: (l: 40, c: 3) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue1.py: (l: 40, c: 3) - mutation from AugAssign_Sub to AugAssign_Add
 - queue1.py: (l: 40, c: 3) - mutation from AugAssign_Sub to AugAssign_Div
 - queue1.py: (l: 44, c: 5) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue1.py: (l: 44, c: 19) - mutation from None to True
 - queue1.py: (l: 44, c: 19) - mutation from None to False
 - queue1.py: (l: 50, c: 15) - mutation from None to False
 - queue1.py: (l: 50, c: 15) - mutation from None to True
 - queue1.py: (l: 56, c: 14) - mutation from None to True
 - queue1.py: (l: 56, c: 14) - mutation from None to False