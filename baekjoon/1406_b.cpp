#include <string>
#include <iostream>
#include <stack>
#include <cstring>

using namespace std;

char a[600000];

int main(){
	scanf("%s",a);
	stack<char> l, r;
	int n = strlen(a);
	for(int i; i<n; i++){
		l.push(a[i]);
	}
	int m;
	scanf("%d", &m);
	cin.ignore();
	while(m--){
		string comm;
		getline(cin, comm);
		if(comm[0]=='L'&&!l.empty()){
			r.push(l.top());
			l.pop();
		}else if(comm[0]=='D'&&!r.empty()){
			l.push(r.top());
			r.pop();
		}else if(comm[0]=='B'&&!l.empty()){
			l.pop();
		}else if(comm[0]=='P'){
			char ch = comm[2];
			l.push(ch);
		}
	}
	
	while(!l.empty()){
		r.push(l.top());
		l.pop();
	}
	
	while(!r.empty()){
		printf("%c", r.top());
		r.pop();
	}
		
	return 0;
}