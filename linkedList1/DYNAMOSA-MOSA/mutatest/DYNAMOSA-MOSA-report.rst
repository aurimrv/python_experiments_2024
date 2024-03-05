Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:03.542309
 - Clean trial 2 run time: 0:00:01.426725
 - Mutation trials total run time: 0:00:52.600281

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 2
 - ERROR: 1
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-03-05 18:45:35.403672


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 134, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - linkedList1.py: (l: 53, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 53, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 65, c: 24) - mutation from None to False
 - linkedList1.py: (l: 65, c: 24) - mutation from None to True
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 95, c: 31) - mutation from None to False
 - linkedList1.py: (l: 95, c: 31) - mutation from None to True
 - linkedList1.py: (l: 113, c: 35) - mutation from None to True
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Sub


ERROR
-----
 - linkedList1.py: (l: 180, c: 0) - mutation from If_Statement to If_True