#include <iostream>

class Solve{
  
  public:
    int square(int n){
      int ketQua = 0;
      for (int i = 1; i <= n; i ++){
        ketQua += i * i;
      }
      return ketQua;
    }
    
    void lam(){
      while(true){
        int n = 0;
        std::cin >> n;
        if(n == 0) break;
        int ketQua = square(n);
        std::cout << ketQua << std::endl;
      }
    }

};


int main(){
  Solve *p = new Solve();
  p -> lam();
  delete p;
  p = NULL;
}
