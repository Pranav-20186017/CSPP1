#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
#include <time.h>
void compute_sum(long long int n);
void compute_sum(long long int n)
{
	long long int temp=0;
	long long int i;
	for(i=1;i<n;i++)
	{
		if((i%3==0)||(i%5==0))
		temp += i;
	}
	printf("%lld",temp);
}
int main()
{	
	clock_t begin = clock();
	long long int t=1;
	long long int n=10000000;
	for(long long int i=0;i<t;i++)
	{
		compute_sum(n);
	}
	clock_t end=clock();
	double time_spent= (double)(end-begin)/ CLOCKS_PER_SEC;
	printf("\nbuild complete in %lf seconds",time_spent);
}