t = int(input());
while(t > 0):
    a, b = map(int, input().split(" "));
    if(b == 0): print(1);
    else:
        mod = [];
        x = a % 10;
        while(True):
            mod.append(x);
            x = (x * a) % 10;
            if(x == a % 10): break;
        size = len(mod);
        mod = mod[size - 1:] + mod[:size - 1];
        m = b % size;
        ketQua = mod[m];
        print(ketQua);
    t -= 1;
