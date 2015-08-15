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
	ListNode *getintersectionnode(ListNode *heada, ListNode *headb) {
		if (heada == NULL | headb == NULL)
		{
			return NULL;
		}
		auto p = heada;
		auto q = headb;
		while ( p != q)
		{
			p = p->next;
			q = q->next;
			if (p==q) return p;
			if (p == NULL)
			{
				p = headb;
			}
			if (q == NULL)
				q = heada;
		}
		return p;

	}
};


int main()
{
	ListNode *heada = new ListNode(-1);
	auto p = heada;
	vector<int> vec{ 1, 2, 3, 5,9,8 };
	for (auto x : vec)
	{
		p->next = new ListNode(x);
		p = p->next;
	}
	p->next = NULL;
	auto headb = new ListNode(0);
	auto q = headb;
	q->next = new ListNode(7);
	q = q->next;
	q->next = heada->next->next->next;
	//p = root->next;
	//while (p!=NULL)
	//{
	//	cout << p->val << endl;
	//	p = p->next;
	//}
	solution sol;
	cout<<sol.getintersectionnode(heada,headb)->val;
	cin.get();
	return 0;
}
