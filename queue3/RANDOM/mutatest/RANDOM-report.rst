Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './RANDOM']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:13.088892
 - Clean trial 2 run time: 0:00:01.810456
 - Mutation trials total run time: 0:01:12.927962

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 12
 - TOTAL RUNS: 35
 - RUN DATETIME: 2023-07-13 23:59:36.130324


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 30, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 66, c: 32) - mutation from None to False
 - queue3.py: (l: 66, c: 32) - mutation from None to True
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 74, c: 32) - mutation from None to False
 - queue3.py: (l: 74, c: 32) - mutation from None to True
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 83, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 106, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>