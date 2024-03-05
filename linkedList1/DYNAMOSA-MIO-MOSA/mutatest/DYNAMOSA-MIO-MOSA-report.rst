Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.552720
 - Clean trial 2 run time: 0:00:00.284383
 - Mutation trials total run time: 0:00:10.138588

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 1
 - TOTAL RUNS: 21
 - RUN DATETIME: 2023-03-06 00:05:36.257075


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_True


DETECTED
--------
 - linkedList1.py: (l: 10, c: 20) - mutation from None to True
 - linkedList1.py: (l: 10, c: 20) - mutation from None to False
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 27, c: 15) - mutation from False to True
 - linkedList1.py: (l: 27, c: 15) - mutation from False to None
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 95, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 95, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 95, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 113, c: 35) - mutation from None to True
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 125, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 130, c: 12) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 130, c: 12) - mutation from If_Statement to If_False