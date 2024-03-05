Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 35
 - Location sample coverage: 28.57 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.236723
 - Clean trial 2 run time: 0:00:00.216058
 - Mutation trials total run time: 0:00:07.474608

Overall mutation trial summary
==============================
 - DETECTED: 11
 - SURVIVED: 21
 - TOTAL RUNS: 32
 - RUN DATETIME: 2023-03-09 23:56:51.368366


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Gt'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Sub'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mult'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Add'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Pow'>
 - stack1.py: (l: 97, c: 29) - mutation from <class 'ast.Div'> to <class 'ast.Mod'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - stack1.py: (l: 39, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 57, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 57, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Lt'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.Eq'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.LtE'>
 - stack1.py: (l: 66, c: 19) - mutation from <class 'ast.NotEq'> to <class 'ast.GtE'>
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 72, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_True