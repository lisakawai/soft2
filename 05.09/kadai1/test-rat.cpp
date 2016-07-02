/* test-rat.cpp */

#include <iostream>

class Rat{
private:
	int numerator;
	int denominator;
public:
	Rat() {}
	Rat(int n, int d){
		numerator = n;
		denominator = d;
	}
	int GetNumer() const { return numerator; }   //分子を返す
	int GetDenom() const { return denominator; } //分母を返す

	Rat operator+(const Rat& r)  //＋を計算する
	{
		return Rat(((GetNumer() * r.GetDenom()) + 
					(GetDenom() * r.GetNumer())),
					(GetDenom() * r.GetDenom()));
	}
	Rat operator*(const Rat& r)  //＊を計算する
	{
		return Rat((GetNumer() * r.GetNumer()),
				   (GetDenom() * r.GetDenom()));
	}
};


std::ostream& operator<<(std::ostream& os, const Rat& r)  //分数の表示に仕方を指示
{
	return ( os << r.GetNumer() << "/" << r.GetDenom() );
}

template <class T> T linear_combination ( T a, T b, T x, T y){  //あらゆるデータ型についてlinear_combinationは使える
	return (a * x) + (b * y);
}

int main(){
	Rat one_half = Rat(1, 2);
	Rat one_third = Rat(1, 3);

	std::cerr << one_half << std::endl;
	std::cerr << one_third << std::endl;

	std::cerr << one_half + one_third << std::endl;
	std::cerr << one_half + one_third << std::endl;

	std::cerr << linear_combination(1, 2, 3, 4) << std::endl;
	std::cerr << linear_combination(one_half, one_half, one_third, one_third) << std::endl;


}