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
	ListNode *addTwoNumbers(ListNode* l1, ListNode * l2) 
	{
		auto dummy = new ListNode(-1);
		auto q = dummy;
		auto carry = 0;
		while (l1 && l2)
		{
			q->next = new ListNode((l1->val + l2->val + carry) % 10);
			carry = (l1->val + l2->val+carry) / 10;
			q = q->next;
			l1 = l1->next;
			l2 = l2->next;
		}
		while (l1)
		{
			q->next = new ListNode((l1->val + carry)%10);
			carry = (l1->val+carry)/10;
			l1 = l1->next;
			q = q->next;
			if (carry == 0)
			{
				q->next = l1;
				return dummy->next;
			}
		}
		while (l2)
		{
			q->next = new ListNode((l2->val + carry)%10);
			carry = (l2->val + carry) / 10;
			l2 = l2->next;
			q = q->next;
			if (carry == 0)
			{
				q->next = l2;
				return dummy->next;
			}
		}
		if (carry)
		{
			q->next = new ListNode(1);
			q = q->next;
		}
		q->next = NULL;
		return dummy->next;		
	}
};


int main()
{
	ListNode *heada = new ListNode(2);
	auto p = heada;
	vector<int> vec{ 4,5,9 };
	for (auto x : vec)
	{
		p->next = new ListNode(x);
		p = p->next;
	}
	p->next = NULL;
	auto headb = new ListNode(5);
	auto q = headb;
	q->next = new ListNode(6);
	q = q->next;
	q->next = new ListNode(4);
	q->next->next = NULL;

	solution sol;
	auto tmp = sol.addTwoNumbers(heada, headb);
	while (tmp)
	{
		cout << tmp->val << endl;
		tmp = tmp ->next;
	}
	
	cin.get();
	return 0;
}
