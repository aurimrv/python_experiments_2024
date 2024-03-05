Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:02.379163
 - Clean trial 2 run time: 0:00:01.439824
 - Mutation trials total run time: 0:00:49.610180

Overall mutation trial summary
==============================
 - DETECTED: 23
 - SURVIVED: 1
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-05 12:20:05.515521


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>


DETECTED
--------
 - linkedList1.py: (l: 21, c: 11) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 86, c: 20) - mutation from None to False
 - linkedList1.py: (l: 86, c: 20) - mutation from None to True
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 107, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 123, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 125, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 130, c: 12) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 130, c: 12) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 130, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>