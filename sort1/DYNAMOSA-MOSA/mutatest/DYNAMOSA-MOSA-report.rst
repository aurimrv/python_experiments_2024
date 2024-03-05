Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 32
 - Location sample coverage: 31.25 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:01.063434
 - Clean trial 2 run time: 0:00:01.652110
 - Mutation trials total run time: 0:01:23.933386

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 22
 - TOTAL RUNS: 44
 - RUN DATETIME: 2023-03-05 18:56:48.602079


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - sort1.py: (l: 31, c: 30) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - sort1.py: (l: 15, c: 27) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - sort1.py: (l: 33, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 47, c: 11) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - sort1.py: (l: 86, c: 33) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>