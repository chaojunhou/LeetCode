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
	vector<int> postorderTraversal(TreeNode* root){  // based on the root right left ,then just reverse the result
		stack<TreeNode* > Stack; 
		vector<int> res;
		if (root)
		{
			Stack.push(root);
			while (!Stack.empty())
			{
				auto p = Stack.top();
				Stack.pop();
				res.push_back(p->val);
				if (p->left) Stack.push(p->left);
				if (p->right) Stack.push(p->right);
			}
		}
		reverse(res.begin(), res.end());
		return res;
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

	sol.printTreeInOrder(root1);
	cout << endl;
	for (auto k : sol.inorderTraversal(root1)) cout << k << " ";
	cout << endl;
	cout << "__________" << endl;
	sol.printTreePreOrder(root1);
	cout << endl;
	for (auto k : sol.preorderTraversal2(root1)) cout << k << " ";
	cout << endl;
	system("pause");
	return 0;
}
