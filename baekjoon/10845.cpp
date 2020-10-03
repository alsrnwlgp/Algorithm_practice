#include <string>
#include <iostream>
#define MAXLEN 10000 //큐 size

using namespace std;

class Queue{
private:
	int start;
	int end;
	int* values;
	int max_size;
	
public:
	Queue(){
		start = 0;
		end = 0;
		max_size = MAXLEN;
		values = new int[max_size];
	}
	~Queue(){
		delete[] values;
	}
	void push(int x){
		values[end++] = x;
		end %= max_size;
	}
	int pop(){
		if(empty())
			return -1;
		int res = values[start];
		start = (start+1)%max_size;
		return res;
	}
	int size(){
		if(start<=end)
			return
		return end - start;
	}
	bool empty(){
		return size() == 0;
	}
	int front(){
		if(empty())
			return -1;
		else
			return values[start];
	}
	int back(){
		if(empty())
			return -1;
		else
			return values[end-1];
	}
};

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int m;
	cin >> m;
	Queue q;
	while(m--){
		string cmm;
		cin >> cmm;
		if(cmm == "push"){
			int inp;
			cin >> inp;
			q.push(inp);
		}else if(cmm == "pop"){
			cout << q.pop() << endl;
		}else if(cmm == "empty"){
			cout << q.empty() << endl;
		}else if(cmm == "size"){
			cout << q.size() << endl;
		}else if(cmm == "front"){
			cout << q.front() << endl;
		}else if (cmm == "back"){
			cout << q.back() << endl;
		}
	}
	
	return 0;
}