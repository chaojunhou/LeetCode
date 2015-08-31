# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;



class Solution {
public:
	void flatten(TreeNode* root) {
		if (!root) return;
		auto p = root->left;
		if (p)
		{
			while (p->right) p = p->right;
			p->right = root->right;
			root->right = root->left;
			root->left = NULL;
		}
		flatten(root->right);

	}
		void flatten1(TreeNode* root)
	{
		if (!root) return; // find the right most tree of the left subtree then point to the right subtree 
		while (root)
		{
			auto p = root->left;
			if (p)
			{
				while (p->right) p = p->right;
				p->right = root->right;
				root->right = root->left;
				root->left = NULL;
			}
			root = root->right;
		}
	}
	void print(TreeNode* root)
	{
		if (root)
		{
			cout << root->val << " ";
			print(root->left);
			print(root->right);
		}
	}

};
