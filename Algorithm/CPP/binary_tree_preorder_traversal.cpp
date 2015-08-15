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
	vector<int> preorderTraversal(TreeNode* root)
	{
		vector<int> res;
		stack<TreeNode*> Stack;
		if (root)
		{
			Stack.push(root);
			while (!Stack.empty())
			{
				auto p = Stack.top();
				res.push_back(p->val);
				Stack.pop();
				if (p->right)   Stack.push(p->right);
				if (p->left)	Stack.push(p->left);
			}
		}
		return res;
	}
	void printTree(TreeNode* root)
	{
		if (root)
		{
			cout << root->val << " ";
			printTree(root->left);
			
			printTree(root->right);
		}
	}
};
int  main()
{
	Solution sol;	
	TreeNode *root1;
	root1 = new TreeNode(4);
	root1->left =new  TreeNode(2);
	root1->right = new TreeNode(5);
	root1->left->left = new TreeNode(1);
	root1->left->right = new TreeNode(3);
	sol.printTree(root1);
	cout << endl;
	for (auto k:sol.preorderTraversal(root1)) cout<< k<< " ";
	cout << endl;
	
	cout<< endl;
	system("pause");
	return 0;
}
