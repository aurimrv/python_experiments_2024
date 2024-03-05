Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTMUT']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 32
 - Total locations identified: 32
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.408173
 - Clean trial 2 run time: 0:00:00.362200
 - Mutation trials total run time: 0:00:49.909763

Overall mutation trial summary
==============================
 - SURVIVED: 10
 - DETECTED: 101
 - TIMEOUT: 3
 - TOTAL RUNS: 114
 - RUN DATETIME: 2024-03-04 11:07:45.709437


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>


TIMEOUT
-------
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - sort1.py: (l: 31, c: 18) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 31, c: 34) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Sub'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Add'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Div'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Pow'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mod'>
 - sort1.py: (l: 45, c: 15) - mutation from <class 'ast.FloorDiv'> to <class 'ast.Mult'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_Unbounded
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - sort1.py: (l: 66, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 82, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 85, c: 40) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 92, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 92, c: 15) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Sub
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Mult