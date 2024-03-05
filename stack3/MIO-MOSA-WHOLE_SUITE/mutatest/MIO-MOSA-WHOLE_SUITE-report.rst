Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 24
 - Location sample coverage: 41.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.257268
 - Clean trial 2 run time: 0:00:00.237952
 - Mutation trials total run time: 0:00:08.026498

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 9
 - TOTAL RUNS: 31
 - RUN DATETIME: 2023-03-06 09:35:07.869557


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_False
 - stack3.py: (l: 140, c: 0) - mutation from If_Statement to If_True
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>


DETECTED
--------
 - stack3.py: (l: 15, c: 31) - mutation from None to True
 - stack3.py: (l: 15, c: 31) - mutation from None to False
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - stack3.py: (l: 32, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 38, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 39, c: 19) - mutation from None to True
 - stack3.py: (l: 39, c: 19) - mutation from None to False
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack3.py: (l: 44, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 75, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>