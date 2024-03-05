Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:05.834042
 - Clean trial 2 run time: 0:00:01.826426
 - Mutation trials total run time: 0:01:47.968376

Overall mutation trial summary
==============================
 - DETECTED: 19
 - TOTAL RUNS: 19
 - RUN DATETIME: 2023-03-05 18:50:18.263370


Mutations by result status
==========================


DETECTED
--------
 - linkedList5.py: (l: 19, c: 14) - mutation from <class 'ast.IsNot'> to <class 'ast.Is'>
 - linkedList5.py: (l: 19, c: 26) - mutation from None to False
 - linkedList5.py: (l: 19, c: 26) - mutation from None to True
 - linkedList5.py: (l: 32, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 35, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 35, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 48, c: 31) - mutation from None to False
 - linkedList5.py: (l: 48, c: 31) - mutation from None to True
 - linkedList5.py: (l: 55, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 57, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 74, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 77, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 81, c: 12) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 81, c: 12) - mutation from If_Statement to If_False