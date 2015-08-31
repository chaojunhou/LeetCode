# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;


struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	int kthSmallest(TreeNode* root, int k) {
		int res = 0;
		int count = 0;
		inorder(root, k, count,res);
		return res;
	}
	void inorder(TreeNode* root, int k, int& count,int& res)
	{
		if (root)
		{
			
			inorder(root->left, k, count,res);
			count += 1;
			if (count == k)
			{
				res = root->val;
				return;
			}
			inorder(root->right, k, count, res);
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

int  main()
{
	Solution sol;
	TreeNode *root1;
	root1 = new TreeNode(5);
	root1->left = new  TreeNode(4);
	root1->right = new TreeNode(8);
	root1->left->left = new TreeNode(3);
	//root1->left->right = new TreeNode(13);
	//root1->right->left = new TreeNode(4);
	//root1->left->left->left = new TreeNode(7);
	//root1->left->left->right = new TreeNode(2);
	//root1->right->right->left =new TreeNode(5);
	//root1->right->right->right = new TreeNode(1);

	cout << sol.kthSmallest(root1,4) << endl;

	system("pause");
	return 0;
}
