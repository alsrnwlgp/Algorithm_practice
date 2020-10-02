#include <string>
#include <iostream>
#include <vector>

using namespace std;

string reverse_string(string& s){
	string ret = "";
	size_t pos;
	while((pos = s.find(' ')) != string::npos){
		string tmp = s.substr(0,pos);
		for(int i = tmp.size()-1; i>=0; i--)
			ret+=tmp[i];
		ret+=' ';
		s.erase(0, pos+1);
	}
	for(int i = s.size()-1; i>=0; i--)
		ret+=s[i];
	return ret;
}

int main(){
	string is;
	vector<string> container;
	getline(cin, is);
	// string 을 tag와 단어로 구분해 vector에 넣는다
	while(is.size()){
		size_t pos1 = is.find('<');
		size_t pos2 = is.find('>');
		//첫번째가 tag일때
		if(pos1 == 0){
			container.push_back(is.substr(0,pos2+1));
			is.erase(0,pos2+1);
		}
		//단어일때
		else{
			container.push_back(is.substr(0,pos1));
			is.erase(0,pos1);
		}
	}
	// 단어들만 reverse해서 출력
	for(int i=0; i<container.size(); i++){
		string tmp = container.at(i);
		if(tmp[0] == '<')
			cout << tmp;
		else
			cout << reverse_string(tmp);
	}
	
	return 0;
}