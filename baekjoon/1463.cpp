#include <iostream>

using namespace std;

int d[1000001];

int min(int a, int b){
	return a > b? b : a;
}

int count(int n){
	if(d[n] != -1)
		return d[n];
	d[n] = count(n-1)+1;
	if(n%2 == 0)
		d[n] = min(d[n], count(n/2)+1);
	if(n%3 == 0)
		d[n] = min(d[n], count(n/3)+1);
	return d[n];
}

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n;
	cin >> n;
	d[1] = 0;
	// for(int i=2; i<n+1; i++)
	// 	d[i] = -1;
	// cout << count(n);
	for(int i=2; i<n+1; i++){
		d[i] = d[i-1]+1;
		if(i%2==0)
			d[i] = min(d[i], d[i/2]+1);
		if(i%3==0)
			d[i] = min(d[i], d[i/3]+1);
	}
	cout << d[n];
	return 0;
}