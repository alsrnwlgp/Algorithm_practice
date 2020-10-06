#include <stack>
#include <iostream>
#include <stack>

using namespace std;

int precedence(char ch){
	if(ch == '(')
		return 0;
	if(ch == '+' || ch == '-')
		return 1;
	else
		return 2;
}

int main(){
	string exp;
	cin >> exp;
	stack<char> ops;
	string ans;
	
	for(char ch: exp){
		if(ch == '('){
			ops.push(ch);
		}else if(ch == ')'){
			while(!ops.empty()){
				char op = ops.top();
				ops.pop();
				if(op == '(')
					break;
				ans += op;
			}
		}else if('A' <= ch && ch <= 'Z'){
			ans += ch;
		}else{
			while(!ops.empty()&&precedence(ops.top())>=precedence(ch)){
				ans += ops.top();
				ops.pop();
			}
			ops.push(ch);
		}
	}
	
	while(!ops.empty()){
		ans += ops.top();
		ops.pop();
	}
	
	cout << ans;
	
	return 0;
}