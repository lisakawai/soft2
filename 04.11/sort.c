#include<stdio.h>
#define NUM 20


void sort(int a[],int n);

int main(void){
  int data[NUM]={20,62,17,38,76,92,59,11,93,88,79,50,89,67,75,26,83,22,13,48};
  int i;

  // k=partition(data,NUM);
  //printf("%d\n",k);
  sort(data,NUM);
 for(i=0;i<NUM;i++){
    printf("%d,",data[i]);
  }  
 printf("\n");

  return 0;

}

void sort(int a[], int n){
  int c;
  if(n<=1){return;}

  c=partition(a,n);
  sort(a,c);//先頭側
  sort(a+c+1,n-c-1);//末尾側

}

int partition(int a[], int n){
  int p;
  p=a[0];
  int i,j,m=0,temp,pre;

  for(i=0;i<n;i++){
    if(a[i]<p)
      {
      pre=a[0];
      a[0]=a[i];
      m++;

      for(j=1;j<i+1;j++)
	{
	temp=a[j];
	a[j]=pre;
	pre=temp;
	}
      }
  }

  /*  for(i=0;i<n;i++){
    printf("%d,",a[i]);
    } */ 
  return m;


}
