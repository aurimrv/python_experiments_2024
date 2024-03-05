Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.233672
 - Clean trial 2 run time: 0:00:00.218385
 - Mutation trials total run time: 0:00:08.998019

Overall mutation trial summary
==============================
 - DETECTED: 12
 - SURVIVED: 25
 - TOTAL RUNS: 37
 - RUN DATETIME: 2023-03-06 00:07:14.513233


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>