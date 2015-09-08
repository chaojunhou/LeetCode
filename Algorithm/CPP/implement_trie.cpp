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
	string word;
	TrieNode() {
		memset(children, 0, sizeof(children));
	}
};
class Trie {
public:
	Trie() {
		root = new TrieNode();
	}

	// Inserts a word into the trie.
	void insert(string word) {
		auto p = root;
		for (auto ch : word)
		{
			cout << (ch) << endl;
			if (p->children[ch-'a']==NULL)
			{
				p->children[ch - 'a'] = new TrieNode();
			}
			p = p->children[ch - 'a'];
		}
		p->word = word;
	}

	// Returns if the word is in the trie.
	bool search(string word) {
		auto p = root;
		for (auto ch : word)
		{
			if (!p->children[ch - 'a']) return false;
			p = p->children[ch - 'a'];
		}
		return p->word == word;

	}

	// Returns if there is any word in the trie
	// that starts with the given prefix.
	bool startsWith(string prefix) {
		auto p = root;
		for (auto ch : prefix)
		{
			if (!p->children[ch - 'a']) return false;
			p = p->children[ch - 'a'];
		}
		return true;
	}

private:
	TrieNode* root;
};
