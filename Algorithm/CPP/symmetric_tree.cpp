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
	bool isSymmetric1(TreeNode* root)
	{
		if (root)		return check(root->left, root->right);
		return true;
	}

	bool check(TreeNode* left, TreeNode* right)
	{
		if (!left && !right) return true;
		if (left && right && left->val == right->val) return check(left->right, right->left) && check(left->left,right->right);
		return false;
	}
	bool isSymmetric(TreeNode* root)
	{
		if (!root) return true;
		queue<TreeNode*> leftSubtree, rightSubtree;

		leftSubtree.push(root->left);
		rightSubtree.push(root->right);
		while (!leftSubtree.empty() && !rightSubtree.empty())
		{
			auto p = leftSubtree.front();
			leftSubtree.pop();
			auto q = rightSubtree.front();
			rightSubtree.pop();
			if (p == NULL && q == NULL) continue;
			if (p == NULL ||q == NULL) return false;
			if (p->val != q->val) // left subtree is null or right subtree is null
				return false;
			leftSubtree.push(p->left);
			leftSubtree.push(p->right);
			rightSubtree.push(q->right);
			rightSubtree.push(q->left);
		}
		return true;
	}
};
int  main()
{
	Solution sol;	
	TreeNode *root1,*root2;
	root1 = new TreeNode(-1);
	root1->left =new  TreeNode(2);
	root1->right = new TreeNode(2);
	root1->left->left = new TreeNode(1);
	root2 = new TreeNode(-1);
	root2->left = new TreeNode(2);

	//root->right = new TreeNode(3);
	//root->left->left = new TreeNode(4);

	cout << sol.isSymmetric(root1);
	cout<< endl;
	cin.get();
	return 0;
}


