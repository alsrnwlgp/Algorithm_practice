#include <iostream>

using namespace std;

int d[11] = {-1,1,2,4,-1,-1,-1,-1,-1,-1,-1};

int main(){
	int n,t;
	cin >> t;
	while(t--){
		cin >> n;
		if(d[n]!=-1)
		{
			cout << d[n] << endl;
			continue;
		}
		for(int i=4; i<n+1; i++)
			d[i] = d[i-1]+d[i-2]+d[i-3];
		cout << d[n] << endl;
	}
	
	return 0;
}