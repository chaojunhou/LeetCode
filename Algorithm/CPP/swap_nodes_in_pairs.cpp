# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
# include <algorithm>
# include <time.h>
# include<random>
# include <queue>
#include <stdint.h>

using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};

class Solution {
public:
	ListNode* swapPairs(ListNode* head) {
		if (!head || !head->next) return head;
		auto dummy = new ListNode(-1);

		auto p = dummy;
		auto q = head;
		while (q && q->next )
		{
			auto nxt = q->next;
			p->next = nxt;
			q->next = nxt->next;
			
			nxt->next = q;
			p = nxt->next;
			q = q->next;
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

	auto pp = sol.swapPairs(head1);
	while (pp != NULL)
	{
		cout << pp->val << " ";
		pp = pp->next;
	}
	cout << endl;
	system("pause");
	return 0;
}
