# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class Solution {
public:
	ListNode* partition(ListNode* head, int x) {
		auto dummy1 = new ListNode(-1);
		auto dummy2 = new ListNode(-1);
		auto p = dummy1;
		auto q = dummy2;
		while (head)
		{
			if (head->val <x )
			{
				p->next = head;
				p = p->next;
			}
			else
			{
				q->next = head;
				q = q->next;
			}
			head = head->next;
		}
		q->next = NULL;
		p->next = dummy2->next;
		return dummy1->next;

	}
};
int main()
{
	ListNode *head1 = new ListNode(1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{ 4,3,2,5,2};//2
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

	auto pp = sol.partition(head1, 3);
	while (pp != NULL)
	{
		cout << pp->val << endl;
		pp = pp->next;
	}
	cout << endl;
	system("pause");
	return 0;
}
