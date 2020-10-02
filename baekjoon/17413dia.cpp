#include <string>
#include <vector>
#include <iostream>

using namespace std;

string reverse_sentence(string& s){
	string ret = "";
	size_t pos;
	while(s.empty()){
		pos = s.find(' ');
		string cur;
		if(pos == std::string::npos)
			cur = s;
		else
			cur = s.substr(0,pos);
		while(!cur.empty()){
			ret += cur.back();
			cur.pop_back();
		}
		s.erase(0, pos+1);
	}
	return ret;
}

int main(){
	string input;
	getline(cin, input);
	vector<string> container;
	while(!input.empty()){
		string tmp;
		if(input.at(0)=='<'){
			tmp = input.substr(0,input.find('<'));
			input.erase(0,input.find('>')+1);
		}
		else{
			if(input.find('<')!=string::npos){
				tmp = input.substr(0,input.find('<'));
				input.erase(0,input.find('<'));
			}
			else{
				tmp = input;
				input.erase(0,input.size());
			}
		}
		container.push_back(tmp);
	}
	for(int i=0; i<container.size(); i++){
		if(container.at(i)[0]=='<')
			cout << container.at(i);
		else
			cout << reverse_sentence(container.at(i));
	}
	return 0;
}