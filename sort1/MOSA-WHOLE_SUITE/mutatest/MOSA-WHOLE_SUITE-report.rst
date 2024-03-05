Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 32
 - Location sample coverage: 31.25 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.215000
 - Clean trial 2 run time: 0:00:00.208159
 - Mutation trials total run time: 0:00:09.811702

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 17
 - TIMEOUT: 1
 - TOTAL RUNS: 39
 - RUN DATETIME: 2023-03-06 14:09:11.846110


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>


TIMEOUT
-------
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Div'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Add'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mod'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Sub'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Pow'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mult'>
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_Unbounded
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>