
# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
using namespace std;



struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	bool isValidBST(TreeNode* root) {
		if (!root) return true;
		TreeNode* pre = NULL;
		return check(root, pre);
	}
	bool check(TreeNode* root, TreeNode* &pre)
	{
		if (!root) return true;
		if (check(root->left, pre))
		{
			if (pre && pre->val >= root->val)
			{

				return false;
			}
			pre = root;
			return check(root->right, pre);
		}
		return false;
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

int  main()
{
	Solution sol;
	TreeNode *root1;
	root1 = new TreeNode(5);
	//root1->left = new  TreeNode(5);
	//root1->right = new TreeNode(8);
	//root1->left->left = new TreeNode(11);
	//root1->left->right = new TreeNode(13);
	//root1->right->left = new TreeNode(4);
	//root1->left->left->left = new TreeNode(7);
	//root1->left->left->right = new TreeNode(2);
	//root1->right->right->left =new TreeNode(5);
	//root1->right->right->right = new TreeNode(1);
	vector<int> postorder = {2, 3,1};
	vector<int> inorder = { 2, 1, 3 };
	vector<int> nums = { 1, 3, 5, 6, 7 };
	cout << sol.isValidBST(root1) << endl;

	system("pause");
	return 0;
}

