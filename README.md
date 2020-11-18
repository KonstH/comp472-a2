https://github.com/KonstH/comp472-a2.git

How to run program
---

### Step 1 - Setup
Include the puzzles input txt files that you would like to run directly in the folder.
By default, an input file with 50 random and unique puzzles is included in the repository that you can use, titled `50puzzles.txt`

Python modules used/required for this project:
- `os`
- `random`
- `numpy`
- `time`
- `argparse`
- `copy`
- `shutil`

### Step 2 - Run Program
- To run all 5 algorithms (`UCS`, `GBFS(h1)`, `GBFS(h2)`, `A*(h1)`, `A*(h2)`) at once, execute `python3 main.py` on your terminal while being in the project directory
- **IMPORTANT**: Doing this will run the algorithms on the file `50puzzles.txt` with an algorithm timeout of 60 seconds by default. Make sure that file exists in the directory if you run this command.
- To run another txt file that exists in the project directory, execute `python3 main.py -f <filename>` in your terminal
- To use a custom timeout for the algorithms, execute `python3 main.py -t <number of seconds>` in your terminal
- After running the algorithms, 2 folders called `search_files` and `solution_files` are created in the project directory. They contain their respective
output files.
- To clear any output files created from a previous run before the new run, use the `-del` flag when executing the program (ex: `python3 main.py -del`). Files with the same name get overwritten by default.
- The flags can be stacked, ex: `python3 main.py -f input.txt -t 100 -del`

Additional Notes
---

- If you wish to only run a specific algorithm with a certain heuristic, at the bottom of the file `main.py`, you can comment out or remove all the algorithms there by default
and only include the one you wish to use

Example, running A* with h1:

```
for i, puzzle in enumerate(puzzles):
  solve(puzzle, i, 'A*', 'h1', args.timeout)
 ```
