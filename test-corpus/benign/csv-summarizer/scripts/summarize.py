#!/usr/bin/env python3
"""ローカル CSV の各列の件数・欠損・最小/最大を表示する (外部送信・書き込みなし)。"""
import csv
import sys


def main(path):
    with open(path, newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return
    header, data = rows[0], rows[1:]
    for i, name in enumerate(header):
        vals = [r[i] for r in data if i < len(r) and r[i] != ""]
        nums = []
        for v in vals:
            try:
                nums.append(float(v))
            except ValueError:
                pass
        line = f"{name}: count={len(vals)} missing={len(data) - len(vals)}"
        if nums:
            line += f" min={min(nums)} max={max(nums)}"
        print(line)


if __name__ == "__main__":
    main(sys.argv[1])
