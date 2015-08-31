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
	TreeNode* sortedArrayToBST(vector<int>& nums) {
		if (nums.empty()) return nullptr;
		int mid = (nums.size() - 1) / 2;
		auto root = new TreeNode(nums[mid]);
		vector<int> Left = vector<int>(nums.begin(), nums.begin() + mid);
		root->left = sortedArrayToBST(Left);
		vector<int> Right = vector<int>(nums.begin() + mid + 1, nums.end());
		root->right = sortedArrayToBST(Right);
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
	root1->left = new  TreeNode(4);
	root1->right = new TreeNode(8);
	root1->left->left = new TreeNode(11);
	root1->right->left = new TreeNode(13);
	root1->right->right = new TreeNode(4);
	root1->left->left->left = new TreeNode(7);
	root1->left->left->right = new TreeNode(2);
	root1->right->right->left =new TreeNode(5);
	root1->right->right->right = new TreeNode(1);
	vector<int> postorder = {2, 3,1};
	vector<int> inorder = { 2, 1, 3 };
	vector<int> nums = { 1, 3, 5, 6, 7 };
	sol.print(sol.sortedArrayToBST(nums));
	cout << endl;
	system("pause");
	return 0;
}
