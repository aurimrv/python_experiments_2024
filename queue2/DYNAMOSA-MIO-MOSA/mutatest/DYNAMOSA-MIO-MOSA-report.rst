Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.435627
 - Clean trial 2 run time: 0:00:00.279705
 - Mutation trials total run time: 0:00:09.509804

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 2
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-06 00:06:40.293487


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 21, c: 12) - mutation from If_Statement to If_False


DETECTED
--------
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - queue2.py: (l: 21, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 37, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 90, c: 36) - mutation from None to False
 - queue2.py: (l: 90, c: 36) - mutation from None to True
 - queue2.py: (l: 91, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 91, c: 24) - mutation from None to False
 - queue2.py: (l: 91, c: 24) - mutation from None to True
 - queue2.py: (l: 120, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Div