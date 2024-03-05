Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 39
 - Location sample coverage: 25.64 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.200530
 - Clean trial 2 run time: 0:00:00.195377
 - Mutation trials total run time: 0:00:07.090908

Overall mutation trial summary
==============================
 - DETECTED: 30
 - SURVIVED: 5
 - TOTAL RUNS: 35
 - RUN DATETIME: 2023-07-14 00:13:31.663765


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to None
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>


DETECTED
--------
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 15, c: 19) - mutation from True to False
 - identifier1.py: (l: 15, c: 19) - mutation from True to None
 - identifier1.py: (l: 17, c: 19) - mutation from False to True
 - identifier1.py: (l: 23, c: 8) - mutation from If_Statement to If_True
 - identifier1.py: (l: 23, c: 8) - mutation from If_Statement to If_False
 - identifier1.py: (l: 26, c: 12) - mutation from If_Statement to If_False
 - identifier1.py: (l: 26, c: 12) - mutation from If_Statement to If_True
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - identifier1.py: (l: 39, c: 19) - mutation from False to None
 - identifier1.py: (l: 39, c: 19) - mutation from False to True