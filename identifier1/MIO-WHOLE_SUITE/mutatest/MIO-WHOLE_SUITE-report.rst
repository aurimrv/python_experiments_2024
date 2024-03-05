Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.212962
 - Clean trial 2 run time: 0:00:00.201495
 - Mutation trials total run time: 0:00:07.071808

Overall mutation trial summary
==============================
 - DETECTED: 24
 - SURVIVED: 6
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-09 23:55:16.005648


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 22, c: 19) - mutation from False to True
 - identifier1.py: (l: 22, c: 19) - mutation from False to None
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>


DETECTED
--------
 - identifier1.py: (l: 7, c: 12) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 15, c: 19) - mutation from True to None
 - identifier1.py: (l: 15, c: 19) - mutation from True to False
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 34, c: 12) - mutation from If_Statement to If_False
 - identifier1.py: (l: 34, c: 12) - mutation from If_Statement to If_True
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 37, c: 23) - mutation from False to True
 - identifier1.py: (l: 37, c: 23) - mutation from False to None