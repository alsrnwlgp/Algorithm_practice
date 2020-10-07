#include <iostream>

using namespace std;

int gcd(int a, int b){
	if(a < b){
		int tmp = a;
		a = b;
		b = tmp;
	}
	while(b!=0){
		int tmp = a%b;
		a = b;
		b = tmp;
	}
	return a;
}

int main(){
	int a,b;
	cin >> a >> b;
	int ans1 = gcd(a,b);
	int ans2 = a*b/ans1;
	cout << ans1 << endl << ans2;
	return 0;
}