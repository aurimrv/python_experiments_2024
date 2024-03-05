Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack3/stack3.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 23
 - Location sample coverage: 43.48 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.224892
 - Clean trial 2 run time: 0:00:00.215974
 - Mutation trials total run time: 0:00:07.296859

Overall mutation trial summary
==============================
 - DETECTED: 13
 - SURVIVED: 10
 - TIMEOUT: 2
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-07-14 00:10:26.926961


Mutations by result status
==========================


SURVIVED
--------
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_True
 - stack3.py: (l: 103, c: 32) - mutation from None to False
 - stack3.py: (l: 103, c: 32) - mutation from None to True
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack3.py: (l: 140, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


TIMEOUT
-------
 - stack3.py: (l: 24, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 24, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>


DETECTED
--------
 - stack3.py: (l: 40, c: 8) - mutation from If_Statement to If_False
 - stack3.py: (l: 42, c: 35) - mutation from None to True
 - stack3.py: (l: 42, c: 35) - mutation from None to False
 - stack3.py: (l: 75, c: 15) - mutation from True to False
 - stack3.py: (l: 75, c: 15) - mutation from True to None
 - stack3.py: (l: 75, c: 45) - mutation from False to None
 - stack3.py: (l: 75, c: 45) - mutation from False to True
 - stack3.py: (l: 125, c: 15) - mutation from True to False
 - stack3.py: (l: 125, c: 15) - mutation from True to None
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack3.py: (l: 125, c: 23) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>