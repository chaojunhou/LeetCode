# include <iostream>
# include <string>
# include <stdlib.h>
# include <algorithm>
# include <vector>
# include <unordered_map>
# include <map>
using namespace std;

class Solution {
public:
    bool isPalindrome(string s) {
		int left = 0;
		int right = s.size() - 1;
		while (left <=
			right)
		{
			while ((ispunct(s[left]) || s[left] == ' ') ){ left++; if (left == s.size()) return true; }
			
			while ((ispunct(s[right]) || s[right] == ' ')){ right--; if (right < left) return true; }
		
			if (tolower(s[left]) == tolower(s[right]))
			{
				left++;
				right--;
			}
			else
			{
				return false;
			}

		}
		return true;
    }
};

int  main()
{
	Solution sol;

	string path = "/a/./b/../../c/";
	//path = "/";
	path = "/...";
	path = "A man, a plan, a canal: Panama";
	path = " ";
	path = "1a2";

	cout << sol.isPalindrome(path) << endl;
	system("pause");
	return 0;
}
