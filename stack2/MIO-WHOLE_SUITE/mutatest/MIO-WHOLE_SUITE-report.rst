Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack2/stack2.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 3
 - Total locations identified: 3
 - Location sample coverage: 100.00 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.192338
 - Clean trial 2 run time: 0:00:00.186643
 - Mutation trials total run time: 0:00:02.757695

Overall mutation trial summary
==============================
 - DETECTED: 11
 - SURVIVED: 2
 - TOTAL RUNS: 13
 - RUN DATETIME: 2023-03-09 23:56:54.761633


Mutations by result status
==========================


SURVIVED
--------
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack2.py: (l: 21, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack2.py: (l: 13, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack2.py: (l: 21, c: 8) - mutation from If_Statement to If_True
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack2.py: (l: 27, c: 15) - mutation from <class 'ast.Add'> to <class 'ast.Div'>