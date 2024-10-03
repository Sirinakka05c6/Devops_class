#include<stdio.h>
#include<math.h>
int main()
{
 int p;
 printf("enter principle amt:");
 scanf("%d", &p);
 int t;
 printf("enter time duration:");
 scanf("%d", &t);
 int r;
 printf("enter rate of interest:");
 scanf("%d", &r);
 
 int CI = p * pow((1+r)/100,t);
 printf("compound interest is %d", CI);
 return 0;
}
