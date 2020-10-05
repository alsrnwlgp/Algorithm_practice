#include <stack>
#include <map>
#include <string>
#include <iostream>


using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n;
	cin >> n;
	string exp;
	cin >> exp;
	map<char, int> m;
	m['A'] = 0;m['B'] = 1;m['C'] = 2;m['D'] = 3;m['E'] = 4;m['F'] = 5;m['G'] = 6;m['H'] = 7;m['I'] = 8;m['J'] = 9;
	m['K'] = 10;m['L'] = 11;m['M'] = 12;m['N'] = 13;m['O'] = 14;m['P'] = 15;m['Q'] = 16;m['R'] = 17;m['S'] = 18;m['T'] = 19;
	m['U'] = 20;m['V'] = 21;m['W'] = 22;m['X'] = 23;m['Y'] = 24;m['Z'] = 25;
	double v[26];
	for(int i=0; i<n; i++)
		cin >> v[i];
	stack<double> s;
	for(int i=0; i<exp.size(); i++){
		char ch = exp[i];
		if(ch == '*'){
			double a = s.top();
			s.pop();
			double b = s.top();
			s.pop();
			s.push(b*a);
		}else if(ch == '+'){
			double a = s.top();
			s.pop();
			double b = s.top();
			s.pop();
			s.push(b+a);
		}else if(ch == '/'){
			double a = s.top();
			s.pop();
			double b = s.top();
			s.pop();
			s.push(b/a);
		}else if(ch == '-'){
			double a = s.top();
			s.pop();
			double b = s.top();
			s.pop();
			s.push(b-a);
		}else{
			s.push(v[m[ch]]);
		}
	}
	cout << fixed;
	cout.precision(2);
	cout << s.top();
	
	return 0;
}