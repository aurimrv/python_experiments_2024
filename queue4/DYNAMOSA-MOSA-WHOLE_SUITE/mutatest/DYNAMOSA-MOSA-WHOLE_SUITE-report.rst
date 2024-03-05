Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.364844
 - Clean trial 2 run time: 0:00:00.254072
 - Mutation trials total run time: 0:00:07.510951

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 2
 - TOTAL RUNS: 22
 - RUN DATETIME: 2023-03-12 12:48:23.231583


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 60, c: 28) - mutation from None to True
 - queue4.py: (l: 60, c: 28) - mutation from None to False


DETECTED
--------
 - queue4.py: (l: 32, c: 20) - mutation from None to False
 - queue4.py: (l: 32, c: 20) - mutation from None to True
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 39, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 55, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 96, c: 15) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue4.py: (l: 98, c: 49) - mutation from None to True
 - queue4.py: (l: 98, c: 49) - mutation from None to False
 - queue4.py: (l: 99, c: 47) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>