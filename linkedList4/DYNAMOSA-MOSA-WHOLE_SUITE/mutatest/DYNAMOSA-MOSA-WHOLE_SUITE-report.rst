Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList4/linkedList4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.307859
 - Clean trial 2 run time: 0:00:00.234640
 - Mutation trials total run time: 0:00:08.355006

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 8
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-12 12:47:33.854118


Mutations by result status
==========================


SURVIVED
--------
 - linkedList4.py: (l: 30, c: 28) - mutation from None to False
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 73, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 77, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - linkedList4.py: (l: 77, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - linkedList4.py: (l: 77, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult


DETECTED
--------
 - linkedList4.py: (l: 30, c: 28) - mutation from None to True
 - linkedList4.py: (l: 33, c: 20) - mutation from None to False
 - linkedList4.py: (l: 33, c: 20) - mutation from None to True
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 38, c: 12) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - linkedList4.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 75, c: 12) - mutation from If_Statement to If_True
 - linkedList4.py: (l: 75, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 85, c: 23) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - linkedList4.py: (l: 87, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>