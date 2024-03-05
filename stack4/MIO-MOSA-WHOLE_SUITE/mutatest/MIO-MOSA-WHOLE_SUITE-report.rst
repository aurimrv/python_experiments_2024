Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/stack4/stack4.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 22
 - Location sample coverage: 45.45 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.273143
 - Clean trial 2 run time: 0:00:00.230762
 - Mutation trials total run time: 0:00:06.773919

Overall mutation trial summary
==============================
 - DETECTED: 19
 - SURVIVED: 6
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 09:35:15.418156


Mutations by result status
==========================


SURVIVED
--------
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 74, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Add
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Mult
 - stack4.py: (l: 76, c: 16) - mutation from AugAssign_Sub to AugAssign_Div


DETECTED
--------
 - stack4.py: (l: 63, c: 12) - mutation from If_Statement to If_False
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 63, c: 15) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_False
 - stack4.py: (l: 70, c: 8) - mutation from If_Statement to If_True
 - stack4.py: (l: 70, c: 11) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - stack4.py: (l: 70, c: 20) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - stack4.py: (l: 74, c: 12) - mutation from If_Statement to If_True
 - stack4.py: (l: 74, c: 16) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - stack4.py: (l: 74, c: 30) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Div
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Mult
 - stack4.py: (l: 84, c: 12) - mutation from AugAssign_Add to AugAssign_Sub