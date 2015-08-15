# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
# include <queue>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	TreeNode* invertTree1(TreeNode* root) 
	{
		if (root)
		{
			TreeNode* left = root->left;
			TreeNode* right = root->right;
			root->left = right;
			root->right = left;
			invertTree1(root->left);
			invertTree1(root->right);
			return root;  // add this wiil take less time 
		}

		return root;
	}

	TreeNode* invertTree2(TreeNode* root)
	{
		if (root)
		{

			auto tmp = invertTree(root->right);
			
			root->right = invertTree(root->left);
			root->left = tmp;

			//root->left = invertTree(root->right);
			//root->right = invertTree(root->left);
			return root;
		}
		return root;
	}

	TreeNode* invertTree(TreeNode* root)
	{
		queue<TreeNode *> Queue;
		if (root)
		{
			Queue.push(root);
			while (!Queue.empty())
			{
				auto p = Queue.front();
				Queue.pop();
				auto left = p->left;
				p->left = p->right;
				p->right = left;
				if (p->left)	Queue.push(p->left);
				if (p->right)  Queue.push(p->right);
			}
			return root;
		}
	}

	void printTree(TreeNode* root)
	{
		if (root)
		{
			cout << root->val;
			printTree(root->left);
			printTree(root->right);
		}
	}
};
int  main()
{
	Solution sol;	
	TreeNode *root1;
	root1 = new TreeNode(-1);
	root1->left =new  TreeNode(2);
	root1->right = new TreeNode(3);
	root1->left->left = new TreeNode(1);
	root1->left->right = new TreeNode(4);

	sol.invertTree(root1);
	sol.printTree(root1);
	cout<< endl;
	cin.get();
	return 0;
}


