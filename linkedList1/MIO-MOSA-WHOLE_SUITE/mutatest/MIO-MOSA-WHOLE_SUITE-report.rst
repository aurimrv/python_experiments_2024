Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/linkedList1/linkedList1.py
 - Test commands: ['python', '-m', 'pytest', './MIO-MOSA-WHOLE_SUITE']
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
 - Clean trial 1 run time: 0:00:00.500156
 - Clean trial 2 run time: 0:00:00.272830
 - Mutation trials total run time: 0:00:10.162210

Overall mutation trial summary
==============================
 - ERROR: 1
 - DETECTED: 20
 - SURVIVED: 6
 - TOTAL RUNS: 27
 - RUN DATETIME: 2023-03-06 09:33:20.171599


Mutations by result status
==========================


SURVIVED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 134, c: 17) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>


DETECTED
--------
 - linkedList1.py: (l: 21, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 35, c: 33) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Eq'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Gt'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.Lt'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.LtE'>
 - linkedList1.py: (l: 44, c: 11) - mutation from <class 'ast.GtE'> to <class 'ast.NotEq'>
 - linkedList1.py: (l: 65, c: 8) - mutation from If_Statement to If_False
 - linkedList1.py: (l: 65, c: 8) - mutation from If_Statement to If_True
 - linkedList1.py: (l: 65, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 107, c: 11) - mutation from <class 'ast.Is'> to <class 'ast.IsNot'>
 - linkedList1.py: (l: 107, c: 24) - mutation from None to True
 - linkedList1.py: (l: 107, c: 24) - mutation from None to False
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Sub
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Mult
 - linkedList1.py: (l: 171, c: 8) - mutation from AugAssign_Add to AugAssign_Div


ERROR
-----
 - linkedList1.py: (l: 180, c: 3) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>