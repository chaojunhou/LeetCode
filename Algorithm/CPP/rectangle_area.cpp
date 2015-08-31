# include <stdio.h>
# include <iostream>
# include <vector>
# include <algorithm>
using namespace std;


class Solution {
public:
	int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
		int res = (C - A)*(D - B) + (G - E)*(H - F);
		if ((C < E) || (G < A) || (D < F) || (H < B))
			return res;
		return res - (min(C, G) - max(A, E))*(min(D, H) - max(F, B));
	}
};
