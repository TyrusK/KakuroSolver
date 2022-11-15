# Kakuro Solver

* Takes boards
  * Returns solutions
  * UI display
  * Animate through solving
    * Ability to pause?
    * See its “logic”?
  * Maybe expand to let user solve
* Take boards from text file
  * Reader
  * Output in same format
  * Ability to take partially solved boards?
* Store the possible combinations for each col/row
  * Each white tile stores its options, its col/row
* 1: Repeatedly find tile with lowest number of options, guess (depth first)
  * Update possible values in other tiles, using possible combos
  * Stack saving each guess and changes
  * Return to guess if contradiction
    * A contradiction is when there are zero options
  * Should handle case with one option
  * If tie, choose first or random?
  * Figure out if it could use numerical tricks
  * Could also do breadth first
* 2: Find cell with the lowest number of options
  * Follow both/all paths
  * If solution is found, done
  * if not, compare things done
    * Implement commonalities using recursive stuff
  * Go through cells with 2 options, then 3, etc
  * Reset if anything is found
* 3: Find cell with the lowest number of options
  * Follow all paths
  * If failure is found, remove that option recursively

# Tasks

* Learn Python
* Github
* Tests
* Describe file format
* Plan Board class
  * Methods to put numbers in cells, rows/cols
  * Tests
  * Methods to draw current board
  * Loop logic
  * Stack
  * Record statistics
* Cell class
* row/col class
