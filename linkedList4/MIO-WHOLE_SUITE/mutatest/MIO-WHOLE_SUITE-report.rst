Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.246829
 - Clean trial 2 run time: 0:00:00.209558
 - Mutation trials total run time: 0:00:06.955629

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 6
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-09 23:55:48.476344


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 10, c: 39) - mutation from None to False
 - linkedList4.py: (l: 10, c: 39) - mutation from None to True
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList4.py: (l: 33, c: 20) - mutation from None to True
 - linkedList4.py: (l: 33, c: 20) - mutation from None to False
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 53, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList4.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 71, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>