/* labmember4.h */

class LabMember{
	protected:
		char name[32];

	public:
		LabMember() {};
		LabMember(char* _name){
			strcpy(name, _name);
		}
		~LabMember() {
		}

		void SetName(const char* _name){
			sprintf(name, "Mr.%s", _name);
		}

		char* GetName(){
			return name;
		}

		virtual void PrintInfo(){};
};