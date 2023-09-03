class Solve:

    def __init__(self, n:int) -> None:
        self.col = n;
        self.mess = "";
        self.encryted = [];

    def vao(self) -> None:
        self.mess = input();

    def giaiMa(self, size:int) -> None:
        flag = 0;
        for i in range(size):
            s = self.mess[flag:flag + self.col];
            if(i % 2 == 0):
                self.encryted.append(s);
            else:
                s = s[::-1];
                self.encryted.append(s);
            flag += self.col;

    def lam(self) -> None:
        size = len(self.mess) // self.col;
        self.giaiMa(size);
        for i in range(self.col):
            for j in range(size):
                print(self.encryted[j][i], end= "");
        print("");


def main():
    while(True):
        x = int(input());
        if(x == 0): break;
        p = Solve(x);
        p.vao();
        p.lam();

main();
