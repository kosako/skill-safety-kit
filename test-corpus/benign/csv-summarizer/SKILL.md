---
name: csv-summarizer
description: ローカル CSV の各列の要約統計 (件数・欠損・最小最大) を表示する。CSV の概要を把握したいときに使う。
---

# csv-summarizer

CSV の要約統計を出す skill です。外部送信も書き込みもしません。

## 手順

1. 対象 CSV のパスを受け取る。
2. scripts/summarize.py で各列の件数・欠損数・最小/最大を計算する。
3. 結果を表で表示する。
