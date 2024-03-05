Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:01.132732
 - Clean trial 2 run time: 0:00:01.018722
 - Mutation trials total run time: 0:00:31.788449

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 4
 - TOTAL RUNS: 26
 - RUN DATETIME: 2023-03-05 12:19:10.050832


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>


DETECTED
--------
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 8, c: 19) - mutation from True to False
 - identifier1.py: (l: 8, c: 19) - mutation from True to None
 - identifier1.py: (l: 14, c: 12) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 78) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 34, c: 12) - mutation from If_Statement to If_False
 - identifier1.py: (l: 34, c: 12) - mutation from If_Statement to If_True
 - identifier1.py: (l: 34, c: 15) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 35, c: 23) - mutation from True to False
 - identifier1.py: (l: 35, c: 23) - mutation from True to None
 - identifier1.py: (l: 39, c: 19) - mutation from False to None
 - identifier1.py: (l: 39, c: 19) - mutation from False to True