Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.342722
 - Clean trial 2 run time: 0:00:00.234010
 - Mutation trials total run time: 0:00:06.143442

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 5
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-06 14:08:49.600108


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 40, c: 37) - mutation from None to True
 - queue3.py: (l: 40, c: 37) - mutation from None to False
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 97, c: 28) - mutation from None to True
 - queue3.py: (l: 97, c: 28) - mutation from None to False


DETECTED
--------
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 75, c: 32) - mutation from None to False
 - queue3.py: (l: 75, c: 32) - mutation from None to True
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 106, c: 15) - mutation from True to False
 - queue3.py: (l: 106, c: 15) - mutation from True to None
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 112, c: 8) - mutation from If_Statement to If_False