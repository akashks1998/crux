In the final submission, your compiler will generate code for the target assembly. 

The primary requirement of your code generator is correctness. The next requirement is completeness—all compulsory 
features should be implemented in a general sense. For instance, your code generator should not fail because an expression 
was too large and you could not find enough registers to hold intermediate values during its evaluation, or because
some function called in the code was declared, but not defined (the code may not assemble/run if the definition is
never supplied, though).
