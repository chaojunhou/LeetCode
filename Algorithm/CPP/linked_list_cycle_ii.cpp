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
	ListNode *detectCycle(ListNode *head)
	{
		if (!head) return NULL;

		auto p = head;
		auto q = p;
		while (p)
		{
			if (p->next)
				p = p->next->next;
			else return NULL;
			q = q->next;
			if (p == q)
			{
				p = head;
				while (p != q)
				{
					q = q->next;
					p = p->next;
				}
				return p;
			}
		}
		return NULL;
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
	auto q = sol.detectCycle(head);
	cout << q;
	//cout << sol.reverseList(head);
	cin.get();
	return 0;
}
