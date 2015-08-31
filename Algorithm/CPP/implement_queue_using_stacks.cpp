# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include<random>
# include <queue>
#include <stdint.h>

using namespace std;

class Queue {
public:
	// Push element x to the back of queue.
	void push(int x) {
		Stack1.push(x);
	}

	// Removes the element from in front of queue.
	void pop(void) {
		while (!Stack1.empty())
		{
			Stack2.push(Stack1.top());
			Stack1.pop();
		}
		Stack2.pop();
		while (!Stack2.empty())
		{
			Stack1.push(Stack2.top());
			Stack2.pop();
		}
	}

	// Get the front element.
	int peek(void) {
		//if (Stack1.empty()) return Stack2.top();
		while (!Stack1.empty())
		{
			Stack2.push(Stack1.top());
			Stack1.pop();
		}
		int top = Stack2.top();
		while (!Stack2.empty())
		{
			Stack1.push(Stack2.top());
			Stack2.pop();
		}
		return top;
	}

	// Return whether the queue is empty.
	bool empty(void) {
		return (Stack1.empty() && Stack2.empty());

	}
private:
	stack<int> Stack1;
	stack<int> Stack2;
};
