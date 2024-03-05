Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO']
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
 - Clean trial 1 run time: 0:00:01.212402
 - Clean trial 2 run time: 0:00:01.283249
 - Mutation trials total run time: 0:00:38.657436

Overall mutation trial summary
==============================
 - SURVIVED: 19
 - TIMEOUT: 2
 - DETECTED: 4
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-05 12:26:37.731125


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_True
 - sort1.py: (l: 17, c: 16) - mutation from If_Statement to If_False
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 17, c: 19) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 74, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Div
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Mult
 - sort1.py: (l: 94, c: 16) - mutation from AugAssign_Add to AugAssign_Sub


TIMEOUT
-------
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - sort1.py: (l: 69, c: 16) - mutation from AugAssign_Add to AugAssign_Mult


DETECTED
--------
 - sort1.py: (l: 47, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 73, c: 8) - mutation from If_Statement to If_True