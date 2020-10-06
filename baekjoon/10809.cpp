#include <stack>
#include <iostream>
#include <vector>

using namespace std;

int main(){
	string s;
	cin >> s;
	vector<int> v(26,-1);
	for(int i = 0; i<s.size(); i++){
		int a = s[i] - 97;
		if(v[a] == -1)
			v[a] = i;
	}
	for(int a: v){
		cout << a << ' ';
	}
	
	return 0;
}