import math;

class Solve:

    def __init__(self) -> None:
        self.n = 0;

    def vao(self) -> None:
        self.n = int(input());

    def lam(self) -> None:
        ketQua = 0;
        chieuRong = int(math.sqrt(self.n));
        for i in range(1, chieuRong + 1):
            ketQua += self.n // i - i + 1;
        print(ketQua);


def main():
    p = Solve();
    p.vao();
    p.lam();


main();
