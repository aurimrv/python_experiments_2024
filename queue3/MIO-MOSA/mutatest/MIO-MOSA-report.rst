Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/queue3/queue3.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 44
 - Location sample coverage: 22.73 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.326509
 - Clean trial 2 run time: 0:00:00.228834
 - Mutation trials total run time: 0:00:07.818902

Overall mutation trial summary
==============================
 - DETECTED: 11
 - SURVIVED: 18
 - TOTAL RUNS: 29
 - RUN DATETIME: 2023-03-06 11:45:40.995191


Mutations by result status
==========================


SURVIVED
--------
 - queue3.py: (l: 21, c: 37) - mutation from None to True
 - queue3.py: (l: 21, c: 37) - mutation from None to False
 - queue3.py: (l: 40, c: 37) - mutation from None to True
 - queue3.py: (l: 40, c: 37) - mutation from None to False
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 62, c: 19) - mutation from None to False
 - queue3.py: (l: 62, c: 19) - mutation from None to True
 - queue3.py: (l: 88, c: 35) - mutation from None to False
 - queue3.py: (l: 88, c: 35) - mutation from None to True
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 168, c: 35) - mutation from None to False
 - queue3.py: (l: 168, c: 35) - mutation from None to True
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - queue3.py: (l: 193, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>


DETECTED
--------
 - queue3.py: (l: 10, c: 20) - mutation from None to False
 - queue3.py: (l: 10, c: 20) - mutation from None to True
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 44, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 75, c: 32) - mutation from None to True
 - queue3.py: (l: 75, c: 32) - mutation from None to False
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - queue3.py: (l: 112, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>