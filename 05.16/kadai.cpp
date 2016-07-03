#include <iostream>
#include <vector>
#include <algorithm>


int main(){
  std::vector<int> c{7, 1, 3, 4, 5, 1, 3, 4};
  std::sort(c.begin(), c.end());
  std::for_each(c.begin(), c.end(), [](int &n){ std::cerr << n <<" "; });
  std::cerr << std::endl;
}
