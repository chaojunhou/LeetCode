# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	bool isSameTree(TreeNode* p, TreeNode* q)
	{
		if (p == NULL && q == NULL) return true;
		if (p && q)
		{
			if (p->val == q->val)
			{
				return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
			}
			return false;
		}
		return false;


	}


};
int  main()
{
	Solution sol;
	TreeNode *root1,*root2;
	root1 = new TreeNode(-1);
	root1->left =new  TreeNode(2);
	root2 = new TreeNode(-1);
	root2->left = new TreeNode(2);

	//root->right = new TreeNode(3);
	//root->left->left = new TreeNode(4);

	cout << sol.isSameTree(root1,root2);
	cout<< endl;
	cin.get();
	return 0;
}
