Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.303790
 - Clean trial 2 run time: 0:00:00.233885
 - Mutation trials total run time: 0:00:09.459805

Overall mutation trial summary
==============================
 - DETECTED: 28
 - SURVIVED: 5
 - TOTAL RUNS: 33
 - RUN DATETIME: 2023-03-06 00:06:05.777646


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 30, c: 28) - mutation from None to False
 - linkedList4.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Add


DETECTED
--------
 - linkedList4.py: (l: 30, c: 28) - mutation from None to True
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList4.py: (l: 85, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList4.py: (l: 85, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList4.py: (l: 85, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper