# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
    void connect(TreeLinkNode *root) {
		if (!root) return;
		if (root && root->left)
		{
			    root->left->next = root->right;
				if (root->next)
				{
					root->right->next = root->next->left;
				}
				else
				{
				   // root->right->next = NULL;
					
				}
			connect(root->left);
			connect(root->right);
		}   
    }
};
