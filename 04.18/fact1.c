/* fact.c */
#include<stdio.h>

int fact(int x){
  if (x>=2){

/* 階乗計算：ｘが2以上の時、x-1で再帰関数を使う */
    return (x*fact(x-1));
  }

  else{

/* xが1以下の時関数を抜ける */
    return 1;
  }
}

int main (int argc,char *argv[]){
  int x,ret;

/* 入力した数字をint型に変換 */
  x=atoi(argv[1]);

/* retに階乗計算の結果を格納 */
  ret = fact(x);

/* retを表示 */
  printf("ret = %d\n",ret);
}
