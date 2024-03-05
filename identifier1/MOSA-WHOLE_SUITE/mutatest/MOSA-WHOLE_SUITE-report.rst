Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', './MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.221668
 - Clean trial 2 run time: 0:00:00.214631
 - Mutation trials total run time: 0:00:08.055524

Overall mutation trial summary
==============================
 - DETECTED: 29
 - SURVIVED: 5
 - TOTAL RUNS: 34
 - RUN DATETIME: 2023-03-06 14:07:50.989651


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to None
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 32, c: 35) - mutation from False to None


DETECTED
--------
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 45) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 17, c: 19) - mutation from False to True
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 26, c: 12) - mutation from If_Statement to If_False
 - identifier1.py: (l: 26, c: 12) - mutation from If_Statement to If_True
 - identifier1.py: (l: 32, c: 35) - mutation from False to True
 - identifier1.py: (l: 37, c: 23) - mutation from False to None
 - identifier1.py: (l: 37, c: 23) - mutation from False to True