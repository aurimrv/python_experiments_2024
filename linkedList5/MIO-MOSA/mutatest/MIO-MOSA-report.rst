Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.607019
 - Clean trial 2 run time: 0:00:00.239482
 - Mutation trials total run time: 0:00:13.184311

Overall mutation trial summary
==============================
 - DETECTED: 29
 - SURVIVED: 2
 - TOTAL RUNS: 31
 - RUN DATETIME: 2023-03-06 11:45:14.434101


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 55, c: 19) - mutation from None to True
 - linkedList5.py: (l: 55, c: 19) - mutation from None to False


DETECTED
--------
 - linkedList5.py: (l: 39, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 49, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 49, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 65, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 65, c: 12) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 81, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 88, c: 31) - mutation from None to True
 - linkedList5.py: (l: 88, c: 31) - mutation from None to False
 - linkedList5.py: (l: 95, c: 31) - mutation from None to True
 - linkedList5.py: (l: 95, c: 31) - mutation from None to False