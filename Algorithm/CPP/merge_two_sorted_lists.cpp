# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;
struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class solution {
public:
	ListNode* mergeTwoLists(ListNode* l1, ListNode* l2)
	{
		auto dummy = new ListNode(-1);
		auto p = dummy;
		while (l1 && l2)
		{
			if (l1->val < l2->val)
			{
				p->next = l1;
				l1 = l1->next;
			}
			else {
				p->next = l2;
				l2 = l2->next;
			}
			p = p->next;

		}
		if (l1)
		{
			p->next = l1 ;

		}
		if (l2)
		{
			p->next = l2;
		}
		return dummy->next;
	}
};


int main()
{
	ListNode *head1 = new ListNode(-1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{ 1, 2, 3, 5, 9, };
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
	solution sol;
	auto q1 = sol.mergeTwoLists(head1, head2);
	while (q1)
	{
		cout << q1->val;
		q1 = q1->next;
	}
	system("pause");
	return 0;
}
