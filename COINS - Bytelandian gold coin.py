class Solve:

    def __init__(self, n) -> None:
        self.n = n;
        self.coin = dict();

    def vao(self) -> None:
        pass;

    def checkCoin(self, coin:int) -> int:
        try:
            x = self.coin[coin];
        except KeyError:
            return self.splitCoin(coin);
        else:
            return x;

    def splitCoin(self, coin:int) -> int:
        if(coin == 0): return 0;
        x1 = self.checkCoin(coin // 4);
        x2 = self.checkCoin(coin // 3);
        x3 = self.checkCoin(coin // 2);
        tmp = x1 + x2 + x3;
        if(tmp > coin):
            self.coin[coin] = tmp;
        else:
            self.coin[coin] = coin;
        ketQua = self.coin[coin];
        return ketQua;


    def lam(self) -> None:
        ketQua = self.splitCoin(self.n);
        print(ketQua);


def main():
    while(True):
        try:
            s = input();
        except EOFError: break;
        else:
            p = Solve(int(s));
            p.vao();
            p.lam();


main();
