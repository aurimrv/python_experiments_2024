Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 39
 - Location sample coverage: 25.64 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.226846
 - Clean trial 2 run time: 0:00:00.222698
 - Mutation trials total run time: 0:00:09.814562

Overall mutation trial summary
==============================
 - SURVIVED: 5
 - DETECTED: 30
 - TIMEOUT: 1
 - TOTAL RUNS: 36
 - RUN DATETIME: 2023-03-06 00:05:24.990362


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to None
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>


TIMEOUT
-------
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 78) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to True
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Div
 - identifier1.py: (l: 34, c: 15) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>