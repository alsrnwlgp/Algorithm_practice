#include <iostream>

using namespace std;

int d[1001];

int main(){
	int N;
	cin >> N;
	cin >> d[1];
	for(int i=2; i<=N; i++){
		cin >> d[i];
		for(int j=1; j<i; j++){
			if(d[i]<d[j]+d[i-j])
				d[i] = d[j]+d[i-j];
		}
	}
	cout << d[N];
	return 0;
}