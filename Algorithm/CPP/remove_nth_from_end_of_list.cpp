# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class solution {
public:
	ListNode* removeNthFromEnd(ListNode* head,int n)
	{
		auto fast = head;
		ListNode* dummy = new ListNode(0);
		dummy->next = head;
		ListNode* slow = dummy;
		while (n)
		{
			fast = fast->next;
			if (fast == NULL) return head->next;
			n--;
		}

		while (fast)
		{
			slow = slow->next;
			fast = fast->next;
		}
		auto q = slow->next;
		slow->next = q->next;
		delete(q);
		return dummy->next;
	}
};


int main()
{
	ListNode *head1 = new ListNode(1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{  2 };//2, 3, 5, 9,
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
	auto q1 = sol.removeNthFromEnd(head1, 1);
	while (q1)
	{
		cout << q1->val;
		q1 = q1->next;
	}
	system("pause");
	return 0;
}
