/* test0.c */
#include<stdio.h>

int test(int i, int j){
/* i*jの結果を返す */
  return (i * j);
}

int main(int argc, char *argv){
  int i,j,k;

/*　初期値　*/
  i = 3;
  j = 2;

/*　test(i,j)の値をｋに格納 */
  k = test(i,j);

/*　k>5のとき">5\n"と表示　*/
  if(k>5) printf(">5\n");

/*　それ以外の時"<=5"と表示　*/
  else printf("<=5\n");
  return 0;
}
