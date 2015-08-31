# include <iostream>
# include <string>
using namespace std;



class Stack {
public:
	// Push element x onto stack.
	void push(int x) {
		Queue1.push(x);

	}

	// Removes the element on top of the stack.
	void pop() {
		int count = 0;
		while (!Queue1.empty())
		{
			Queue2.push(Queue1.front());
			Queue1.pop();
			count++;
		}
		while (--count)
		{
			Queue1.push(Queue2.front());
			Queue2.pop();
		}
		Queue2.pop();
	}

	// Get the top element.
	int top() {
		int count = 0;
		while (!Queue1.empty())
		{
			Queue2.push(Queue1.front());
			Queue1.pop();
			count++;
		}
		while (--count)
		{
			Queue1.push(Queue2.front());
			Queue2.pop();
		}
		int top = Queue2.front();
		Queue2.pop();
		Queue1.push(top);
		return top;

	}

	// Return whether the stack is empty.
	bool empty() {
		return Queue1.empty();
	}

private:
	queue<int> Queue1;
	queue<int> Queue2;
};
