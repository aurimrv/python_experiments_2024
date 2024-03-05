Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.351993
 - Clean trial 2 run time: 0:00:00.243724
 - Mutation trials total run time: 0:00:08.616910

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 6
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 22:21:25.125291


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 11, c: 20) - mutation from None to True
 - queue3.py: (l: 11, c: 20) - mutation from None to False
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 113, c: 19) - mutation from None to True
 - queue3.py: (l: 113, c: 19) - mutation from None to False


DETECTED
--------
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 75, c: 32) - mutation from None to False
 - queue3.py: (l: 75, c: 32) - mutation from None to True
 - queue3.py: (l: 76, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 76, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 76, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 87, c: 32) - mutation from None to False
 - queue3.py: (l: 87, c: 32) - mutation from None to True