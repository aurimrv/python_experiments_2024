Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA-MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 24
 - Location sample coverage: 41.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.238136
 - Clean trial 2 run time: 0:00:00.231575
 - Mutation trials total run time: 0:00:08.430248

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 11
 - TIMEOUT: 2
 - TOTAL RUNS: 26
 - RUN DATETIME: 2023-07-14 00:19:37.124994


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False


TIMEOUT
-------
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_Unbounded
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>