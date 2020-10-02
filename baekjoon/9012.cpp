#include <string>
#include <iostream>
#include <stack>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int t;
	cin >> t;
	cin.ignore();
	string str;
	while(t--){
		stack<char> s;
		getline(cin, str);
		for(char ch : str){
			if(ch=='(')
				s.push(ch);
			else{
				if(s.empty())
					s.push(ch);
				else if(s.top()=='(')
					s.pop();
				else
					s.push(ch);
			}
		}
		if(s.empty())
			cout << "YES\n";
		else
			cout << "NO\n";
	}
	
	return 0;
}