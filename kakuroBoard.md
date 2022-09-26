A Kakuro board is rectangular and made of square 
cells. All cells begin and end with | characters. 
Adjacent cells share a |. Each cell is either a wall 
or an open space. 

Wall cells can have up to two numbers in them, one 
describing the sum of the values in the column below 
them, one describing the sum of the values in the row 
to their right. Both columns and rows stop when they 
first encounter another wall cell or the edge of the 
board. The minimum length for a row or column is 1 
cell. A wall cell lists the column sum first, followed
by a backslash, followed by the row sum. If the length 
of a column or row would be 0, the number is replaced 
by a - character. In order to have a consistent cell 
size, single digit numbers have a space on the side,
and double digit numbers do not.

Open cells are represented by two spaces on either side
of a period. If it contains a value, the digit replaces
the period.

The initial board:
```
| -\- | 5\- |20\- | -\- |15\- |12\- | 7\- |
| -\12|  .  |  .  | -\7 |  .  |  .  |  .  |
| -\9 |  .  |  .  |11\17|  .  |  .  |  .  |
| -\- | -\8 |  .  |  .  |  .  |11\- | -\- |
| -\- |16\- |10\22|  .  |  .  |  .  |10\- |
| -\10|  .  |  .  |  .  | -\9 |  .  |  .  |
| -\19|  .  |  .  |  .  | -\4 |  .  |  .  |
```
The solved board:
```
| -\- | 5\- |20\- | -\- |15\- |12\- | 7\- |
| -\12|  3  |  9  | -\7 |  2  |  4  |  1  |
| -\9 |  2  |  7  |11\17|  3  |  8  |  6  |
| -\- | -\8 |  4  |  3  |  1  |11\- | -\- |
| -\- |16\- |10\22|  5  |  9  |  8  |10\- |
| -\10|  7  |  2  |  1  | -\9 |  2  |  7  |
| -\19|  9  |  8  |  2  | -\4 |  1  |  3  |
```

| -\- | 4\- |35\- |11\- |40\- | -\- |24\- |13\- |17\- |17\- |
| -\26|  .  |  .  |  .  |  .  | -\20|  .  |  .  |  .  |  .  |
| -\16|  .  |  .  |  .  |  .  |19\25|  .  |  .  |  .  |  .  |
| -\- |17\33|  .  |  .  |  .  |  .  |  .  |  .  |  .  | 5\- |
| -\16|  .  |  .  |14\16|  .  |  .  |31\6 |  .  |  .  |  .  |
| -\32|  .  |  .  |  .  |  .  |  .  |  .  | 4\3 |  .  |  .  |
| -\- |16\- |25\16|  .  |  .  | 7\5 |  .  |  .  |19\- | 4\- |
| -\17|  .  |  .  |28\25|  .  |  .  |  .  |  .  |  .  |  .  |
| -\24|  .  |  .  |  .  |16\4 |  .  |  .  |13\3 |  .  |  .  |
| -\- |11\29|  .  |  .  |  .  |  .  |  .  |  .  |  .  | 3\- |
| -\11|  .  |  .  |  .  |  .  | -\26|  .  |  .  |  .  |  .  |
| -\28|  .  |  .  |  .  |  .  | -\12|  .  |  .  |  .  |  .  |


| -\- |17\- |23\- |39\- |17\- |13\- |23\- |20\- | -\- |10\- |16\- |11\- |
| -\30|  .  |  .  |  .  |  .  |  .  |  .  |  .  | -\11|  .  |  .  |  .  |
| -\41|  .  |  .  |  .  |  .  |  .  |  .  |  .  |16\19|  .  |  .  |  .  |
| -\- |13\44|  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |15\- |11\- |
| -\17|  .  |  .  |  .  |  .  |  .  |35\15|  .  |  .  |  .  |  .  |  .  |
| -\10|  .  |  .  |  .  |  .  | 5\19|  .  |  .  |  .  |37\3 |  .  |  .  |
| -\6 |  .  |  .  |  .  |17\9 |  .  |  .  |16\27|  .  |  .  |  .  |  .  |
| -\- |24\- |12\42|  .  |  .  |  .  |  .  |  .  |  .  |  .  |39\- |11\- |
| -\21|  .  |  .  |  .  |  .  |26\17|  .  |  .  |35\23|  .  |  .  |  .  |
| -\10|  .  |  .  |30\19|  .  |  .  |  .  |30\24|  .  |  .  |  .  |  .  |
| -\30|  .  |  .  |  .  |  .  |  .  | 9\29|  .  |  .  |  .  |  .  |  .  |
| -\- |17\- | 9\37|  .  |  .  |  .  |  .  |  .  |  .  |  .  |  .  |17\- |
| -\16|  .  |  .  |  .  | -\29|  .  |  .  |  .  |  .  |  .  |  .  |  .  |
| -\23|  .  |  .  |  .  | -\42|  .  |  .  |  .  |  .  |  .  |  .  |  .  |
