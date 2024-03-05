Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList2/linkedList2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.264868
 - Clean trial 2 run time: 0:00:00.218794
 - Mutation trials total run time: 0:00:07.441682

Overall mutation trial summary
==============================
 - SURVIVED: 6
 - DETECTED: 23
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-09 23:55:32.850296


Mutations by result status
==========================


SURVIVED
--------
 - linkedList2.py: (l: 15, c: 20) - mutation from None to True
 - linkedList2.py: (l: 15, c: 20) - mutation from None to False
 - linkedList2.py: (l: 37, c: 24) - mutation from None to True
 - linkedList2.py: (l: 37, c: 24) - mutation from None to False
 - linkedList2.py: (l: 66, c: 24) - mutation from None to True
 - linkedList2.py: (l: 66, c: 24) - mutation from None to False


DETECTED
--------
 - linkedList2.py: (l: 46, c: 15) - mutation from None to True
 - linkedList2.py: (l: 46, c: 15) - mutation from None to False
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 47, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 47, c: 19) - mutation from None to True
 - linkedList2.py: (l: 47, c: 19) - mutation from None to False
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList2.py: (l: 48, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 53, c: 23) - mutation from True to False
 - linkedList2.py: (l: 53, c: 23) - mutation from True to None
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - linkedList2.py: (l: 60, c: 14) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - linkedList2.py: (l: 60, c: 19) - mutation from None to False
 - linkedList2.py: (l: 60, c: 19) - mutation from None to True