Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:03.499845
 - Clean trial 2 run time: 0:00:02.345103
 - Mutation trials total run time: 0:01:22.581880

Overall mutation trial summary
==============================
 - DETECTED: 24
 - SURVIVED: 5
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-05 18:52:29.942166


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 103, c: 24) - mutation from None to True
 - queue2.py: (l: 103, c: 24) - mutation from None to False
 - queue2.py: (l: 108, c: 24) - mutation from None to True
 - queue2.py: (l: 108, c: 24) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 15, c: 29) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 16, c: 26) - mutation from None to True
 - queue2.py: (l: 16, c: 26) - mutation from None to False
 - queue2.py: (l: 46, c: 15) - mutation from None to True
 - queue2.py: (l: 46, c: 15) - mutation from None to False
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 55, c: 15) - mutation from False to None
 - queue2.py: (l: 55, c: 15) - mutation from False to True
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 76, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 91, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>