class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        vector<int> res;
        stack<TreeNode* > Stack;
        TreeNode* pNode = root;
        while (!Stack.empty() || pNode)
        {
            if (pNode)
            {
                Stack.push(pNode);
                pNode = pNode->left;
            }
            else {
                pNode = Stack.top();
                res.push_back(pNode->val);
                Stack.pop();
                pNode = pNode->right;
            }
        }
        return res;       
    }
        vector<int> inorderTraversal1(TreeNode* root) {
        vector<int> res;
        auto pNode = root;
        while (pNode)
        {
            if (!pNode->left)
            {
                res.push_back(pNode->val);
                pNode = pNode->right;
            } else {
                auto pre = pNode->left;
                while (pre->right && pre->right != pNode)
                    pre = pre->right;
                if (!pre->right)
                {
                    pre->right = pNode;
                    pNode = pNode->left;
                }
                else {
                    res.push_back(pNode->val);
                    pre->right = NULL;
                    pNode = pNode->right;
                }
            }
        }
        return res;      
    }
};

