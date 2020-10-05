#include <iostream>

using namespace std;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int t;
	cin >> t;
	while(t--){
		int a,b;
		cin >> a >> b;
		cout << a+b << '\n';
	}
	return 0;
}

// sync_with_stdio와 cin.tie(nullptr) 를 사용할때는 scanf, printf를 사용하면 안된다. cin만 사용