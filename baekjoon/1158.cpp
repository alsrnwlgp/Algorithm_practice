#include <string>
#include <iostream>
#include <queue>
#include <vector>
#define MAXLEN 5000

using namespace std;

vector<int> list;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int n, k;
	cin >> n >> k;
	queue<int> q;
	for(int i = 1; i < n+1; i++){
		q.push(i);
	}
	cout << '<';
	while(!q.empty()){
		for(int i = 0; i < k-1; i++){
			q.push(q.front());
			q.pop();
		}
		cout << q.front();
		q.pop();
		if(q.size()!=0){
			cout << ", ";
		}
	}
	cout << ">\n";
	return  0;
}
