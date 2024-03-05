Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 55
 - Location sample coverage: 18.18 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.707434
 - Clean trial 2 run time: 0:00:00.281491
 - Mutation trials total run time: 0:00:10.197078

Overall mutation trial summary
==============================
 - SURVIVED: 2
 - DETECTED: 22
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-12 11:34:32.611573


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 25, c: 19) - mutation from None to False
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 25, c: 19) - mutation from None to True
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 59, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 59, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 64, c: 31) - mutation from None to False
 - linkedList5.py: (l: 64, c: 31) - mutation from None to True
 - linkedList5.py: (l: 77, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 80, c: 36) - mutation from None to True
 - linkedList5.py: (l: 80, c: 36) - mutation from None to False
 - linkedList5.py: (l: 88, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 95, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>