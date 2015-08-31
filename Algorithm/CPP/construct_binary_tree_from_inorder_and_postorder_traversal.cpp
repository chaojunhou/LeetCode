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
	TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
		if (postorder.empty()) return nullptr;
		TreeNode* root = new TreeNode(postorder.back());
		auto tmp = find(inorder.begin(), inorder.end(), postorder.back());
		postorder.erase(postorder.end()-1);

		if ( tmp < (inorder.end()-1))
		{
			auto Right = vector<int>(tmp + 1, inorder.end());
			root->right = buildTree(Right, postorder);

		}
		if (tmp > inorder.begin())
		{
			auto Left = vector<int>(inorder.begin(), tmp);
			root->left = buildTree(Left, postorder);

		}
		return root;

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
	root1->left->left = new TreeNode(11);
	root1->right->left = new TreeNode(13);
	root1->right->right = new TreeNode(4);
	root1->left->left->left = new TreeNode(7);
	root1->left->left->right = new TreeNode(2);
	root1->right->right->left =new TreeNode(5);
	root1->right->right->right = new TreeNode(1);
	vector<int> postorder = {2, 3,1};
	vector<int> inorder = { 2, 1, 3 };
	sol.print(sol.buildTree(inorder, postorder));
	cout << endl;
	system("pause");
	return 0;
}

