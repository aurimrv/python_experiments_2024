Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack1/stack1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.238089
 - Clean trial 2 run time: 0:00:00.209552
 - Mutation trials total run time: 0:00:05.663567

Overall mutation trial summary
==============================
 - DETECTED: 15
 - SURVIVED: 8
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-06 11:46:07.813343


Mutations by result status
==========================


SURVIVED
--------
 - stack1.py: (l: 15, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Sub'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mult'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Div'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Add'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.Mod'>
 - stack1.py: (l: 99, c: 29) - mutation from <class 'ast.Pow'> to <class 'ast.FloorDiv'>
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - stack1.py: (l: 9, c: 20) - mutation from None to False
 - stack1.py: (l: 9, c: 20) - mutation from None to True
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 29, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 29, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Add
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack1.py: (l: 35, c: 12) - mutation from AugAssign_Sub to AugAssign_Div
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_True
 - stack1.py: (l: 39, c: 8) - mutation from If_Statement to If_False
 - stack1.py: (l: 48, c: 20) - mutation from None to True
 - stack1.py: (l: 48, c: 20) - mutation from None to False
 - stack1.py: (l: 73, c: 15) - mutation from False to None
 - stack1.py: (l: 73, c: 15) - mutation from False to True
 - stack1.py: (l: 106, c: 8) - mutation from If_Statement to If_True