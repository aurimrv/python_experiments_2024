Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 49
 - Location sample coverage: 20.41 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.282806
 - Clean trial 2 run time: 0:00:00.238209
 - Mutation trials total run time: 0:00:06.665278

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 6
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-09 23:56:27.445063


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 88, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 88, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


DETECTED
--------
 - queue4.py: (l: 33, c: 20) - mutation from None to True
 - queue4.py: (l: 33, c: 20) - mutation from None to False
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 80, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 96, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue4.py: (l: 98, c: 43) - mutation from None to True
 - queue4.py: (l: 98, c: 43) - mutation from None to False
 - queue4.py: (l: 99, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - queue4.py: (l: 101, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>