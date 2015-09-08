# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	unordered_map<UndirectedGraphNode*, UndirectedGraphNode*>myMap;
	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) {
	
		if (!node) return node;
		return dfs(node);
	}

	UndirectedGraphNode* dfs(UndirectedGraphNode* node)
		{
			if (myMap.find(node) != myMap.end())
				return myMap[node];
			UndirectedGraphNode* root = new UndirectedGraphNode(node->label);
			myMap[node] = root;
			for (auto neightbor : node->neighbors)
			{
				root->neighbors.push_back(	dfs(neightbor));
			}
		return root;
	}
};

