Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.291261
 - Clean trial 2 run time: 0:00:00.225261
 - Mutation trials total run time: 0:00:07.063357

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 5
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 14:08:57.442045


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue4.py: (l: 102, c: 59) - mutation from None to False
 - queue4.py: (l: 114, c: 14) - mutation from True to None
 - queue4.py: (l: 114, c: 14) - mutation from True to False


DETECTED
--------
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - queue4.py: (l: 50, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 97, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue4.py: (l: 97, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue4.py: (l: 98, c: 43) - mutation from None to True
 - queue4.py: (l: 98, c: 43) - mutation from None to False
 - queue4.py: (l: 99, c: 21) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue4.py: (l: 102, c: 59) - mutation from None to True
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>