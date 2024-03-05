Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.341666
 - Clean trial 2 run time: 0:00:00.273532
 - Mutation trials total run time: 0:00:10.273454

Overall mutation trial summary
==============================
 - SURVIVED: 12
 - DETECTED: 23
 - TOTAL RUNS: 35
 - RUN DATETIME: 2023-03-12 11:34:57.016636


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 168, c: 35) - mutation from None to True
 - queue3.py: (l: 168, c: 35) - mutation from None to False
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - queue3.py: (l: 10, c: 20) - mutation from None to False
 - queue3.py: (l: 10, c: 20) - mutation from None to True
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - queue3.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 61, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 63, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 66, c: 32) - mutation from None to False
 - queue3.py: (l: 66, c: 32) - mutation from None to True
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 83, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 85, c: 13) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 106, c: 45) - mutation from False to True
 - queue3.py: (l: 106, c: 45) - mutation from False to None