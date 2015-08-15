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
	int maxDepth(TreeNode* root)
	{
		int res = 0;
		if (root)
		{
			res = max(maxDepth(root->left), maxDepth(root->right)) + 1;
		}
		return res ;
	}


};
int  main()
{
	Solution sol;
	TreeNode *root;
	root = new TreeNode(-1);
	root->left =new  TreeNode(2);
	root->right = new TreeNode(3);
	root->left->left = new TreeNode(4);

	cout << sol.maxDepth(root);
	cout<< endl;
	cin.get();
	return 0;
}
