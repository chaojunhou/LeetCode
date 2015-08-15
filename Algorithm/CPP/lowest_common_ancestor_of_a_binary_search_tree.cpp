//# include <iostream>
//# include <stdlib.h>
//# include <stdio.h>
//using namespace std;
//struct TreeNode {
//	int val;
//	TreeNode *left;
//	TreeNode *right;
//	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
//};
//
//class Solution {
//public:
//	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
//		if (root == NULL) return NULL;
//		if (root->val > p->val && root->val > q->val) return lowestCommonAncestor(root->left, p, q);
//
//		if (root->val < p->val && root->val < q->val) return lowestCommonAncestor(root->right, p, q);
//
//		return root;
//
//	}
//};
//
//int main()
//{
//	auto root = new TreeNode(20);
//	root->left = new TreeNode(8);
//	root->right = new TreeNode(22);
//	root->left->left = new TreeNode(4);
//	root->left->right = new TreeNode(12);
//	root->left->right->left = new TreeNode(10);
//	root->left->right->right = new TreeNode(14);
//	int n1 = 10, n2 = 14;
//	Solution sol;
//	auto t = sol.lowestCommonAncestor(root, new TreeNode(n1), new TreeNode(n2));
//	printf("LCA of %d and %d is %d \n", n1, n2, t->val);
//
//	n1 = 14, n2 = 8;
//	t = sol.lowestCommonAncestor(root, new TreeNode(n1), new TreeNode(n2));
//	 printf("LCA of %d and %d is %d \n", n1, n2, t->val);
//
//	n1 = 10, n2 = 22;
//	t = sol.lowestCommonAncestor(root, new TreeNode(n1), new TreeNode(n2));
//	printf("LCA of %d and %d is %d \n", n1, n2, t->val);
//
//	cin.get();
//	return 0;
//}
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
	TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) 
	{
		if (p->val < root->val && q->val < root->val)
		{
			return lowestCommonAncestor(root->left, p, q);
		}
		if (p->val > root->val && q->val > root->val)
		{
			return lowestCommonAncestor(root->right, p, q);
		}
		return root;
	}

	void printTree(TreeNode* root)
	{
		if (root)
		{
			printTree(root->left);
			cout << root->val;
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

	cout << sol.lowestCommonAncestor(root1, root1->left->right, root1->left->left)->val << endl;
	//sol.printTree(root1);
	cout<< endl;
	system("pause");
	return 0;
}



