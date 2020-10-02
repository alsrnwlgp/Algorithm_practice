#include <string>
#include <iostream>
#include <stack>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int t;
	int a;
	cin >> t;
	stack<int> s;
	int inp = 1;
	string res = "";
	while(t--){
		cin >> a;
		while(inp<=a){
			s.push(inp);
			inp++;
			res += "+\n";
		}
		if(a!=s.top()){
			cout << "NO";
			return 0;
		}else{
			s.pop();
			res += "-\n";
		}
	}
	cout << res;
	return 0;
}
