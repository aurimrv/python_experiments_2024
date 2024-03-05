Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.381403
 - Clean trial 2 run time: 0:00:00.244540
 - Mutation trials total run time: 0:00:10.084047

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 14
 - TOTAL RUNS: 34
 - RUN DATETIME: 2023-03-06 00:06:51.261301


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 40, c: 37) - mutation from None to False
 - queue3.py: (l: 40, c: 37) - mutation from None to True
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 62, c: 19) - mutation from None to False
 - queue3.py: (l: 62, c: 19) - mutation from None to True
 - queue3.py: (l: 65, c: 35) - mutation from None to False
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 55, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 55, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 55, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 65, c: 35) - mutation from None to True
 - queue3.py: (l: 74, c: 32) - mutation from None to True
 - queue3.py: (l: 74, c: 32) - mutation from None to False
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 91, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>