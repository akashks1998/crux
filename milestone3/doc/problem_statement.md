Project Milestone 3 (Activations)

-----------------------------------------------------------

Submission Date: 5th April 2019

Now that  you have IR for most of the constructs, it is time to generate IR with
support for run-time activations.

The structure of the activation record must include :

- space for return value
- space for parameters
- space for old stack pointers to pop an activation
- space for locals
- space for saved registers
- any other fields required by your particular language/target
  (for example, access links if your implementation supports nested procedures)

How to lay them out is your choice but follow the conventions
used by assembler for your target architecture if you would like
your code to run eventually.

At this point, you should be able to handle small but complete non-trivial programs, 
such as Factorial, Fibonacci, and those using Dynamic Memory allocation, data structures
like lists and trees. 

You must create a few non-trivial test programs in the tests directory to show off :)
