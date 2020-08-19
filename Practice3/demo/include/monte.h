#ifndef MONTE_H
#define MONTE_H

double variance(double X[],int len);
double stdDev(double X[],int len);
double throwNeedles(double numNeedles);
int getEst(double a[],int len);
double estPi(double precision, double numTrials);

#endif