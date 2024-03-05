Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.380832
 - Clean trial 2 run time: 0:00:00.268945
 - Mutation trials total run time: 0:00:07.976991

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 1
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-06 00:07:00.150633


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 30, c: 28) - mutation from None to False


DETECTED
--------
 - queue4.py: (l: 30, c: 28) - mutation from None to True
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 55, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 62, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 80, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 89, c: 24) - mutation from None to False
 - queue4.py: (l: 89, c: 24) - mutation from None to True
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>