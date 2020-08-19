#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <math.h>
#include "monte.h"

double variance(double X[],int len)
{
    /*Assumes that X is a list of numbers.
       Returns the standard deviation of X*/
    double sum=0,mean=0;
    for(int i=0;i<len;i++)
    {
        sum=sum+X[i];
    }
    mean = sum/len;
    double tot = 0;
    for(int i=0;i<len;i++)
    {
        // printf("%.2f",X[i]);  test
        tot=tot+(X[i]- mean)*(X[i]- mean);
        //printf("%.5lf",tot);  test
    }
    return tot/len;
}
    
double stdDev(double X[],int len)
{
    /*Assumes that X is a list of numbers.
       Returns the standard deviation of X*/
    double i=variance(X,len);
    return sqrt(i);
}

double throwNeedles(double numNeedles)
{
    double inCircle =0;
    double x=0,y=0;
//  printf("%.3f",numNeedles);  tset
    for (int i=1;i<=numNeedles;i++)
    {
        x =(double)rand()/RAND_MAX;
        y =(double)rand()/RAND_MAX;
        //printf("%d\t",i);
        double p=sqrt(x*x + y*y);
        if (p<=1)
        {
            inCircle=inCircle+1;
        //    printf("%.5lf\t",inCircle);
        //    printf("%.5lf\t",p);  test
        }
    }
    //printf("end\n");  test
    return 4*(inCircle/numNeedles);
}

int getEst(double a[],int len)
{
    //int i=a[2];
    double estimates[100];
    double piGuess=0;

    for(int t=0;t<a[1];t++)
    {
        piGuess = throwNeedles(a[0]);
        estimates[t]=piGuess;
    }
    double sDev = stdDev(estimates,len);
    double sum=0;
    //double mean=0;
    for(int m=0;m<len;m++)
    {
        sum=sum+estimates[m];
    }
    double curEst = sum/len;
    a[0]=curEst;
    a[1]=sDev;

    return 0;
}

double estPi(double precision, double numTrials)
{
    double numNeedles = 1000;
    //printf("\t, Needles = %d",(int)(numNeedles),'\n');  test
    double sDev = precision;
    double curEst=0;
    int len=numTrials;
    srand(time(NULL));

    while (sDev >= precision/1.96)
    {
        //printf("\t, Needles = %d",(int)(numNeedles),'\n');  test
        double a[2]={numNeedles,numTrials};
        getEst(a,len);
        curEst=a[0];
        sDev=a[1];
        printf("Est. = %.5lf",curEst);
        printf("\t, Std. dev. = %.5lf",sDev);
        printf("\t, Needles = %d",(int)(numNeedles));
        printf("\n");
        numNeedles=numNeedles*2;
    }
    return curEst;
}
