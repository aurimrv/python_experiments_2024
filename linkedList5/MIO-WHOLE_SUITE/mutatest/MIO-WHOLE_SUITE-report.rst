Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList5/linkedList5.py
 - Test commands: ['python', '-m', 'pytest', './MIO-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.481775
 - Clean trial 2 run time: 0:00:00.243908
 - Mutation trials total run time: 0:00:09.780609

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 4
 - TOTAL RUNS: 24
 - RUN DATETIME: 2023-03-09 23:55:59.247645


Mutations by result status
==========================


SURVIVED
--------
 - linkedList5.py: (l: 25, c: 8) - mutation from If_Statement to If_False
 - linkedList5.py: (l: 45, c: 19) - mutation from None to True
 - linkedList5.py: (l: 45, c: 19) - mutation from None to False
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList5.py: (l: 13, c: 28) - mutation from None to False
 - linkedList5.py: (l: 13, c: 28) - mutation from None to True
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList5.py: (l: 20, c: 12) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList5.py: (l: 25, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 32, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 55, c: 8) - mutation from If_Statement to If_True
 - linkedList5.py: (l: 57, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 59, c: 11) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList5.py: (l: 65, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList5.py: (l: 74, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>