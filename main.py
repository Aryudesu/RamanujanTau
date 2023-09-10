def calc_pascal_triangle(num):
    dp = [1]
    for i in range(num):
        new_dp = []
        s = 0
        bs = 0
        for j in dp:
            s = bs + j
            bs = j
            new_dp.append(s)
        new_dp.append(1)
        dp = new_dp
    return dp


def calc(num):
    ta = calc_pascal_triangle(24)
    lta = len(ta)
    dp = {0: 1}
    n = 1
    for n in range(1, num + 1):
        new_dp = dict()
        for d in dp:
            sgn = 1
            for idx in range(lta):
                key = d + n * idx
                if key > num:
                    break
                nndp = new_dp.get(key, 0)
                tmp = dp.get(d) * (sgn * ta[idx])
                new_dp[key] = nndp + tmp
                sgn = -sgn
        dp = new_dp
    result = [0]
    for i in range(num):
        result.append(dp[i])
    return result


def inputNum():
    print("InputNum > ", end="")
    return int(input())


result = calc(inputNum())
with open("Result.txt", mode="w") as f:
    for r in result:
        f.write(str(r) + "\n")
