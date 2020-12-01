#include <iostream>

using namespace std;

int combination(int a, int b){
	int ans = 1;
	for(int i = 0; i < b; i++)
		ans *= a - i;
	for(int i = 0; i < b; i++)
		ans /= i + 1;
	return ans;
}

int main(){
	int n;
	cin >> n;
	int ans;
	if(n%2==0){
		ans=1;
		for(int i=0; i<n/2; i++){
			ans*=2;
			ans%=10007;
		}
	}
	else{
		ans=0;
		int a = (n+1)/2;
		int b = 1;
		while(a<=n){
			ans += combination(a,b);
			ans%=10007;
			a++;
			b+=2;
		}
	}
	cout << ans;
	return 0;
}