# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* deleteDuplicates(ListNode* head) {
		if (!head || !head->next) return head;
		auto dummy = new ListNode(-1);
		dummy->next = head;
		auto pre = dummy;
		auto cur = head->next;
		ListNode* tmp = NULL;
		while (cur)
		{
			if (pre->next->val != cur->val)
			{
				pre = pre->next;
				cur = cur->next;
			}
			else
			{
				while (cur && pre->next->val == cur->val)
				{
					tmp = cur;
					cur = cur->next;
					delete tmp;
				}
				pre->next = cur;
				if (cur)				cur = cur->next;
			}
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
	vector<int> vec{ 1,1,};//2
	for (auto x : vec)
	{
		p->next = new ListNode(x);
		p = p->next;
	}
	p->next = NULL;

	Solution sol;

	auto pp = sol.deleteDuplicates(head1);
	while (pp != NULL)
	{
		cout << pp->val << " ";
		pp = pp->next;
	}
	cout << endl;
	system("pause");
	return 0;
}
////////////////

