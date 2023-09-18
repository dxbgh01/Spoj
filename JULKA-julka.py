class Solve:
    
    def __init__(self) -> None:
        self.apples = [];
        self.more = [];

    def vao(self) -> None:
        self.apples = [int(item) for item in input()];
        self.more = [int(item) for item in input()];

    def chuanHoa(self, dauVao:list) -> list:
        ketQua = [];
        for i in range(len(dauVao)):
            if(dauVao[i] != 0):
                ketQua = dauVao[i:];
                break;
        return ketQua;

    def SUB(self, dauVao:list):
        size1 = len(self.apples);
        size2 = len(dauVao);
        khoangCach = size1 - size2;
        ketQua = [0 for _ in range(size1)];
        du = 0;
        for i in range(size1 - 1, -1, -1):
            m = i - khoangCach;
            if(m < 0): 
                if(self.apples[i] >= du):
                    ketQua[i] = self.apples[i] - du;
                    du = 0;
                else:
                    ketQua[i] = 10 + self.apples[i] - du;
                    du = 1;
            else:
                if(self.apples[i] >= dauVao[m] + du):
                    ketQua[i] = self.apples[i] - dauVao[m] - du;
                    du = 0;
                else:
                    soTru = 10 + self.apples[i];
                    soBiTru = dauVao[m] + du;
                    ketQua[i] = soTru - soBiTru;
                    du = 1;
        ketQua = self.chuanHoa(ketQua);
        return ketQua;
    
    def DIV(self, dauVao: list) -> list:
        ketQua = [];
        du = 0;
        for i in range(len(dauVao)):
            du = du * 10 + dauVao[i];
            if(len(ketQua) == 0 and du // 2 == 0): continue;
            else:
                tmp = du // 2;
                ketQua.append(tmp);
                du = du - tmp * 2;
        return ketQua;
    
    def Print(self, dauVao:list) -> None:
        if(len(dauVao) == 0): 
            print("0");
            return;
        for item in dauVao:
            print(item, end = "");
        print("");

    def lam(self) -> None:
        tmp = self.SUB(self.more);
        Natalia = self.DIV(tmp);
        Klaudia = self.SUB(Natalia);
        self.Print(Klaudia);
        self.Print(Natalia);


def main():
    for _ in range(10):
        p = Solve();
        p.vao();
        p.lam();

main();
