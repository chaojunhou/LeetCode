# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
# include <vector>
# include <unordered_map>
# include <map>
using namespace std;

struct ListNode {
	int val;
	ListNode *next;
	ListNode(int x) : val(x), next(NULL) {}
};
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
public:
	TreeNode* sortedListToBST(ListNode* head)
	{
		if (!head) return NULL;
		if (!head->next) return new TreeNode(head->val);
		auto slow = head;
		auto fast = head->next->next;
		while (fast && fast->next)
		{ 
			slow = slow->next;
			fast = fast->next->next;
		}
		
		auto nRoot = slow->next;
		auto root = new TreeNode(nRoot->val);
		slow->next = NULL;
		root->left = sortedListToBST(head);
		root->right = sortedListToBST(nRoot->next);
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
	//root1->left = new  TreeNode(5);
	//root1->right = new TreeNode(8);
	//root1->left->left = new TreeNode(11);
	//root1->left->right = new TreeNode(13);
	//root1->right->left = new TreeNode(4);
	//root1->left->left->left = new TreeNode(7);
	//root1->left->left->right = new TreeNode(2);
	//root1->right->right->left =new TreeNode(5);
	//root1->right->right->right = new TreeNode(1);
	ListNode *head1 = new ListNode(1);
	ListNode *head2 = new ListNode(-2);
	auto p = head1;
	auto q = head2;
	vector<int> vec{ 2,3};//2
	for (auto x : vec)
	{
		p->next = new ListNode(x);
		p = p->next;
	}
	p->next = NULL;
	sol.print(sol.sortedListToBST(head1));

	system("pause");
	return 0;
}
