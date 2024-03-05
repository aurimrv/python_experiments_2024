Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue2/queue2.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 59
 - Location sample coverage: 16.95 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:33.658158
 - Clean trial 2 run time: 0:00:01.866175
 - Mutation trials total run time: 0:00:58.385317

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 18
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-07-13 23:58:08.035408


Mutations by result status
==========================


SURVIVED
--------
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_False
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - queue2.py: (l: 47, c: 19) - mutation from None to False
 - queue2.py: (l: 47, c: 19) - mutation from None to True
 - queue2.py: (l: 48, c: 12) - mutation from If_Statement to If_True
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - queue2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - queue2.py: (l: 83, c: 20) - mutation from None to False
 - queue2.py: (l: 83, c: 20) - mutation from None to True
 - queue2.py: (l: 91, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 91, c: 8) - mutation from If_Statement to If_False
 - queue2.py: (l: 91, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 103, c: 8) - mutation from If_Statement to If_True
 - queue2.py: (l: 120, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue2.py: (l: 130, c: 12) - mutation from AugAssign_Add to AugAssign_Sub