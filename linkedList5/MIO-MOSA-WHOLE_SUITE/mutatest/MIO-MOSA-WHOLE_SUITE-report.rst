Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.717984
 - Clean trial 2 run time: 0:00:00.260827
 - Mutation trials total run time: 0:00:10.185600

Overall mutation trial summary
==============================
 - DETECTED: 17
 - SURVIVED: 2
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-06 09:34:00.097746


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList5.py: (l: 25, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 57, c: 24) - mutation from None to True
 - linkedList5.py: (l: 57, c: 24) - mutation from None to False
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 80, c: 36) - mutation from None to False
 - linkedList5.py: (l: 80, c: 36) - mutation from None to True
 - linkedList5.py: (l: 88, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 88, c: 31) - mutation from None to False
 - linkedList5.py: (l: 88, c: 31) - mutation from None to True