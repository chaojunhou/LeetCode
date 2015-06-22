# include <vector>
# include <iostream>
using namespace std;
class Solution{
public:
	vector<int> plusOne(vector<int>& digits){
		int n = digits.size();


		for (int i=n-1;i > -1;--i)
 		 {
 		 	if (digits[i] < 9)
			{
				digits[i] += 1;
				return digits;
			}

			else
				digits[i] = 0;
		}
		digits.insert(digits.begin(),1);
		return digits;
	}
};

int main()
{
	Solution sol;
	vector<int> digits = {9,9,9,9};
	for (auto m:sol.plusOne(digits))
	{
		cout<< m;
	}

	
	return 0;
}
