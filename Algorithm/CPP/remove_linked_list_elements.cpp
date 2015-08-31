# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;


struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* removeElements(ListNode* head, int val) {
		ListNode* dummy = new ListNode(-1);
		dummy->next = head;
		auto p = dummy;
		auto q = head;
		while (q)
		{
			if (q->val == val)
			{
				auto tmp = q;
				q = q->next;
				p->next = q;
				delete tmp;

				
			}
			else
			{
				p = q;
				q = q->next;
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
	vector<int> vec{ 1 };//2
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

	auto qq = sol.removeElements(head1, 1);
	while (qq)
	{
		cout << qq->val << " " << endl;
		qq = qq->next;
	}
	system("pause");
	return 0;
}


