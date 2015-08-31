# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	    static 	bool myCmp(ListNode* p, ListNode* q)
	{
		return p->val > q->val;
	}
	ListNode* mergeKLists(vector<ListNode*>& lists) {
		ListNode* dummy = new ListNode(-1);
		auto p = dummy;
		vector<ListNode*> vec;
		for (auto l : lists)
		{
			if (l) vec.push_back(l);
		}
		make_heap(vec.begin(), vec.end(), myCmp);
		while (!vec.empty())
		{
			p->next = vec.front();
			pop_heap(vec.begin(), vec.end(), myCmp);
			vec.pop_back();
			p = p->next;
			if (p->next)
			{
				vec.push_back(p->next);
				push_heap(vec.begin(), vec.end(), myCmp);
			}
		}
		return dummy->next;
	}
	/////////////////////////////////////
	struct mycompare{
		bool operator()(ListNode* p, ListNode* q)
		{
			return p->val > q->val;
		}
	};
	ListNode* mergeKLists(vector<ListNode*>& lists) 
	{
		ListNode* dummy = new ListNode(-1);
		auto p = dummy;
		priority_queue<ListNode*, vector<ListNode*>, mycompare> Heap;
		for (auto list : lists)
		{
			if (list) Heap.push(list);
		}
		if (Heap.empty())return NULL;

		while (!Heap.empty())
		{
			p->next = Heap.top();
			Heap.pop();
			p = p->next;
			if (p->next)
			{
				Heap.push(p->next);
			}
		}
		return dummy->next;
	}
};
////////////////

