#include<cstdio>

int a,i,n;

int main(){
	char c[100001],b='.';
	scanf("%s",c);
	for(;c[i];i++){
		if(c[i]=='(')
			n++;
		else {
			n--;
			if(b==')')
				a++;
			else 
				a+=n;
		}
		b=c[i];
	}
	printf("%d",a);
}