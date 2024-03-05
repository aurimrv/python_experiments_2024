Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 36
 - Location sample coverage: 27.78 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.268807
 - Clean trial 2 run time: 0:00:00.217579
 - Mutation trials total run time: 0:00:05.309541

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 5
 - TOTAL RUNS: 20
 - RUN DATETIME: 2023-03-06 14:08:05.037994


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 37, c: 24) - mutation from None to True
 - linkedList2.py: (l: 37, c: 24) - mutation from None to False
 - linkedList2.py: (l: 66, c: 24) - mutation from None to True
 - linkedList2.py: (l: 66, c: 24) - mutation from None to False


DETECTED
--------
 - linkedList2.py: (l: 15, c: 35) - mutation from None to True
 - linkedList2.py: (l: 15, c: 35) - mutation from None to False
 - linkedList2.py: (l: 16, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 22, c: 15) - mutation from False to True
 - linkedList2.py: (l: 22, c: 15) - mutation from False to None
 - linkedList2.py: (l: 27, c: 21) - mutation from None to False
 - linkedList2.py: (l: 27, c: 21) - mutation from None to True
 - linkedList2.py: (l: 55, c: 15) - mutation from False to True
 - linkedList2.py: (l: 55, c: 15) - mutation from False to None
 - linkedList2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 75, c: 19) - mutation from None to True
 - linkedList2.py: (l: 75, c: 19) - mutation from None to False
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div