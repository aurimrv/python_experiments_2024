Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:02.617050
 - Clean trial 2 run time: 0:00:01.874167
 - Mutation trials total run time: 0:01:18.390688

Overall mutation trial summary
==============================
 - SURVIVED: 7
 - DETECTED: 28
 - TOTAL RUNS: 35
 - RUN DATETIME: 2023-03-05 18:53:55.689370


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 40, c: 37) - mutation from None to False
 - queue3.py: (l: 40, c: 37) - mutation from None to True
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 25, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 63, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 67, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - queue3.py: (l: 99, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - queue3.py: (l: 106, c: 45) - mutation from False to True
 - queue3.py: (l: 106, c: 45) - mutation from False to None