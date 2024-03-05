Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 50
 - Location sample coverage: 20.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.312858
 - Clean trial 2 run time: 0:00:00.303262
 - Mutation trials total run time: 0:00:08.148841

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 6
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-05 22:21:34.173747


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 30, c: 28) - mutation from None to False
 - queue4.py: (l: 88, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult


DETECTED
--------
 - queue4.py: (l: 30, c: 28) - mutation from None to True
 - queue4.py: (l: 33, c: 20) - mutation from None to False
 - queue4.py: (l: 33, c: 20) - mutation from None to True
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 64, c: 24) - mutation from None to True
 - queue4.py: (l: 64, c: 24) - mutation from None to False
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 88, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 96, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>