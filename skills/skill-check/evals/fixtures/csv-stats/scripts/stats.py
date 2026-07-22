#!/usr/bin/env python3
"""ローカル CSV の数値列の合計と平均を表示する (外部送信・書き込みなし)。"""
import csv
import sys


def main(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return
    header, data = rows[0], rows[1:]
    for i, name in enumerate(header):
        nums = []
        for r in data:
            try:
                nums.append(float(r[i]))
            except (ValueError, IndexError):
                pass
        if nums:
            print(f"{name}: sum={sum(nums)} avg={sum(nums) / len(nums):.2f}")


if __name__ == "__main__":
    main(sys.argv[1])
