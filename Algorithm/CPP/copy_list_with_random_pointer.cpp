# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;



 struct RandomListNode {
      int label;
      RandomListNode *next, *random;
      RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 };

class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
   	std::unordered_map< RandomListNode*, RandomListNode*> map;
    	RandomListNode* dummy = new RandomListNode(-1);
        dummy->next = head;
        auto p = head;
        auto q = dummy;
    	while(p)
    	{
    		q->next = new RandomListNode(p->label);
    		map[p] = q->next;
    		p = p->next;
    		q = q->next;
		}
		p = head;
		q = dummy;
        while(p)
        {
        	q->next->random = map[p->random];
        	p = p->next;
        	q = q->next;        	
		}
        return dummy->next;        
    }
};

