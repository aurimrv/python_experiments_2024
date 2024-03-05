Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.387811
 - Clean trial 2 run time: 0:00:00.293076
 - Mutation trials total run time: 0:00:13.994831

Overall mutation trial summary
==============================
 - DETECTED: 32
 - SURVIVED: 4
 - TOTAL RUNS: 36
 - RUN DATETIME: 2023-03-05 22:21:15.626468


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 120, c: 24) - mutation from None to True
 - queue2.py: (l: 120, c: 24) - mutation from None to False


DETECTED
--------
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 15, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 99, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 114, c: 19) - mutation from None to False
 - queue2.py: (l: 114, c: 19) - mutation from None to True
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 129, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 129, c: 19) - mutation from None to True
 - queue2.py: (l: 129, c: 19) - mutation from None to False
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Div