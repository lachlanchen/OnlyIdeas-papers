[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# OnlyIdeas-papers

*深く読み、ともに考える。*

[OnlyIdeas](https://agent.onlyideas.art) · [GitHub Sponsors](https://github.com/sponsors/lachlanchen) · [OnlyIdeas-papers](https://github.com/lachlanchen/OnlyIdeas-papers)

## 概要

このリポジトリは OnlyIdeas の小さな公開論文パッケージを保存します。正本となる Mathpix Markdown、最小限のメタデータ、保存済みの図で構成されます。アップロードした元の PDF、私的なノート、アカウント情報は含みません。

各論文のライセンスと出典表記を維持します。公開には本文と図の両方について許可が必要です。最初の CC0 サンプルは独自のデモ資料で、発表済みの研究論文ではありません。

## 使い始める

追加前に本文のハッシュ、メタデータ、ライセンス、すべての図のパスを検証してください。

```bash
python3 tools/validate.py
```

[FORMAT.md](../FORMAT.md) · [papers/](../papers/) · [OnlyIdeasApp](https://github.com/lachlanchen/OnlyIdeasApp)

## 設計

正本のテキストと図を一組だけ保持します。派生 JSON や完全な TeX は必要に応じて出力できます。大きな PDF アーカイブは通常の Git 履歴に置きません。

## 状況

公開読書室には、明示されたオリジナルサンプルに加え、実際の論文 OpenAlex（CC0-1.0）と Measuring holographic entanglement entropy on a quantum simulator（CC-BY-4.0）を収録しました。元の図を計4点保持しています。どちらも実際の変換処理で取り込み、ログインせずにスマートフォン幅のリーダーで確認しました。

[OpenAlex](https://arxiv.org/abs/2205.01833v2) · [Quantum simulator](https://www.nature.com/articles/s41534-019-0145-z) · [OnlyIdeas](https://agent.onlyideas.art)

## 支援

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 引用

研究でこのリポジトリを利用する場合は引用してください。GitHub は CITATION.cff から引用情報を提供します。 [CITATION.cff](../CITATION.cff)

```bibtex
@software{chen_onlyideas_papers_2026,
  author = {Chen, Lachlan},
  title = {OnlyIdeas-papers: Read deeply, think together},
  year = {2026},
  url = {https://github.com/lachlanchen/OnlyIdeas-papers}
}
```
