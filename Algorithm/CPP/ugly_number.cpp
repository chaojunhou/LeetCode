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

	bool isUgly(int num) {
		vector<int> primes = { 2, 3, 5 };
		if (num == 1) return true;

		while (num>1)
		{
			int tmp = num;
			for (auto prime : primes)
			{
				if (num%prime == 0)
				{
					num = num / prime;
				}
			} 
			if (tmp == num) return false;
			
		}
		if (num == 1 ) return true;
		return false;
	}

};


int main()
{
	Solution sol;
	vector<int> triangle = { 1,2,1,3,2,5};
	triangle = { 2, 1, 2, 3, 4, 1 };
	triangle = { 1, 2, 2 };
	int num = 14;
	cout<<sol.isUgly(num)<<endl;
	system("pause");
	return 0;
}

