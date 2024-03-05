Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.289993
 - Clean trial 2 run time: 0:00:00.235497
 - Mutation trials total run time: 0:00:05.877684

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 9
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-12 12:49:07.733562


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 9, c: 39) - mutation from None to True
 - stack4.py: (l: 9, c: 39) - mutation from None to False
 - stack4.py: (l: 29, c: 28) - mutation from None to False
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 101, c: 28) - mutation from None to True
 - stack4.py: (l: 101, c: 28) - mutation from None to False


DETECTED
--------
 - stack4.py: (l: 29, c: 28) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to False
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper