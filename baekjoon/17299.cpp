#include <iostream>
#include <vector>
#include <stack>
#define MAXLEN 1000000

using namespace std;

int v[MAXLEN] = {0,};

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n;
	cin >> n;
	vector<int> l;
	vector<int> ans(n, -1);
	stack<int> s;
	int a;
	// while(n--){
	// 	cin >> a;
	// 	l.push_back(a);
	// 	v[a]++;
	// }
	int t = n;
	while(t--){
		cin >> a;
		l.push_back(a);
		v[a]++;
	}
	for(int i=0; i<n; i++){
		while(!s.empty()&&v[l[s.top()]]<v[l[i]]){
			ans[s.top()] = l[i];
			s.pop();
		}
		s.push(i);
	}
	
	for(auto i: ans){
		cout << i << ' ';
	}
	
	return 0;
}