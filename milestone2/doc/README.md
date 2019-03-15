Command to run :
1. go to <top-dir>/src
2. run ./cmd --help to get info how to use the file

Currently the parser can parse a subset of C++.
We have named this language crux.
Most of the features are covered in the testcases.

Features :
## Branches
 - Same as vanilla C++ except following changes
 - We have no else if clause so you have to write if-else as :
   ```
   if(i==0){
      y=1;
   }else{
      if(i==1){
        y=2;
      }
   }
   ```
 - You have to use curly braces for all loops,branches,etc... single lines not allowed
   ```
   if(i==0) y=1;    //not allowed
   if(i==0){ y=1; } //allowed
   ```
## Loops
- All 3 for, while and do-while loops are allowed and same as vanilla C++ except for the compulsory use of braces
  ```
  for(;;)int i=0; //not allowed
  for(;;){;}      //allowed
  ```
- break gets attached to nearest switch-case/\{for,while,do-while\}loop, while continue gets attached to nearest \{for,while,do-while\}loop. See tests/34.cpp.
