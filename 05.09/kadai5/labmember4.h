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
			sprintf(name, "%s", _name);
		}

		bool operator<(const LabMember l) const{
			return (name[0] < l.name[0]) ? true : false;
		}

		bool operator>(const LabMember l) const{
			return (name[0] > l.name[0]) ? true : false;
		}

		char* GetName(){
			return name;
		}

		virtual void PrintInfo(){};
};