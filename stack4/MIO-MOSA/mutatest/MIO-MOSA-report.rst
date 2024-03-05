Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.247999
 - Clean trial 2 run time: 0:00:00.216642
 - Mutation trials total run time: 0:00:08.379128

Overall mutation trial summary
==============================
 - DETECTED: 24
 - SURVIVED: 8
 - TOTAL RUNS: 32
 - RUN DATETIME: 2023-03-06 11:46:28.133356


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 52, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>


DETECTED
--------
 - stack4.py: (l: 32, c: 20) - mutation from None to False
 - stack4.py: (l: 32, c: 20) - mutation from None to True
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded