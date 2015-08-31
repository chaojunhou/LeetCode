
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

class BSTIterator {
public:
	BSTIterator(TreeNode *root) {
		auto p = root;
		while (p)
		{
			myStack.push(p);
			p = p->left;
		}

	}

	/** @return whether we have a next smallest number */
	bool hasNext() {
		return !myStack.empty();
	}

	/** @return the next smallest number */
	int next() {
		auto p = myStack.top();
		myStack.pop();
		int top = p->val;
		p = p->right;
		while (p)
		{
			myStack.push(p);
			p = p->left;
		}
		return top;
	}
private:
	stack<TreeNode*> myStack;
};


int  main()
{
	TreeNode *root1;
	root1 = new TreeNode(5);
	root1->left = new  TreeNode(4);
	root1->right = new TreeNode(8);
	//root1->left->left = new TreeNode(3);
	BSTIterator sol = BSTIterator(root1);
	//root1->left->right = new TreeNode(13);
	//root1->right->left = new TreeNode(4);
	//root1->left->left->left = new TreeNode(7);
	//root1->left->left->right = new TreeNode(2);
	//root1->right->right->left =new TreeNode(5);
	//root1->right->right->right = new TreeNode(1);

	while (sol.hasNext())
		cout << sol.next()<<" ";

	system("pause");
	return 0;
}


