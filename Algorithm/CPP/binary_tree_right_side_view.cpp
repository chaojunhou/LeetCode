# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <stack>
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
	vector<int> rightSideView(TreeNode* root) 
	{
		vector<int> res;
		dfs(res, root, 1);
		return res;

	}
	void dfs(vector<int> & res, TreeNode* root, int depth)
	{
		if (root)
		{
			if (res.size() < depth) // the new level, should build a new vector<int> to the res 
				res.push_back(root->val);
			dfs(res, root->right, depth + 1);
			dfs(res, root->left, depth + 1);
			
		}
	}

};
int  main()
{
	Solution sol;
	TreeNode *root1;
	root1 = new TreeNode(4);
	root1->left = new  TreeNode(2);
	root1->right = new TreeNode(5);
	root1->left->left = new TreeNode(1);
	root1->left->right = new TreeNode(3);
	for (auto x : sol.rightSideView(root1))
	{

		cout << x << " ";

	}
	cout << endl;
	system("pause");
	return 0;
}
