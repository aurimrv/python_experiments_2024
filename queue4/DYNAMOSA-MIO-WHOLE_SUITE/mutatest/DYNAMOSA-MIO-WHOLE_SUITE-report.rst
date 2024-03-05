Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue4/queue4.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.336751
 - Clean trial 2 run time: 0:00:00.249997
 - Mutation trials total run time: 0:00:08.266908

Overall mutation trial summary
==============================
 - DETECTED: 24
 - SURVIVED: 3
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-12 11:35:06.133708


Mutations by result status
==========================


SURVIVED
--------
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_False
 - queue4.py: (l: 102, c: 59) - mutation from None to False


DETECTED
--------
 - queue4.py: (l: 33, c: 20) - mutation from None to False
 - queue4.py: (l: 33, c: 20) - mutation from None to True
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue4.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 63, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 64, c: 24) - mutation from None to True
 - queue4.py: (l: 64, c: 24) - mutation from None to False
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - queue4.py: (l: 73, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Add
 - queue4.py: (l: 87, c: 8) - mutation from AugAssign_Sub to AugAssign_Div
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_True
 - queue4.py: (l: 96, c: 12) - mutation from If_Statement to If_False
 - queue4.py: (l: 98, c: 43) - mutation from None to False
 - queue4.py: (l: 98, c: 43) - mutation from None to True
 - queue4.py: (l: 99, c: 16) - mutation from If_Statement to If_True
 - queue4.py: (l: 102, c: 59) - mutation from None to True