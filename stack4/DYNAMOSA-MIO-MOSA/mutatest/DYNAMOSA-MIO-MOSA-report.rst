Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 22
 - Location sample coverage: 45.45 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.287275
 - Clean trial 2 run time: 0:00:00.238413
 - Mutation trials total run time: 0:00:06.081948

Overall mutation trial summary
==============================
 - SURVIVED: 8
 - DETECTED: 14
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-06 00:07:39.740957


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 9, c: 39) - mutation from None to False
 - stack4.py: (l: 9, c: 39) - mutation from None to True
 - stack4.py: (l: 29, c: 28) - mutation from None to False
 - stack4.py: (l: 48, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 74, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - stack4.py: (l: 29, c: 28) - mutation from None to True
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 48, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 74, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded