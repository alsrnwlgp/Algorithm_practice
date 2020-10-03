#include <string>
#include <iostream>
#include <stack>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	string s;
	cin >> s;
	int m;
	cin >> m;
	cin.ignore();
	int cursor = s.size()-1;
	while(m--){
		string comm;
		getline(cin, comm);
		if(comm == "L"&&cursor>=0){
			cursor--;
		}if(comm == "D"&&cursor<s.size()-1){
			cursor++;
		}if(comm == "B"&&cursor!=-1){
			s.erase(cursor--, 1); // 주의 두번째 인수에 정수 넣어주지 않으면 default = npos(-1)
		}if(comm[0] == 'P'){
			if(cursor==s.size()-1){
				s.push_back(comm[2]);
				cursor++;
			}
			else
				s.insert(++cursor, 1, comm[2]);
		}
	}
	cout << s;
	return 0;
}