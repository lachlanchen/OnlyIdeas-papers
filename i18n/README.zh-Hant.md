[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# OnlyIdeas-papers

*認真閱讀，一起思考。*

[OnlyIdeas](https://agent.onlyideas.art) · [GitHub Sponsors](https://github.com/sponsors/lachlanchen) · [OnlyIdeas-papers](https://github.com/lachlanchen/OnlyIdeas-papers)

## 概覽

本儲存庫保存 OnlyIdeas 的精簡公開論文套件：作為權威文本的 Mathpix Markdown、少量中繼資料，以及持久保存的插圖。不包含上傳的原始 PDF、私人筆記或帳戶資料。

每篇論文保留自己的授權條款和來源署名。發布須取得正文和插圖的使用授權。初始 CC0 範例是原創展示材料，並非已發表的研究論文。

## 快速開始

新增論文套件前，請驗證文本雜湊、中繼資料、授權條款及所有插圖路徑。

```bash
python3 tools/validate.py
```

[FORMAT.md](../FORMAT.md) · [papers/](../papers/) · [OnlyIdeasApp](https://github.com/lachlanchen/OnlyIdeasApp)

## 設計

每篇論文只保留一份權威文本及插圖。衍生 JSON 和完整 TeX 匯出可按需產生。大型 PDF 檔案不應放入一般 Git 歷史。

## 狀態

公共閱讀室現有兩篇真實論文：OpenAlex（CC0-1.0）和 Measuring holographic entanglement entropy on a quantum simulator（CC-BY-4.0），另保留明確標示的原創範例。四幅原始插圖完整保留。兩篇均透過真實轉換流程匯入，並在未登入的手機寬度閱讀器中驗證。

[OpenAlex](https://arxiv.org/abs/2205.01833v2) · [Quantum simulator](https://www.nature.com/articles/s41534-019-0145-z) · [OnlyIdeas](https://agent.onlyideas.art)

## 支持

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 引用

在研究中使用本儲存庫時請引用。GitHub 透過 CITATION.cff 提供引用資訊。 [CITATION.cff](../CITATION.cff)

```bibtex
@software{chen_onlyideas_papers_2026,
  author = {Chen, Lachlan},
  title = {OnlyIdeas-papers: Read deeply, think together},
  year = {2026},
  url = {https://github.com/lachlanchen/OnlyIdeas-papers}
}
```
