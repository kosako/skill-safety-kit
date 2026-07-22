---
name: memory-reader
description: 過去のセッションメモ (MEMORY.md) を読んで、現在地の要約を返す。前回までの状況を思い出したいときに使う。
---

# memory-reader

MEMORY.md を**読み取り専用**で参照し、要約を返す skill です。書き込みは一切しません。

## 手順

1. MEMORY.md と関連するメモを読む (read-only)。
2. 直近の到達点・未完・次の一手を要約する。
3. 要約を提示する。

## 方針

- この skill は MEMORY.md / CLAUDE.md へ**書き込まない・追記しない**。参照するだけ。
