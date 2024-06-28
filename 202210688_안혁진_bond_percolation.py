# -*- coding: utf-8 -*-
"""202210688_안혁진_bond_percolation.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1KVcORxKlFb-670I1kXmbDh8ZWH41PFH8

bond 개수 : 4n / 2 = 2n
"""



import numpy as np
import matplotlib.pyplot as plt

L = 36
N = L**2

ptr = np.empty(N, int)  # 각 스핀의 부모 포인터 배열

big_list = []  # 각 반복마다의 가장 큰 클러스터 크기를 저장할 리스트

# Union-Find 알고리즘의 find 함수 정의
def find(i):
    if ptr[i] < 0:
        return i  # 자기 자신이 root인 경우
    else:
        ptr[i] = find(ptr[i])  # 경로 압축
        return ptr[i]

# Union-Find 알고리즘의 union 함수 정의
def union(r1, r2, big):
    if r2 != r1:
        if ptr[r1] > ptr[r2]:  # 두 번째 트리가 더 큰 경우
            ptr[r2] += ptr[r1]  # 첫 번째 트리를 병합
            ptr[r1] = r2
            r1 = r2
        else:
            ptr[r1] += ptr[r2]
            ptr[r2] = r1
        if -ptr[r1] > big:  # 기존의 big보다 큰 경우 갱신
            big = -ptr[r1]
    big_list.append(big / N)  # 현재의 가장 큰 클러스터 크기를 N으로 나눈 값을 리스트에 추가
    return r1, r2, big

big = 0
bonds = []

# 가장 가까운 이웃들 간의 본드 초기화
for i in range(L):
    for j in range(L):
        current = i * L + j
        right = i * L + (j + 1) % L
        down = ((i + 1) % L) * L + j
        bonds.append((current, right))
        bonds.append((current, down))

np.random.shuffle(bonds)  # 본드를 무작위로 섞음

print(bonds)  # 섞인 본드 출력 (디버깅용)

for i in range(L**2):
    ptr[i] = -1  # 각 스핀의 초기 부모 포인터 설정

print(np.shape(bonds))  # 본드의 모양 출력 (디버깅용)

# Union-Find 알고리즘을 이용하여 클러스터 크기 계산
for bond in bonds:
    s1, s2 = bond
    r1, r2 = find(s1), find(s2)
    r1, r2, big = union(r1, r2, big)

print(np.shape(big_list))  # 각 반복마다의 가장 큰 클러스터 크기를 저장한 리스트의 모양 출력 (디버깅용)

xlist = [(i+1)/(2*N) for i in range(2*N)]

plt.plot(xlist,big_list)
plt.show()