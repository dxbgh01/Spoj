class Solve:

    def __init__(self) -> None:
        pass;

    def progression(self, sequence) -> list:
        ketQua = [];
        a, b, c = sequence;
        if(b * 2 == a + c):
            ketQua.append("AP");
            ketQua.append(c + (b - a));
        else:
            ketQua.append("GP");
            ketQua.append(c * (b // a));
        return ketQua;

    def lam(self) -> None:
        while(True):
            sequence = [int(item) for item in input().split(" ")];
            if(sequence[0] == 0 and sequence[1] == 0 and sequence[2] == 0): break;
            ketQua = self.progression(sequence);
            for i in ketQua:
                print(i, end= " ");
            print("");


def main():
    p = Solve();
    p.lam();

main();
