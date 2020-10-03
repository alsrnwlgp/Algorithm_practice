#include <iostream>
#include <cstdio>
#include <stack>
#include <vector>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n;
	scanf("%d", &n);
	stack<int> s; // stack의 원소는 index
	vector<int> l;
	vector<int> ans(n, -1);
	int v;
	for(int i=0; i<n; i++){
		cin >> v;
		l.push_back(v);		
	}
	for(int i = 0; i< n; i++){
		while(!s.empty()&&l[s.top()] < l[i]){
			ans[s.top()] = l[i];
			s.pop();
		}
		s.push(i);
	}
	for(int i=0; i<n; i++){
		cout << ans[i] << " ";
	}
	
	return 0;	
}