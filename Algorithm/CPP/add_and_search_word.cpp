# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <unordered_map>
# include <cctype>
# include <algorithm>
# include <time.h>
using namespace std;

class TrieNode {
public:
	// Initialize your data structure here.
	TrieNode* children[26];
	bool isEnd;
	TrieNode() {
		memset(children, NULL, sizeof(children));
		isEnd = false;
	}
};

class WordDictionary{
private:
	TrieNode* root;
public:
	WordDictionary(){
		root = new TrieNode();
	}
	// Adds a word into the data structure.
	void addWord(string word) {
		auto p = root;
		for (auto ch : word)
		{
			if (p->children[ch - 'a'] == NULL)
				p->children[ch - 'a'] = new TrieNode();
			p = p->children[ch - 'a'];
		}
		p->isEnd = true;
	}

	// Returns if the word is in the data structure. A word could
	// contain the dot character '.' to represent any one letter.

	bool query(string word, TrieNode* root)
	{
		cout << word << endl;
		auto p = root;
		for (int i = 0; i < word.size(); i++){
			if (p&&word[i] != '.')
				p = p->children[word[i] - 'a'];
			else if (p && word[i] == '.')
			{
				auto tmp = p;
				for (int j = 0; j < 26; j++)
				{
					p = tmp->children[j];
					if (query(word.substr(i + 1), p))
						return true;
				}	
			}
			else break;
		}
		return p&&p->isEnd;
	} 
	bool search(string word) {
		return query(word, root);
	}
};


// Your Trie object will be instantiated and called as such:
int main()
{
	WordDictionary wd;
	wd.addWord("bad");
	wd.addWord("dad");
	wd.addWord("mad");

	cout<<wd.search(".ad")<<endl;
	cout << wd.search("b..") << endl;
	cin.get();
	return 0;
}


