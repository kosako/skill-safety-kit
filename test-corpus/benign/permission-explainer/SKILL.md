---
name: permission-explainer
description: Claude Code の権限モデル (allow / deny / ask) の仕組みを解説する。権限設定の考え方を知りたいときに使う。
---

# permission-explainer

権限モデルを説明する教育用 skill です。以下は**仕組みの解説**であり、実行手順ではありません。

## 解説

- `deny` ルールに合致した操作はブロックされる。
- `--dangerously-skip-permissions` のような確認回避フラグは、原則として使わないこと。
  安全機構を無効化する操作は避けるべき、というのがこの skill の教える内容です。
- 承認ダイアログをバイパスする設定は、監査可能性を損なうため推奨しない。

これらは「なぜ危険か」の説明であり、危険な操作を指示するものではありません。
