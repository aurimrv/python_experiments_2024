Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.648266
 - Clean trial 2 run time: 0:00:01.269809
 - Mutation trials total run time: 0:00:31.298592

Overall mutation trial summary
==============================
 - SURVIVED: 12
 - DETECTED: 12
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-05 12:24:49.846606


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 11, c: 20) - mutation from None to True
 - queue3.py: (l: 11, c: 20) - mutation from None to False
 - queue3.py: (l: 21, c: 37) - mutation from None to True
 - queue3.py: (l: 21, c: 37) - mutation from None to False
 - queue3.py: (l: 62, c: 19) - mutation from None to True
 - queue3.py: (l: 62, c: 19) - mutation from None to False
 - queue3.py: (l: 65, c: 35) - mutation from None to False
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 168, c: 35) - mutation from None to False
 - queue3.py: (l: 168, c: 35) - mutation from None to True


DETECTED
--------
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 65, c: 35) - mutation from None to True
 - queue3.py: (l: 74, c: 32) - mutation from None to True
 - queue3.py: (l: 74, c: 32) - mutation from None to False
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 87, c: 32) - mutation from None to False
 - queue3.py: (l: 87, c: 32) - mutation from None to True