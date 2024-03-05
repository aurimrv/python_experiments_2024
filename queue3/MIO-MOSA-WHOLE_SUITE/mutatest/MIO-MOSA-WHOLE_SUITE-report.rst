Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.354725
 - Clean trial 2 run time: 0:00:00.239869
 - Mutation trials total run time: 0:00:08.123165

Overall mutation trial summary
==============================
 - DETECTED: 18
 - SURVIVED: 10
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-06 09:34:24.219054


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 88, c: 35) - mutation from None to False
 - queue3.py: (l: 88, c: 35) - mutation from None to True
 - queue3.py: (l: 113, c: 19) - mutation from None to False
 - queue3.py: (l: 113, c: 19) - mutation from None to True
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 38, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - queue3.py: (l: 49, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 106, c: 15) - mutation from True to False
 - queue3.py: (l: 106, c: 15) - mutation from True to None
 - queue3.py: (l: 106, c: 45) - mutation from False to None
 - queue3.py: (l: 106, c: 45) - mutation from False to True