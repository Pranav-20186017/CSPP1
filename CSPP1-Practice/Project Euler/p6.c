#include<math.h>
#include<stdio.h>
void sum_vals(long int n);
void sum_vals(long int n)
{
	long int t1=0;
	long int t2=0;
	for(long int i=1;i<=n;i++)
	{
		t1 += i;
		t2 += pow(i,2);
	}
	long int temp = pow(t1,2);
	long int ans = temp - t2;
	printf("%d\n",ans);
}
int main(){
    int t; 
    scanf("%d",&t);
    for(int a0 = 0; a0 < t; a0++){
        long int n; 
        scanf("%ld",&n);
    }
    return 0;