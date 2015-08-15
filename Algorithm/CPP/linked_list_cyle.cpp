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
	bool hasCycle(ListNode *head)
	{
		if (!head) return false;

		auto p = head;
		auto q = p;

		while (p)
		{
			if (p->next)
				p = p->next->next;
			else return false;
			q = q->next;
			if (p == q)
				return true;
		}
		return false;
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
	auto q = sol.hasCycle(head);
	cout << q;
	//cout << sol.reverseList(head);
	cin.get();
	return 0;
}
