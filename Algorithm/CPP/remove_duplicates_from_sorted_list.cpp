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
	ListNode* deleteDuplicates(ListNode* head) {
		auto dummy = new ListNode(-1);
		dummy->next = head;
		auto p = head;
		auto q = head->next;
		while (q)
		{
			if (p->val != q->val)
			{
				p = p->next;
				q = q->next;
			}
			else
			{
				p->next = q->next;
				auto tmp = q;
				delete tmp;
				q = p->next;
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
	vector<int> vec{ 1,3,2,5,6};//2
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
