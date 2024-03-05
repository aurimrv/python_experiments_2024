Mutatest diagnostic summary
===========================
 - Source location: /home/auri/temp/lucca/python_experiments/binarySearchTree3/binarySearchTree3.py
 - Test commands: ['python', '-m', 'pytest', './DYNAMOSA-MIO-MOSA']
 - Mode: f
 - Excluded files: []
 - N locations input: 10
 - Random seed: None

Random sample details
---------------------
 - Total locations mutated: 10
 - Total locations identified: 116
 - Location sample coverage: 8.62 %


Running time details
--------------------
 - Clean trial 1 run time: 0:00:00.631481
 - Clean trial 2 run time: 0:00:00.337071
 - Mutation trials total run time: 0:00:13.292909

Overall mutation trial summary
==============================
 - DETECTED: 22
 - SURVIVED: 8
 - TOTAL RUNS: 30
 - RUN DATETIME: 2023-03-06 00:05:08.498948


Mutations by result status
==========================


SURVIVED
--------
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to False
 - binarySearchTree3.py: (l: 103, c: 59) - mutation from None to True
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to False
 - binarySearchTree3.py: (l: 360, c: 12) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 360, c: 12) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 370, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 401, c: 40) - mutation from None to True
 - binarySearchTree3.py: (l: 401, c: 40) - mutation from None to False


DETECTED
--------
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Eq'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 54, c: 11) - mutation from <class 'ast.Lt'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 79, c: 8) - mutation from If_Statement to If_True
 - binarySearchTree3.py: (l: 79, c: 8) - mutation from If_Statement to If_False
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.NotEq'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.GtE'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.Gt'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.LtE'>
 - binarySearchTree3.py: (l: 185, c: 29) - mutation from <class 'ast.Eq'> to <class 'ast.Lt'>
 - binarySearchTree3.py: (l: 288, c: 39) - mutation from None to False
 - binarySearchTree3.py: (l: 288, c: 39) - mutation from None to True
 - binarySearchTree3.py: (l: 290, c: 27) - mutation from None to True
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Add'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mult'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Mod'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Pow'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.Div'>
 - binarySearchTree3.py: (l: 306, c: 15) - mutation from <class 'ast.Sub'> to <class 'ast.FloorDiv'>
 - binarySearchTree3.py: (l: 370, c: 8) - mutation from If_Statement to If_False