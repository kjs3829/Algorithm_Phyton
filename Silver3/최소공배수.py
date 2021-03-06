# BOJ 13241 최소공배수
# 유클리드 호제법
import sys
input = sys.stdin.readline


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def lcm(a, b):
    return a*b//gcd(a, b)


a, b = map(int, input().split())
print(lcm(a, b))
