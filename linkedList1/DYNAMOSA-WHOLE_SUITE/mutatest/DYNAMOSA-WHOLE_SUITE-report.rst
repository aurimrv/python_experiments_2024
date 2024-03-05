Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-WHOLE_SUITE']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 53
 - Location sample coverage: 18.87 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.440140
 - Clean trial 2 run time: 0:00:00.259773
 - Mutation trials total run time: 0:00:09.945645

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 5
 - ERROR: 1
 - TOTAL RUNS: 26
 - RUN DATETIME: 2023-03-05 22:20:18.665284


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - linkedList1.py: (l: 180, c: 0) - mutation from If_Statement to If_False


DETECTED
--------
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.Or'> to <class 'ast.And'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 71, c: 35) - mutation from None to False
 - linkedList1.py: (l: 71, c: 35) - mutation from None to True
 - linkedList1.py: (l: 86, c: 20) - mutation from None to True
 - linkedList1.py: (l: 86, c: 20) - mutation from None to False
 - linkedList1.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 113, c: 35) - mutation from None to True
 - linkedList1.py: (l: 113, c: 35) - mutation from None to False
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - linkedList1.py: (l: 151, c: 31) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - linkedList1.py: (l: 178, c: 20) - mutation from None to True
 - linkedList1.py: (l: 178, c: 20) - mutation from None to False


ERROR
-----
 - linkedList1.py: (l: 180, c: 0) - mutation from If_Statement to If_True