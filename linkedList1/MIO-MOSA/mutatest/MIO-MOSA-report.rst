Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA']
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
 - Clean trial 1 run time: 0:00:00.431470
 - Clean trial 2 run time: 0:00:00.249605
 - Mutation trials total run time: 0:00:09.257511

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 2
 - ERROR: 1
 - TOTAL RUNS: 25
 - RUN DATETIME: 2023-03-06 11:44:34.565101


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 28) - mutation from None to False
 - linkedList1.py: (l: 21, c: 28) - mutation from None to True


DETECTED
--------
 - linkedList1.py: (l: 10, c: 20) - mutation from None to False
 - linkedList1.py: (l: 10, c: 20) - mutation from None to True
 - linkedList1.py: (l: 24, c: 19) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 53, c: 26) - mutation from None to False
 - linkedList1.py: (l: 53, c: 26) - mutation from None to True
 - linkedList1.py: (l: 65, c: 24) - mutation from None to True
 - linkedList1.py: (l: 65, c: 24) - mutation from None to False
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 120, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 178, c: 20) - mutation from None to True
 - linkedList1.py: (l: 178, c: 20) - mutation from None to False


ERROR
-----
 - linkedList1.py: (l: 180, c: 0) - mutation from If_Statement to If_True