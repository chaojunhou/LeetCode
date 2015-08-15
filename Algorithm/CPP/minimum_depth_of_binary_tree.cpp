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
	int minDepth(TreeNode* root)
	{
		if (!root) return 0;
		if (root->left && !root->right)return minDepth(root->left) + 1;
		if (root->right && !root->left) return minDepth(root->right) + 1;
		return min(minDepth(root->left), minDepth(root->right)) + 1;

	}


};
int  main()
{
	Solution sol;
	TreeNode *root;
	root = new TreeNode(-1);
	root->left =new  TreeNode(2);
	//root->right = new TreeNode(3);
	//root->left->left = new TreeNode(4);

	cout << sol.minDepth(root);
	cout<< endl;
	cin.get();
	return 0;
}
