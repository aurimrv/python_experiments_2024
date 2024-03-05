Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.537196
 - Clean trial 2 run time: 0:00:00.270424
 - Mutation trials total run time: 0:00:09.815473

Overall mutation trial summary
==============================
 - DETECTED: 20
 - SURVIVED: 2
 - ERROR: 1
 - TOTAL RUNS: 23
 - RUN DATETIME: 2023-03-12 12:47:06.261405


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 28) - mutation from None to True
 - linkedList1.py: (l: 21, c: 28) - mutation from None to False


DETECTED
--------
 - linkedList1.py: (l: 24, c: 16) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 24, c: 16) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 27, c: 15) - mutation from False to True
 - linkedList1.py: (l: 27, c: 15) - mutation from False to None
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 44, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 44, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 53, c: 26) - mutation from None to False
 - linkedList1.py: (l: 53, c: 26) - mutation from None to True
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 80, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Div
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Mult


ERROR
-----
 - linkedList1.py: (l: 180, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>