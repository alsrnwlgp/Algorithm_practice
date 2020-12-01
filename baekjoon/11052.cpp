#include <iostream>

using namespace std;

int main(){
	int n, before, one_card, cur_card;
	cin >> n;
	cin >> one_card;
	before = one_card;
	for(int i=1; i<n; i++){
		cin >> cur_card;
		if(cur_card >= before+one_card)
			before = cur_card;
		else
			before += one_card;
	}
	cout << before;
	return 0;
}