Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/sort1/sort1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 24
 - Location sample coverage: 41.67 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.230598
 - Clean trial 2 run time: 0:00:00.225972
 - Mutation trials total run time: 0:00:07.120204

Overall mutation trial summary
==============================
 - DETECTED: 9
 - SURVIVED: 15
 - TIMEOUT: 1
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-12 11:35:18.054669


Mutations by result status
==========================


SURVIVED
--------
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_UnboundUpper
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_True
 - sort1.py: (l: 64, c: 12) - mutation from If_Statement to If_False
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.NotEq'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Lt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Gt'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.GtE'>
 - sort1.py: (l: 64, c: 15) - mutation from <class 'ast.LtE'> to <class 'ast.Eq'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_False
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 72, c: 23) - mutation from Slice_UnboundUpper to Slice_UnboundLower
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_False


TIMEOUT
-------
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>


DETECTED
--------
 - sort1.py: (l: 34, c: 22) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - sort1.py: (l: 50, c: 38) - mutation from Slice_UnboundUpper to Slice_Unbounded
 - sort1.py: (l: 50, c: 67) - mutation from Slice_UnboundLower to Slice_Unbounded
 - sort1.py: (l: 62, c: 14) - mutation from <class 'ast.And'> to <class 'ast.Or'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - sort1.py: (l: 62, c: 42) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - sort1.py: (l: 71, c: 8) - mutation from If_Statement to If_True
 - sort1.py: (l: 82, c: 8) - mutation from If_Statement to If_True