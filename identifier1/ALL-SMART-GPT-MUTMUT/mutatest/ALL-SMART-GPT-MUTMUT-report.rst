Mutatest diagnostic summary
===========================
 - Source location: /home/lucca/desktop/ic/experimento/testes/python_experiments/identifier1/identifier1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './ALL-SMART-GPT-MUTMUT']
 - Mode: f
 - Excluded files: []
 - N locations input: 10000
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 39
 - Total locations identified: 39
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.843499
 - Clean trial 2 run time: 0:00:00.721930
 - Mutation trials total run time: 0:01:33.373174

Overall mutation trial summary
==============================
 - DETECTED: 108
 - SURVIVED: 7
 - TIMEOUT: 1
 - TOTAL RUNS: 116
 - RUN DATETIME: 2024-02-23 20:56:58.866690


Mutations by result status
==========================


SURVIVED
--------
 - identifier1.py: (l: 17, c: 19) - mutation from False to None
 - identifier1.py: (l: 22, c: 19) - mutation from False to None
 - identifier1.py: (l: 22, c: 19) - mutation from False to True
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 32, c: 35) - mutation from False to None


TIMEOUT
-------
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - identifier1.py: (l: 7, c: 8) - mutation from If_Statement to If_True
 - identifier1.py: (l: 7, c: 8) - mutation from If_Statement to If_False
 - identifier1.py: (l: 7, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - identifier1.py: (l: 7, c: 12) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 7, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 7, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 7, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 7, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 45) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 7, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 8, c: 19) - mutation from True to False
 - identifier1.py: (l: 8, c: 19) - mutation from True to None
 - identifier1.py: (l: 10, c: 19) - mutation from False to None
 - identifier1.py: (l: 10, c: 19) - mutation from False to True
 - identifier1.py: (l: 14, c: 8) - mutation from If_Statement to If_False
 - identifier1.py: (l: 14, c: 8) - mutation from If_Statement to If_True
 - identifier1.py: (l: 14, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - identifier1.py: (l: 14, c: 12) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 13) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 29) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 45) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 46) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 62) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 78) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 14, c: 79) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 14, c: 95) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 15, c: 19) - mutation from True to False
 - identifier1.py: (l: 15, c: 19) - mutation from True to None
 - identifier1.py: (l: 17, c: 19) - mutation from False to True
 - identifier1.py: (l: 23, c: 8) - mutation from If_Statement to If_False
 - identifier1.py: (l: 23, c: 8) - mutation from If_Statement to If_True
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 23, c: 12) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 26, c: 12) - mutation from If_Statement to If_False
 - identifier1.py: (l: 26, c: 12) - mutation from If_Statement to If_True
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - identifier1.py: (l: 26, c: 15) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - identifier1.py: (l: 29, c: 22) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - identifier1.py: (l: 31, c: 20) - mutation from If_Statement to If_False
 - identifier1.py: (l: 31, c: 20) - mutation from If_Statement to If_True
 - identifier1.py: (l: 32, c: 35) - mutation from False to True
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Sub
 - identifier1.py: (l: 33, c: 20) - mutation from AugAssign_Add to AugAssign_Div
 - identifier1.py: (l: 34, c: 12) - mutation from If_Statement to If_False
 - identifier1.py: (l: 34, c: 12) - mutation from If_Statement to If_True
 - identifier1.py: (l: 34, c: 15) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 34, c: 29) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - identifier1.py: (l: 34, c: 47) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - identifier1.py: (l: 35, c: 23) - mutation from True to None
 - identifier1.py: (l: 35, c: 23) - mutation from True to False
 - identifier1.py: (l: 37, c: 23) - mutation from False to True
 - identifier1.py: (l: 37, c: 23) - mutation from False to None
 - identifier1.py: (l: 39, c: 19) - mutation from False to None
 - identifier1.py: (l: 39, c: 19) - mutation from False to True