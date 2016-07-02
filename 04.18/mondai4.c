/* mondai4.c */
#include<stdio.h>

int main(int argc, char *argv[]){
  int x,y,n;

  /* 入力した数字を整数に変換する。２つ目の引数の表記は*argv2[]でなくargv[2] */
  x=atoi(argv[1]);
  y=atoi(argv[2]);

  /* nに最大公約数を格納 */
  n=divisor(x,y);

  printf("最大公約数は%dです\n",n);
  
  return 0; 
}

int divisor(int x, int y){
  int temp,k;

  /* x<yになるようにする */
  if(x>y){
    temp=x;
    x=y;
    y=temp;
  }

  /* y/xの余りが0のとき、最大公約数はx */
  k=y%x;
  if(k==0){
    return x;
  }

  /* それ以外の時、再帰関数を用いてxとkで最大公約数を求める */
  else{
    return (divisor(x,k));
  }
}
