# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
	vector<int> diffWaysToCompute(string input) {
		vector<int> vec;
		for (auto i = 0; i < input.size(); ++i)
		{
			if (ispunct(input[i]))
			{
				for (auto a : diffWaysToCompute(input.substr(0, i)))
				{
					for (auto b : diffWaysToCompute(input.substr(i + 1)))
					{
						if (input[i] == '+')
						{
							vec.push_back(a + b);
						}
						else if (input[i] == '-')
						{
							vec.push_back(a - b);
						}
						else
						{
							vec.push_back(a*b);
						}

					}

				}

			}
		}

		if (vec.size() == 0) vec.push_back(atoi(input.c_str()));
		return vec;

	}
};
int  main()
{
	Solution sol;
	string  input = "2*3-4*5";
	cout << input.c_str() << endl;
	auto vec= sol.diffWaysToCompute(input);
	for (auto k : vec)
		cout << k << endl;

	cin.get();
	return 0;
}
