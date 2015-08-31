/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if(!root || root==p || root==q) return root;
        auto Left = lowestCommonAncestor(root->left,p,q);
        auto Right = lowestCommonAncestor(root->right,p,q);
        if(Left&&Right) return root;
        else if(Left) return Left;
        else return Right;
    }
};
