Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.324784
 - Clean trial 2 run time: 0:00:00.239945
 - Mutation trials total run time: 0:00:07.448465

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 4
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 11:45:49.267031


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 105, c: 16) - mutation from AugAssign_Sub to AugAssign_Add


DETECTED
--------
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 46, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 46, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 64, c: 24) - mutation from None to False
 - queue4.py: (l: 64, c: 24) - mutation from None to True
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>