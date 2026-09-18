#SUDOKU SOLVER

A backtracking algorithm that solves 9x9 Sudoku puzzles in Python.

--HOW IT WORKS--

The solver uses recursive backtracking:

1) Find the first empty cell on the board (represented as 0).
2) Try placing digits 1–9 in that cell.
3) For each digit, check that it doesn't already appear in the same row, column, or 3x3 box.
4) If a digit is valid, place it and recurse into the next empty cell.
5) If no digit works, backtrack — clear the cell and try the next possibility for the previous cell.
6) Repeat until the board is full (solved) or every possibility is exhausted.

--USAGE--

The puzzle is currently hardcoded as a 2D list at the top of the script. To solve your own puzzle, edit the board variable directly (use 0 for empty cells), then run:

python sudoku_solver.py

--EXAMPLE--

Input:

3 6 4  | 0 9 0  | 0 0 0 
0 5 0  | 1 0 6  | 0 2 7 
0 2 7  | 0 0 5  | 0 4 6 
- - - - - - - - - - - -
0 7 3  | 6 0 1  | 0 0 4 
4 0 2  | 3 0 0  | 1 0 0 
6 0 0  | 2 0 0  | 0 8 0 
- - - - - - - - - - - -
8 3 0  | 9 6 0  | 4 0 0 
0 0 0  | 0 2 8  | 5 0 0 
0 0 0  | 0 1 0  | 6 7 8

Output:

3 6 4  | 7 9 2  | 8 5 1 
9 5 8  | 1 4 6  | 3 2 7 
1 2 7  | 8 3 5  | 9 4 6 
- - - - - - - - - - - -
5 7 3  | 6 8 1  | 2 9 4 
4 8 2  | 3 7 9  | 1 6 5 
6 9 1  | 2 5 4  | 7 8 3 
- - - - - - - - - - - -
8 3 5  | 9 6 7  | 4 1 2 
7 1 6  | 4 2 8  | 5 3 9 
2 4 9  | 5 1 3  | 6 7 8

--REQUIREMENTS--

None — uses only the Python standard library.

--POSSIBLE FUTURE IMPROVEMENTS--

- Read puzzles from a file instead of hardcoding them
- Add input validation for malformed or unsolvable boards
- Add a puzzle generator
- Solve different size sudoku puzzles

--LICENSE--

MIT
