#include<iostream>
#include<fstream>
#include<math.h>

double f(double x){
    x = -1*x*x;
    double result=  exp(x);
    return result;
}

double derivate(double x, double h){
    double derivada= (f(x+h) - f(x-h))/(2*h);
    return derivada;
}

int main(){
    std::ofstream *File;

    File = new std::ofstream[1];

    File->open("Derivada.dat", std::ofstream::trunc);

    double l=20;

    double t[4000];

    int j=0;

    for (double i=-l; i<=20; i+=0.01){
        t[j]=i;
        j++;
    }

    j=0;
    double x[4000];

    for (j; j<4000; j++){
        File[0] << t[j] << "," << derivate(t[j], 0.01) << std::endl;
    }

    File[0].close();

    return 0;
}