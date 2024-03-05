Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:01.369710
 - Clean trial 2 run time: 0:00:01.164213
 - Mutation trials total run time: 0:00:39.757607

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 9
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-05 12:28:59.137837


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 9, c: 39) - mutation from None to False
 - stack4.py: (l: 9, c: 39) - mutation from None to True
 - stack4.py: (l: 29, c: 28) - mutation from None to False
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 72, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack4.py: (l: 101, c: 28) - mutation from None to True
 - stack4.py: (l: 101, c: 28) - mutation from None to False


DETECTED
--------
 - stack4.py: (l: 29, c: 28) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to True
 - stack4.py: (l: 32, c: 20) - mutation from None to False
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack4.py: (l: 84, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack4.py: (l: 86, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_Unbounded
 - stack4.py: (l: 86, c: 15) - mutation from Slice_UnboundLower to Slice_UnboundUpper