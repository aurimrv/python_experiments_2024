Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', '--tb=no', './DYNAMOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: 2023

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.326749
 - Clean trial 2 run time: 0:00:00.227958
 - Mutation trials total run time: 0:00:05.689784

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 2
 - ERROR: 1
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-07-14 00:09:05.137590


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>


DETECTED
--------
 - linkedList1.py: (l: 23, c: 29) - mutation from None to True
 - linkedList1.py: (l: 23, c: 29) - mutation from None to False
 - linkedList1.py: (l: 53, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 53, c: 26) - mutation from None to True
 - linkedList1.py: (l: 53, c: 26) - mutation from None to False
 - linkedList1.py: (l: 65, c: 24) - mutation from None to False
 - linkedList1.py: (l: 65, c: 24) - mutation from None to True
 - linkedList1.py: (l: 86, c: 20) - mutation from None to False
 - linkedList1.py: (l: 86, c: 20) - mutation from None to True
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 113, c: 35) - mutation from None to True
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 123, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


ERROR
-----
 - linkedList1.py: (l: 180, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>