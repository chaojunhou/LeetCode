# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <stack>
# include <algorithm>
# include<time.h>
using namespace std;


struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* reverseBetween(ListNode* head, int m, int n) {
		ListNode* dummy = new ListNode(-1);
		dummy->next = head;
		auto p = dummy;
		auto q = head;
		int k = n - m;
		while (--m)
		{
			q = q->next;
			p = p->next;
		}
		
		while (k--)
		{
			auto nxt = q->next;
			q->next = nxt->next;
			nxt->next = p->next;
			p->next = nxt;
		}

		return dummy->next;
	}
};

int main()
{
	ListNode *head1 = new ListNode(1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{ 2, 3, 5, 9 };//2
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
	//p = root->next;
	//while (p!=NULL)
	//{
	//	cout << p->val << endl;
	//	p = p->next;
	//}
	Solution sol;
	auto q1 = sol.reverseBetween(head1, 2,4);
	while (q1)
	{
		cout << q1->val;
		q1 = q1->next;
	}
	system("pause");
	return 0;
}
