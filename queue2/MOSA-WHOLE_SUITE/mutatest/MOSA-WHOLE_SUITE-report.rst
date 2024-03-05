Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.345898
 - Clean trial 2 run time: 0:00:00.228809
 - Mutation trials total run time: 0:00:06.794551

Overall mutation trial summary
==============================
 - SURVIVED: 6
 - DETECTED: 16
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-06 14:08:42.620772


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 37, c: 24) - mutation from None to True
 - queue2.py: (l: 37, c: 24) - mutation from None to False
 - queue2.py: (l: 66, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 103, c: 24) - mutation from None to False
 - queue2.py: (l: 103, c: 24) - mutation from None to True


DETECTED
--------
 - queue2.py: (l: 22, c: 15) - mutation from False to None
 - queue2.py: (l: 22, c: 15) - mutation from False to True
 - queue2.py: (l: 46, c: 15) - mutation from None to True
 - queue2.py: (l: 46, c: 15) - mutation from None to False
 - queue2.py: (l: 47, c: 19) - mutation from None to False
 - queue2.py: (l: 47, c: 19) - mutation from None to True
 - queue2.py: (l: 66, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 91, c: 24) - mutation from None to False
 - queue2.py: (l: 91, c: 24) - mutation from None to True
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Div