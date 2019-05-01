In this assignment,  you have to construct a scanner  and a parser for
your source language that outputs the abstract syntax tree (AST) in a 
graphical form.

To     draw      the     tree,     use     a      tool     called
graphviz(http://www.graphviz.org/).  There are  two components of
graphviz that you  will have to use: The  language for describing
the  tree called  DOT  and a  tool called  dot.  For example,  if
graph1.dot is a DOT script describing the tree, then

 $ dot -Tps graph1.dot -o graph1.ps

generates a postscript  program containing the drawing of  the tree. The
dot tool will  completely take care of the tree  layout. You just have
to specify through  the DOT language, the nodes,  their labels and the
edges.

Study the  documentation of YACC  tool you use to  understand how
actions  are  specified.   Read   about  the  DOT  language  from
http://www.graphviz.org/Documentation.php 


Specifically you have to do the following:
0. Start from the Assignment 1 (Lexer). You must have the lexer and
   grammar specifications for your source language.

1. Modify the  lexer script  to send tokens to parser.  
   NOTE: In some implementation tools, lexer is always integrated
   with the parser. You *can skip* this step for such tools.

2. Now take  the  grammar  itself and  convert  it  to a  script
   accepted  by  YACC  like  tool.   Link  it  with  the  scanner
   generated earlier (if the lexer is separate).

3.  Add actions  to the grammar script so that  the output of the
    parser is a DOT script representing the abstract syntax tree.

4.  This DOT  script, when processed by the  graphviz tool called
    dot should produce a postscript file with the diagram of the
    parse tree.

For some implementation languages, there are libraries that may 
allow you to merge step 3 and 4. If so, you are allowed to use them.

5.  Submit 10 non-trivial programs written in your source language
    that can be compiled with your compiler

6. Handle erroneous source program. Print a suitable error message for
   the error(s) encountered. You can chose to exit after the first error
   encountered.

The leafs of the AST are to be labeled either by the token names or 
the lexemes (or both).


DETAILS

 * Follow the above steps. Any deviations must be approved
   over CANVAS discussion forum (You post the proposed deviation
   and the instructor will approve/disapprove it in the discussion
   forum so that everyone is informed.).

 * Your program must accept input file(s) and other options as
   command line parameters. Use sensible like options (--help, 
   --out, --verbose etc).

 * Follow the directory structure as mentioned in Assignment 1. 
   All your source must be in <project-top>/src directory,

 * Use Makefile (or an equivalent build tool like "ant") to build the
   implementation
 
  * Update documentation in the "doc/" folder with a brief description
    of your project and the steps to build and run it. Also describe 
    all the command line options.

  * Add a new directory "tests/input2", and add few more (10 or more) 
    interesting  test cases for the AST generator you have developed.

  * The  TAs  will  spend  approx  15-20  minutes  with  you  for
    evaluation.  Make sure  that your  implementation builds  and
    runs  correctly with  minimum  number of  commands.

A  typical example session could be:

$ cd <project-top>/src
$ make
$ ./myASTGenerator ../tests/input/test1.c --out=test1.dot 
  (to execute the tool on test-case file test1.c and generate the dot file test1.dot)
