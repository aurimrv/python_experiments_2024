Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.257634
 - Clean trial 2 run time: 0:00:00.227073
 - Mutation trials total run time: 0:00:08.018441

Overall mutation trial summary
==============================
 - SURVIVED: 21
 - DETECTED: 11
 - TOTAL RUNS: 32
 - RUN DATETIME: 2023-03-06 09:34:55.529650


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Mult'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Pow'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Div'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Sub'>
 - stack1.py: (l: 94, c: 29) - mutation from <class 'ast.Add'> to <class 'ast.Mod'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - stack1.py: (l: 95, c: 29) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Sub'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Mult'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Add'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Div'>
 - stack1.py: (l: 98, c: 29) - mutation from <class 'ast.Mod'> to <class 'ast.Pow'>
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_False
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.NotEq'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Lt'>


DETECTED
--------
 - stack1.py: (l: 9, c: 20) - mutation from None to True
 - stack1.py: (l: 9, c: 20) - mutation from None to False
 - stack1.py: (l: 29, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 39, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 57, c: 11) - mutation from <class 'ast.In'> to <class 'ast.NotIn'>
 - stack1.py: (l: 76, c: 15) - mutation from True to False
 - stack1.py: (l: 76, c: 15) - mutation from True to None
 - stack1.py: (l: 130, c: 4) - mutation from If_Statement to If_True
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.LtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.GtE'>
 - stack1.py: (l: 130, c: 7) - mutation from <class 'ast.Gt'> to <class 'ast.Eq'>