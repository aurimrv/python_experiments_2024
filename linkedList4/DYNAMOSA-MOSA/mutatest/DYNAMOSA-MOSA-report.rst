Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 21
 - Location sample coverage: 47.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:02.467929
 - Clean trial 2 run time: 0:00:02.229027
 - Mutation trials total run time: 0:00:41.747960

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 4
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-05 18:48:19.758239


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 10, c: 39) - mutation from None to False
 - linkedList4.py: (l: 10, c: 39) - mutation from None to True
 - linkedList4.py: (l: 30, c: 28) - mutation from None to False
 - linkedList4.py: (l: 64, c: 12) - mutation from If_Statement to If_True


DETECTED
--------
 - linkedList4.py: (l: 30, c: 28) - mutation from None to True
 - linkedList4.py: (l: 33, c: 20) - mutation from None to False
 - linkedList4.py: (l: 33, c: 20) - mutation from None to True
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 71, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList4.py: (l: 75, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList4.py: (l: 85, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList4.py: (l: 85, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList4.py: (l: 85, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded