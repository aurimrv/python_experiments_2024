Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 36
 - Location sample coverage: 27.78 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.285836
 - Clean trial 2 run time: 0:00:00.232562
 - Mutation trials total run time: 0:00:06.934663

Overall mutation trial summary
==============================
 - DETECTED: 21
 - SURVIVED: 3
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-05 22:20:26.398668


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 21, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 21, c: 32) - mutation from True to False
 - linkedList2.py: (l: 21, c: 32) - mutation from True to None


DETECTED
--------
 - linkedList2.py: (l: 7, c: 37) - mutation from None to False
 - linkedList2.py: (l: 7, c: 37) - mutation from None to True
 - linkedList2.py: (l: 15, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 21, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 22, c: 15) - mutation from False to True
 - linkedList2.py: (l: 22, c: 15) - mutation from False to None
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 49, c: 19) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 53, c: 23) - mutation from True to None
 - linkedList2.py: (l: 53, c: 23) - mutation from True to False
 - linkedList2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList2.py: (l: 75, c: 19) - mutation from None to False
 - linkedList2.py: (l: 75, c: 19) - mutation from None to True