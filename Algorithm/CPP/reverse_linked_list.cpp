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
	ListNode* reverseList1(ListNode* head) {
		if (head == NULL || head->next == NULL)
			return head;
		auto q = reverseList1(head->next); // ·ÀÖ¹¶ÏÁ´
		head->next->next = head;
		head->next = NULL;
		return q;
	}
	ListNode* reverseList(ListNode* head){
		if (head == NULL || head->next == NULL)
			return head;
		auto dummy = new ListNode(-1);
		auto q = dummy;
		q->next = NULL;
		while (head)
		{
			auto tmp = head->next;
			head->next = q->next;
			q->next = head;
			head = tmp;
		}
		return dummy->next;
	}
};


int main()
{
	ListNode *head = new ListNode(-1);
	auto p = head;
	vector<int> vec{ 1, 2, 3, 5, 9, 8 };
	for (auto x : vec)
	{
		p->next = new ListNode(x);
		p = p->next;
	}
	p->next = NULL;
	//p = root->next;
	//while (p!=NULL)
	//{
	//	cout << p->val << endl;
	//	p = p->next;
	//}
	solution sol;
	auto q = sol.reverseList(head);
	while (q)
	{
		cout << q->val;
		q = q->next;
	}
	//cout << sol.reverseList(head);
	cin.get();
	return 0;
}
