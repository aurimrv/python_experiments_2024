Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
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
 - Clean trial 1 run time: 0:00:01.692175
 - Clean trial 2 run time: 0:00:01.457139
 - Mutation trials total run time: 0:00:52.730454

Overall mutation trial summary
==============================
 - DETECTED: 26
 - SURVIVED: 2
 - TOTAL RUNS: 28
 - RUN DATETIME: 2023-03-05 18:46:33.731341


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 21, c: 12) - mutation from If_Statement to If_False
 - linkedList2.py: (l: 66, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 16, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 16, c: 26) - mutation from None to True
 - linkedList2.py: (l: 16, c: 26) - mutation from None to False
 - linkedList2.py: (l: 21, c: 12) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 53, c: 23) - mutation from True to False
 - linkedList2.py: (l: 53, c: 23) - mutation from True to None
 - linkedList2.py: (l: 55, c: 15) - mutation from False to None
 - linkedList2.py: (l: 55, c: 15) - mutation from False to True
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 60, c: 19) - mutation from None to False
 - linkedList2.py: (l: 60, c: 19) - mutation from None to True
 - linkedList2.py: (l: 66, c: 8) - mutation from If_Statement to If_True
 - linkedList2.py: (l: 66, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>