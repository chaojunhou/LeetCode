# include <stdio.h>
# include <iostream>
# include <vector>
using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
	TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	void recoverTree(TreeNode* root) {
		inOrder(root);
		if (p)
		{
			int tmp = p->val;
			p->val = q->val;
			q->val = tmp;
		}

	}
	void inOrder(TreeNode* root )
	{
		if (root)
		{
			inOrder(root->left );
			if (pre && pre->val > root->val)
			{
				q = root;
				if (p == NULL)
				{
					p = pre;
				}
			}
			pre = root;
			inOrder(root->right);
		}
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
private:
	TreeNode* p = NULL;
	TreeNode* q = NULL;
	TreeNode* pre = NULL;
};

int main()
{
	Solution sol;
	TreeNode* root = new TreeNode(1);
	root->left = new TreeNode(2);
	root->right = new TreeNode(3);
	sol.recoverTree(root);
	sol.printTree(root);
	system("pause");

}
