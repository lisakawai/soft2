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

        Rat operator-(const Rat& r)  //ーを計算する
	{
	  return Rat(((GetNumer() * r.GetDenom())-
		      (GetDenom() * r.GetNumer())),
		     (GetDenom() * r.GetDenom()));
	}

        Rat operator/(const Rat& r)  //÷を計算する
	{
	  return Rat((GetNumer() * r.GetDenom()),
		     (GetDenom() * r.GetNumer()));
	}
};


std::ostream& operator<<(std::ostream& os, const Rat& r)  //分数の表示に仕方を指示
{
	return ( os << r.GetNumer() << "/" << r.GetDenom() );
}

template <class T> T linear_combination ( T a, T b, T x, T y){  //あらゆるデータ型についてlinear_combinationは使える
	return (a * x) + (b * y);
}

template <class T> T linear_combination2 ( T a, T b, T x, T y){  //あらゆるデータ型についてlinear_combinationは使える
	return (a / x) - (b / y);
}

int main(){
	Rat one_half = Rat(1, 2);
	Rat one_third = Rat(1, 3);
	
	float a1 = 1.5;
	float a2 = 2.3;
	float a3 = 4.1;	
	float a4 = 6.7;

	double b1 = 1.5;	
	double b2 = 2.3;	
	double b3 = 4.1;	
	double b4 = 6.7;
	
	std::cerr << one_half << std::endl;
	std::cerr << one_third << std::endl;

	std::cerr << one_half + one_third << std::endl;
	std::cerr << one_half + one_third << std::endl;

	std::cerr << linear_combination2(1, 2, 3, 4) << std::endl;
	std::cerr << linear_combination2(one_half, one_half, one_third, one_third) << std::endl;

	std::cerr << linear_combination2(1.5, 2.6, 3.1, 4.5) << std::endl;
	std::cerr << linear_combination2(a1, a2, a3, a4) << std::endl;
	std::cerr << linear_combination2(b1, b2, b3, b4) << std::endl;

}
