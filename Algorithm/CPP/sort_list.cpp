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
	ListNode* sortList(ListNode* head) {
		if (!head || !head->next) return head;
		auto slow = head;
		auto fast = head;
		
		while (fast->next && fast->next->next)
		{
			slow = slow->next;
			fast = fast->next->next;
		}
		auto head2 = slow->next;
		slow->next = NULL;
		return merge(sortList(head), sortList(head2));
	}
	ListNode* merge(ListNode* head1, ListNode * head2)
	{
		ListNode* dummy = new ListNode(-1);
		auto p = dummy;
		while (head1&&head2)
		{
			if (head1->val < head2->val)
			{
				p->next = head1;
				head1 = head1->next;
			}
			else
			{
				p->next = head2;
				head2 = head2->next;
			}
			p = p->next;
		}
		if (head1) p->next = head1;
		if (head2) p->next = head2;
		return dummy->next;
	}

}; 

int main()
{
	Solution sol;
	ListNode* head = new ListNode(3);
	vector<int> nums = { 2, 4, 1 };
	auto p = head;
	for (auto num : nums)
	{
		p->next = new ListNode(num);
		p = p->next;
	}
	p->next = NULL;
	auto q = sol.sortList(head);
	while (q)
	{
		cout << q->val << " ";
		q = q->next;
	}
	cout << endl;
	system("pause");
	return 0;
}
