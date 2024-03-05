Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.360675
 - Clean trial 2 run time: 0:00:00.241496
 - Mutation trials total run time: 0:00:07.776800

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 1
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-09 23:55:24.651072


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>


DETECTED
--------
 - linkedList1.py: (l: 21, c: 11) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 24, c: 19) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 53, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 65, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 65, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 71, c: 35) - mutation from None to False
 - linkedList1.py: (l: 71, c: 35) - mutation from None to True
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 107, c: 24) - mutation from None to False
 - linkedList1.py: (l: 107, c: 24) - mutation from None to True
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>