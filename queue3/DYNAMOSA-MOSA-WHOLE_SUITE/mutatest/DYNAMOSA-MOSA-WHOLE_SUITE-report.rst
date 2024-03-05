Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.402212
 - Clean trial 2 run time: 0:00:00.265296
 - Mutation trials total run time: 0:00:11.510421

Overall mutation trial summary
==============================
 - DETECTED: 27
 - SURVIVED: 10
 - TOTAL RUNS: 37
 - RUN DATETIME: 2023-03-12 12:48:14.831154


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 88, c: 35) - mutation from None to False
 - queue3.py: (l: 193, c: 0) - mutation from If_Statement to If_True
 - queue3.py: (l: 193, c: 0) - mutation from If_Statement to If_False


DETECTED
--------
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 88, c: 35) - mutation from None to True
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Add