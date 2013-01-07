test_harness
============

HPC research needs repeatable experiments and immediate data from them

- timing collection
  - thread safe tic and toc
  - avoid timing system calls themselves
- progress and debug prints
  -avoid timing these
- plotting system
- automatic running on multiple inputs
  - Make a program that generates bash scripts.
  - Or write a very general bash script.
  - Possibly interactively prompt for the variables in the script and then dump it to a file. that way customization can be done without having to remember the variables.
  - randomized inputs for testing thougroughness
  - make sure it can select either even, powers of two or all.

- counts
- per iteration and optional occurrences
- histogramming
  - an ascii output would be nice at first
- basic stats tracking (mean, variance)
- built-in repeat running and variable sweeping (i.e. run with 1 to 16 threads by 4 and for each of those run 
- checkpointing data?
- arbitrary strings
- querying the dataset and quickly building plots (if we could connect this directly to ggplot such that you could say something like give me the histogram that is the sum histogram x across runs with threads 12 and 16 or maybe plot the time of this function over that variable sweep)
- autotuning
  -What would you like to autotune rob?
