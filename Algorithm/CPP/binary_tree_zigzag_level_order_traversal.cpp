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
	vector<vector<int>> zigzagLevelOrder(TreeNode* root)
	{
		vector<vector<int>> res;
		if (!root) return res;
		int nodesInCurrentLevel = 1;
		int nodesInNextLevel = 0;
		queue<TreeNode* > Queue;
		Queue.push(root);
		vector<int> vec;
		int depth = 1;
		while (!Queue.empty())
		{
			auto p = Queue.front();
			Queue.pop();

			vec.push_back(p->val);
			nodesInCurrentLevel--;
			if (p)
			{
				if (p->left)
				{
					Queue.push(p->left);
					nodesInNextLevel++;
				}
				if (p->right)
				{
					Queue.push(p->right);
					nodesInNextLevel++;
				}
			}
			if (nodesInCurrentLevel == 0)
			{
				if (depth%2)			res.push_back(vec);
				else res.push_back(vector<int> (vec.rbegin(), vec.rend()));
				nodesInCurrentLevel = nodesInNextLevel;
				nodesInNextLevel = 0;
				vec = {};
				depth++;
			}
		}
		return res;
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
	//root1->left->left->left = new TreeNode(7);
	//root1->left->left->right = new TreeNode(2);
	//root1->right->right->left =new TreeNode(5);
	//root1->right->right->right = new TreeNode(1);
	for (auto k : sol.zigzagLevelOrder(root1))
	{
		for (auto x:k)	cout << x << " ";
		cout << endl;
	}
	cout << endl;
	system("pause");
	return 0;
}
