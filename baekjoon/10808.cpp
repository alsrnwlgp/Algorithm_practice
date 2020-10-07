#include <stack>
#include <iostream>
#include <vector>

using namespace std;

int main(){
	string s;
	cin >> s;
	vector<int> v(26,0);
	for(int i = 0; i<s.size(); i++){
		int a = s[i] - 97;
		v[a]++;
	}
	for(int a: v){
		cout << a << ' ';
	}
	
	return 0;
}