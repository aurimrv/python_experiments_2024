Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 49
 - Location sample coverage: 20.41 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.246322
 - Clean trial 2 run time: 0:00:00.213585
 - Mutation trials total run time: 0:00:05.604777

Overall mutation trial summary
==============================
 - SURVIVED: 8
 - DETECTED: 17
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-07-14 00:09:56.195225


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 84, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 101, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 103, c: 21) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 152, c: 19) - mutation from None to True
 - queue4.py: (l: 152, c: 19) - mutation from None to False


DETECTED
--------
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 75, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - queue4.py: (l: 75, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - queue4.py: (l: 75, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - queue4.py: (l: 84, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 88, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 99, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - queue4.py: (l: 101, c: 16) - mutation from If_Statement to If_True