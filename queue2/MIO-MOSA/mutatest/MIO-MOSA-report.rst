Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.369446
 - Clean trial 2 run time: 0:00:00.241564
 - Mutation trials total run time: 0:00:12.514496

Overall mutation trial summary
==============================
 - DETECTED: 29
 - SURVIVED: 1
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-06 11:45:32.357954


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_True


DETECTED
--------
 - queue2.py: (l: 15, c: 35) - mutation from None to True
 - queue2.py: (l: 15, c: 35) - mutation from None to False
 - queue2.py: (l: 27, c: 21) - mutation from None to False
 - queue2.py: (l: 27, c: 21) - mutation from None to True
 - queue2.py: (l: 46, c: 15) - mutation from None to False
 - queue2.py: (l: 46, c: 15) - mutation from None to True
 - queue2.py: (l: 49, c: 16) - mutation from If_Statement to If_False
 - queue2.py: (l: 55, c: 15) - mutation from False to None
 - queue2.py: (l: 55, c: 15) - mutation from False to True
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 75, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 83, c: 20) - mutation from None to False
 - queue2.py: (l: 83, c: 20) - mutation from None to True
 - queue2.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 114, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>