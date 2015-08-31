# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;


struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* rotateRight(ListNode* head, int k) {
		if (!head || !head->next) return head;
		auto dummy = new ListNode(-1);
		dummy->next = head;
		auto p = dummy;
		int count = 0;
		while (p->next)
		{
			p = p->next;
			count++ ;
		}
		k = k % (count);
		p->next = head;
		auto q = head;
		int num = count - k-1;
		while (num--)
		{
			q = q->next;
		}
		head = q->next;
		q->next = NULL;
		return head;

	}
};
int main()
{
	ListNode *head1 = new ListNode(1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{ 2,3,4,5};//2
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

	Solution sol;

	auto pp = sol.rotateRight(head1,2);
	while (pp != NULL)
	{
		cout << pp->val << endl;
		pp = pp->next;
	}
	cout << endl;
	system("pause");
	return 0;
}
