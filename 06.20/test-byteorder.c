/* test-byteorder.c */

#include <stdio.h>

int print_byte(unsigned int s){
	int i;
	unsigned char *p;
	p = (unsigned char*) &s;

	for(i = 0; i < sizeof(unsigned int); i++){
		printf("%02x", *p);
		p++;
	}
	printf("\n");
}

int main(int argc, char* argv[]){

	unsigned int u1;
	u1 = 0x1234abcd;
	printf("int u1 = %x: ", u1);
	print_byte(u1);

	unsigned short u2;
	u2 = 0xabcd;
	printf("short u2 = %x: ", u2);
	print_byte(u2);

	unsigned long u3;
	u3 = 0x1234abcd;
	printf("long u3 = %lx: ", u3);
	print_byte(u3);

	return 0;

}