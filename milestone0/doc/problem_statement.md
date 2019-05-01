
1.  ## The Language
    
    1.  Name the source language **S** for your compiler.
    2.  Recall that you have to **implement** some features in the language that distinguish it from vanilla “C” language. If any such features are not present in **S,** you have to add them. **List these features.**
    3.  Name the implementation Language (**I**) and target language (**T**)
    
    You are free to borrow the grammar (ONLY) for your **S** from the internet or some other reference. However, make sure you cite the source.
    
2.  ## The Lexer 
    
    Implement a lexical analyzer for the language **S** in **I**. The task of the lexer is to **highlight the syntax of S.** That is, the lexer will produce an **HTML** file in which different tokens of the input program are coloured in different colours.
    
    Lexer must accept a command line argument **--cfg=<color config file name>** to specify a configuration file for colour scheme. Each row in this file will consist of a pair: <token name, valid HTML colour>. Every lexeme in the input program corresponding to the token “token name” must get the “valid HTML colour”.
    
    Lexer must accept a command line argument **--out=<html file name>** to specify an output file.
    

