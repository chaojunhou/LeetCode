# include <vector>
# include <algorithm>
# include <string>
# include <stack>
# include <algorithm>
# include <deque>
# include <iostream>
# include <time.h>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	bool isPalindrome(ListNode* head)
	{
		if (!head) return true;
		auto slow = head;
		auto fast = head;
		stack<int> Stack;
		while (fast && fast->next)
		{
			Stack.push(slow->val);
			slow = slow->next;
			fast = fast->next->next;
			
		}
		if (fast) slow = slow->next;// the odd situation
		while (slow)
		{			
			if (Stack.top() != slow->val) return false;
			Stack.pop();
			slow = slow->next;
		}
		return true;
	}
};
int main()
{
	ListNode *head1 = new ListNode(1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{ 2,2,1};//2
	for (auto x : vec)
	{
		p->next = new ListNode(x);
		p = p->next;
	}
	p->next = NULL;
	vec = { 3, 4, 7 };
	for (auto v : vec)
	{
		q->next = new ListNode(v);
		q = q->next;
	}
	q->next = NULL;

	Solution sol;

	cout<< sol.isPalindrome(head1);
	cout << endl;
	system("pause");
	return 0;
}
