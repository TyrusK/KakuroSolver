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
* Repeatedly find tile with lowest number of options, guess (depth first)
  * Update possible values in other tiles, using possible combos
  * Stack saving each guess and changes
  * Return to guess if contradiction
    * A contradiction is when there are zero options
  * Should handle case with one option
  * If tie, choose first or random?
  * Figure out if it could use numerical tricks
  * Could also do breadth first

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
