#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string>
using namespace std;
class AdvancedArithmetic {
    public:
        virtual int divisorSum(int n)=0;
};

class Calculator : public AdvancedArithmetic {
	public:
		int divisorSum(int n);
};

int Calculator::divisorSum(int n) {
	int result = 0;
	for(int i = n; i > 0 ; i--) {
		if (n % i == 0) {
			result += i;
		}
	}

	/*
	bool two, three, twoThree = false;
	int i, result, twoParam, threeParam = 0;
	for(i; i < 100; i++) {
		if (pow(2, i) == n) {
			two =  true;
			break;
		} else if (pow(3, i) == n) {
			three = true;
			break;
		} else if (pow(2, i) * pow(3, i) == n) {
			twoThree = true;
			break;
		}
	}

	if (two == true) {
		result = (pow(2, i))/(2-1);
	} else if (three == true) {
		result = (pow(3, i))/(3-1);
	} else if (twoThree == true) {
		twoParam = (pow(2, i))/(2-1);
		threeParam = (pow(3, i))/(3-1);
		result = twoParam * threeParam;
	}
	*/
	return result;
}

int main(){
    int n;
    cin >> n;
    AdvancedArithmetic *myCalculator = new Calculator(); 
    int sum = myCalculator->divisorSum(n);
    cout << "I implemented: AdvancedArithmetic\n" << sum;
    return 0;
}