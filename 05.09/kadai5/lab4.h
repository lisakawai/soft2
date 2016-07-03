/* lab4.h */
#include <vector>
#include <functional>
//#include "labmember4.h"



/*class Judge : std::binary_function<LabMember*, LabMember*, bool> {
	public:
		bool operator()(LabMember*& x, LabMember*& y){
			return x->name < y->name;
		}
};*/

//Judge judge;

class Lab{
	private:
		std::vector<LabMember*> members;
		int n_members;

	public:
		Lab(){
			n_members = 0;
		}
		~Lab(){}

		void AddMember(LabMember* new_member){
			members.push_back(new_member);
			n_members++;
		}

		void PrintMember(){
			std::sort(members.begin(), members.end(), std::less<LabMember*>());
			for(std::vector<LabMember*>::iterator l=members.begin(); l!=members.end(); l++){
				(*l)->PrintInfo();
			}
		}
};

