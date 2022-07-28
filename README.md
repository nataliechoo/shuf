# shuf
Python implementation of shuf, the command-line utility.

implements GNU shuf in Python (the original shuf was written in C).

Supports the following options with the exact same behavior as GNU's shuf:
  --input-range (-i), --head-count (-n), --repeat (-r), and --help. 
  - As with GNU shuf, if --repeat (-r) is used without --head-count (-n), shuf runs forever. 
  - This also supports zero non-option arguments or a single non-option argument "-" (either of which means read from standard input), or single non-option     arguments other than "-" (which specifies the input file name).
  - This also reports an error when given invalid arguments

