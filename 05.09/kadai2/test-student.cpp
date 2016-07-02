#include <stdio.h>
#include "student.h"

int main(int argc, char **argv){
	Student s1("yamada");
	Student s2("suzuki");

	s1.SetGrade(1);
	s2.SetGrade(2);

	printf("student name = %s (%d)\n", s1.GetName(), s1.GetGrade());
	printf("student name = %s (%d)\n", s2.GetName(), s2.GetGrade());

	s1.Promotion(s1.GetGrade());
	s2.Promotion(s2.GetGrade());
	
	printf("after promotion\n");
	printf("student name = %s (%d)\n", s1.GetName(), s1.GetGrade());
	printf("student name = %s (%d)\n", s2.GetName(), s2.GetGrade());

	return 0;
}
