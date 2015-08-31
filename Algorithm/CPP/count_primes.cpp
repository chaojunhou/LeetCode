# include <stdio.h>
# include <iostream>
# include <vector>
# include <string>
# include <cctype>
# include <algorithm>
# include<time.h>
using namespace std;




class Solution {
public:
	int countPrimes(int n) {
		if (2 >= n) return 0;
		bool* a = new bool[n];
		for (int i = 0; i < n; i++)
		{
			if (i & 1)
			{
				a[i] = true;
			}
			else
			{
				a[i] = false;
			}
		}
		a[1] = false;
		a[2] = true;
		for (int i = 3; i*i < n; i += 2)
		{
			if (a[i])
			{
				for (int j = i*i; j < n; j += i << 1)
				{
					a[j] = false;
				}

			}

		}
		int sum = 0;
		for (int i = 0; i < n; i++)
		{
			if (a[i])
			{
				sum += 1;
			}
		}

		return sum;

	}
};

int main()
{
	Solution sol;
	vector<int> nums = { 1,1,1,1,2,3 };
	int k = 8;
	//nums = { 3, 2, 1, 5, 6, 4 };
	cout << sol.countPrimes(10) << endl;
	//for (auto k :nums )cout << k << " ";
	cout << endl;
	system("pause");
	return 0;
}
