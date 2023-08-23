class Solve:

    def __init__(self) -> None:
        self.n = 0;

    def vao(self) -> None:
        self.n = int(input());

    def value(self, x, y) -> int:
        value = 0;
        if(x % 2 == 0 and y % 2 == 0):
            if(x == y or x - y == 2):
                value = x + y;
            else:
                value = -1;
        elif(x % 2 != 0 and y % 2 != 0):
            if(x == y or x - y == 2):
                value = x + y - 1;
            else:
                value = -1;
        else:
            value = -1;
        return value;

    def lam(self) -> None:
        for _ in range(self.n):
            x, y = map(int, input().split(" "));
            ketQua = self.value(x, y);
            if(ketQua != -1):
                print(ketQua);
            else:
                print("No Number");

def main():
    p = Solve();
    p.vao();
    p.lam();

main();
