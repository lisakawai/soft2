/* test-student4.cpp */

#include <stdio.h>
#include <string.h>
#include <vector>
#include <functional>
#include "labmember4.h"
#include "student4.h"
#include "professor4.h"
#include "lab4.h"

int main(int argc, char **argv){
	Lab jsk;
	Professor *p1 = new Professor();
	Student *s1 = new Student();
	Student *s2 = new Student();
	Student *s3 = new Student();
	Student *s4 = new Student();
	Student *s5 = new Student();


	p1->SetName("yamada");
	s1->SetName("suzuki");
	s2->SetName("kobayashi");
	s3->SetName("sato");
	s4->SetName("sakuma");
	s5->SetName("kato");
	p1->SetRoom(123);
	s1->SetGrade(4);
	s2->SetGrade(3);
	s3->SetGrade(5);
	s4->SetGrade(1);
	s5->SetGrade(2);
	jsk.AddMember(p1);
	jsk.AddMember(s1);
	jsk.AddMember(s2);
	jsk.AddMember(s3);
	jsk.AddMember(s4);
	jsk.AddMember(s5);

	printf("jsk member\n");
	jsk.PrintMember();

	delete p1;
	delete s1;
	delete s2;
	delete s3;
	delete s4;
	delete s5;

	return 0;
}
