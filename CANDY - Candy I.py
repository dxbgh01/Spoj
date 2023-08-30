class Solve:

    def __init__(self, n:int) -> None:
        self.n = n;
        self.dauVao = [];

    def vao(self) -> None:
        self.dauVao = [int(input()) for _ in range(self.n)];

    def tinhTong(self) -> int:
        ketQua = 0;
        for i in self.dauVao:
            ketQua += i;
        return ketQua;

    def lam(self) -> None:
        tong = self.tinhTong();
        if(tong % self.n == 0):
            average = tong // self.n;
            ketQua = 0;
            for i in self.dauVao:
                if(i < average): ketQua += average - i;
            print(ketQua);
        else: print("-1");


def main():
    while(True):
        n = int(input());
        if(n == -1): break;
        p = Solve(n);
        p.vao();
        p.lam();


main();
