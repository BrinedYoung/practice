#include <stdio.h>
#include "monte.h"


int main()
{   
    double vPi=estPi(0.01,100);
    printf("The vPi = %.5lf",vPi);
    return 0;
}