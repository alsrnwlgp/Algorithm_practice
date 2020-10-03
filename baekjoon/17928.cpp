#include <string>
#include <iostream>
#include <cstdio>
#include <stack>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n;
	scanf("%d", &n);
	stack<int> s; // stack의 원소는 index
	int ans[n]; // 답 list
	int l[n]; // input
	for(int i=0; i<n; i++){
		cin >> l[i];
	}
	for(int i = 0; i< n; i++){
		if(s.empty()){
			s.push(i);
			continue;
		}
		while(!s.empty()&&l[s.top()] < l[i]){
			ans[s.top()] = l[i];
			s.pop();
		}
		s.push(i);
	}
	while(!s.empty()){
		ans[s.top()] = -1;
		s.pop();
	}
	for(int i = 0;i<n;i++){
		cout << ans[i] << ' ';
	}
	
	return 0;	
}