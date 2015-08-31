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


 class Solution {
	public:
		int compareVersion(string version1, string version2) {
			int m = version1.size();
			int n = version2.size();
			int i = 0, j = 0;
			int num1 = 0, num2 = 0;
			while (i < m || j < n)
			{
				while ((i < m) && (version1[i] != '.'))
				{

					num1 = num1 * 10 + (version1[i] - '0');
					i++;
				}
				while ((j < n) && (version2[j] != '.'))
				{
					num2 = num2 * 10 + (version2[j] - '0');
					j++;
				}

				if (num1 > num2) return 1;
				else if (num1 < num2)return -1;
				num1 = 0;
				num2 = 0;
				if ((i == m) && (j == n))
				{
					return 0;
				}
				i++;
				j++;
			}
			return 0;
		}
	int compareVersion1(string version1, string version2) {
		for (; version2 != version1; version1 = nextVersion(version1), version2 = nextVersion(version2))
		{
			int gap = stoi(version1) - stoi(version2);
			if (gap != 0)
				return gap > 0 ? 1 : -1;

		}
		return 0;
	}
	string nextVersion(string& s)
	{
		int n = s.size();
		for (int i = 0; i < n; ++i)
		{
			if (s[i] == '.')
				return s.substr(i + 1);
		}
		return "0";
	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 4, 1, 2, 7, 5, 3, 1};
	//nums = { 1, 2 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	string word1 = "vintner";
	string word2 = "writers";

	string s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT";
	int n = sol.compareVersion("1.0", "1");
	cout<<n<<endl;
	
	cout<<endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}

