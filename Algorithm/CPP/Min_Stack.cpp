# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;



class MinStack {
public:
	void push(int x) {
		Stack.push(x);
		if (Min.empty() || Min.top() >= x)
			Min.push(x);

	}

	void pop() {
		int top = Stack.top();
		Stack.pop(); 
		if (top == Min.top())
			Min.pop();
	}

	int top() {
		return Stack.top();
	}

	int getMin() {
		return Min.top();
	}
private:
	stack<int> Stack;
	stack<int> Min;
};
int  main()
{
	MinStack ms;
	ms.push(0);
	ms.push(1);
	ms.push(0);
	//cout << ms.top() << endl;
	cout << ms.getMin() << endl;
	ms.pop();
	//cout << ms.top() << endl;
	cout << ms.getMin() << endl;
	cout << endl;
	system("pause");
	return 0;
}
