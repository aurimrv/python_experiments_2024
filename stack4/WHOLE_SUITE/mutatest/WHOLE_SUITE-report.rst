Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 22
 - Location sample coverage: 45.45 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.214848
 - Clean trial 2 run time: 0:00:00.196415
 - Mutation trials total run time: 0:00:05.094947

Overall mutation trial summary
==============================
 - SURVIVED: 12
 - DETECTED: 13
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-07-14 00:17:20.358474


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 44, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 101, c: 28) - mutation from None to False
 - stack4.py: (l: 101, c: 28) - mutation from None to True


DETECTED
--------
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 37, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 70, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - stack4.py: (l: 74, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>