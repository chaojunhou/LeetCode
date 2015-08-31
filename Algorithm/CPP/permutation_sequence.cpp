# include <stdio.h>
# include <iostream>
# include <vector>
# include <array>
# include <string.h>

using namespace std;

class Solution {
public:
	string getPermutation(int n, int k)
	{
		int fact = 1;
		k--;
		string s(n,'0');
		string res;
		for (int i = 1; i <= n; i++)
		{
			fact *= i;
			s[i-1] += i;
		}
		int j;
		for (int i = 0;i < n; i++)
		{
			//fact = fact / (n - i);
			//j =i+k / fact;
			//res += s[j];
			////char tmp = s[j];
			//for (; j > i; j--)
			//	s[j] = s[j-1];
			//k = k%fact;
			////s[i] = tmp;
			fact /= (n - i);
			j = k / fact;
			res += s[j];
			s.erase(s.begin() + j);
			k = k%fact;

		}
		return res;

	}
};
int main()
{
	Solution sol;
	vector<int> nums = { -2};
	nums = { 3, 2, -2, 4 };
	//nums = { -4, -3 };
	nums = {1,2,3};
	cout<<sol.getPermutation(3,2);
	
	cout << endl;
	//for (auto k :nums )cout << k << " ";
	system("pause");
	return 0;
}
