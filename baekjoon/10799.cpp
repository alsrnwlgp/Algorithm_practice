#include <cstring>
#include <cstdio>
#define MAXLEN 100000

using namespace std;

char l[MAXLEN];

int main(){
	scanf("%s", l);
	bool before;
	int s = 0;
	int ans = 0;
	for(int i=0; i < strlen(l); i++){
		char ch = l[i];
		if(ch == '('){
			s++;
			before = true;
		}
		else if(ch == ')'){
			if(before){ // razor
				ans += --s;
				before = false;
			}else{ //rod
				s--;
				ans++;
			}
		}
	}
	printf("%d",ans);
	return 0;
}