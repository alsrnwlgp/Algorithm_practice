#include <string>
#include <iostream>
#define MAXLEN 10000 //큐 size

using namespace std;

class Deque{
private:
	int start;
	int end;
	int* values;
	int max_size;
	
public:
	Deque(){
		start = 0;
		end = 0;
		max_size = MAXLEN;
		values = new int[max_size];
	}
	~Deque(){
		delete[] values;
	}
	void push_front(int x){
		start = (start-1+max_size)%max_size;
		values[start] = x;
	}
	void push_back(int x){
		values[end] = x;
		end = (end+1)%max_size;
	}
	int pop_front(){
		if(empty())
			return -1;
		int res = values[start];
		start = (start+1)%max_size;
		return res;
	}
	int pop_back(){
		if(empty())
			return -1;
		end = (end-1+max_size)%max_size;
		return values[end];
	}
	int size(){
		if(start<=end)
			return end-start;
		else
			return end+max_size-start;
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
			return values[(end-1+max_size)%max_size];
	}
};

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(nullptr);
	int m;
	cin >> m;
	Deque d;
	while(m--){
		string cmm;
		cin >> cmm;
		if(cmm == "push_back"){
			int inp;
			cin >> inp;
			d.push_back(inp);
		}else if(cmm == "push_front"){
			int inp;
			cin >> inp;
			d.push_front(inp);
		}else if(cmm == "pop_back"){
			cout << d.pop_back() << endl;
		}else if(cmm == "pop_front"){
			cout << d.pop_front() << endl;
		}else if(cmm == "empty"){
			cout << d.empty() << endl;
		}else if(cmm == "size"){
			cout << d.size() << endl;
		}else if(cmm == "front"){
			cout << d.front() << endl;
		}else if (cmm == "back"){
			cout << d.back() << endl;
		}
	}
	
	return 0;
}