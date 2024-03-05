Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.253850
 - Clean trial 2 run time: 0:00:00.221329
 - Mutation trials total run time: 0:00:07.085555

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 4
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-06 11:45:00.144119


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList4.py: (l: 33, c: 20) - mutation from None to True
 - linkedList4.py: (l: 33, c: 20) - mutation from None to False
 - linkedList4.py: (l: 45, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList4.py: (l: 45, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList4.py: (l: 45, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 49, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList4.py: (l: 64, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList4.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 71, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList4.py: (l: 75, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - linkedList4.py: (l: 87, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded