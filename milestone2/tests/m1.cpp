#include <"stdio.h">
int main()
{
      int firstNumber, secondNumber, temporaryVariable;

      // Value of firstNumber is assigned to temporaryVariable
      temporaryVariable = firstNumber;

      // Value of secondNumber is assigned to firstNumber
      firstNumber = secondNumber;

      // Value of temporaryVariable (which contains the initial value of firstNumber) is assigned to secondNumber
      secondNumber = temporaryVariable;

      return 0;
}
