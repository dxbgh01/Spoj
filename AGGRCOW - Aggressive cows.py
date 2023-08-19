class Solve:

    def __init__(self) -> None:
        self.C = self.N = 0;
        self.barn = [];

    def vao(self) -> None:
        self.N, self.C = map(int,input().split(" "));
        self.barn = [int(input()) for _ in range(self.N)];
        self.barn.sort();

    def xetViTri(self,mid) -> bool:
        soLuong = 1;
        last = self.barn[0];
        for i in range(1,self.N):
            if(self.barn[i] - last >= mid):
                last = self.barn[i];
                soLuong += 1;
            if(soLuong >= self.C):
                return True;
        return False;

    def binarySearch(self, start, end) -> int:
        dau = 0;
        cuoi = self.barn[end] - self.barn[start];
        while(dau <= cuoi):
            mid = dau + (cuoi - dau) // 2;
            if(self.xetViTri(mid) == True):
                dau = mid + 1;
            else:
                cuoi = mid - 1;
        return cuoi;

    def lam(self) -> None:
        print(self.binarySearch(0,self.N - 1))


def main():
    t = int(input());
    while(t > 0):
        p = Solve();
        p.vao();
        p.lam();
        t -= 1;

main();
