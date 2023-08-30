class Solve:

    def __init__(self) -> None:
        self.pair = 0;
        self.men = [];
        self.women = [];

    def vao(self) -> None:
        self.pair = int(input());
        self.men = [int(item) for item in input().split(" ")];
        self.women = [int(item) for item in input().split(" ")];

    def lam(self) -> None:
        ketQua = 0;
        men = sorted(self.men);
        women = sorted(self.women);
        for i in range(self.pair):
            ketQua += men[i] * women[i];
        print(ketQua);


def main():
    t = int(input());
    while(t > 0):
        p = Solve();
        p.vao();
        p.lam();
        t -= 1;


main();
