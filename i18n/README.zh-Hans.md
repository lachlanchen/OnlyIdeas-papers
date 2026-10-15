[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner — apps and four buddies](https://lazying.art/media/brand/lazyingart-intro.gif)](https://lazying.art)

# OnlyIdeas-papers

*认真阅读，一起思考。*

[OnlyIdeas](https://agent.onlyideas.art) · [GitHub Sponsors](https://github.com/sponsors/lachlanchen) · [OnlyIdeas-papers](https://github.com/lachlanchen/OnlyIdeas-papers)

## 概览

本仓库存储 OnlyIdeas 的精简公开论文包：作为权威文本的 Mathpix Markdown、少量元数据以及持久保存的插图。不包含上传的原始 PDF、私人笔记或账户数据。

每篇论文保留自己的许可证和来源署名。发布须获得正文和插图的使用授权。初始 CC0 示例是原创演示材料，并非已发表的研究论文。

## 快速开始

添加论文包前，请校验文本哈希、元数据、许可证及全部插图路径。

```bash
python3 tools/validate.py
```

[FORMAT.md](../FORMAT.md) · [papers/](../papers/) · [OnlyIdeasApp](https://github.com/lachlanchen/OnlyIdeasApp)

## 设计

每篇论文只保留一份权威文本及插图。派生 JSON 和完整 TeX 导出可按需生成。大型 PDF 档案不应放入普通 Git 历史。

## 状态

公共阅读室现有两篇真实论文：OpenAlex（CC0-1.0）和 Measuring holographic entanglement entropy on a quantum simulator（CC-BY-4.0），另保留明确标注的原创示例。四幅原始插图完整保留。两篇均通过真实转换流程导入，并在未登录的手机宽度阅读器中验证。

[OpenAlex](https://arxiv.org/abs/2205.01833v2) · [Quantum simulator](https://www.nature.com/articles/s41534-019-0145-z) · [OnlyIdeas](https://agent.onlyideas.art)

## 支持

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 引用

在研究中使用本仓库时请引用。GitHub 通过 CITATION.cff 提供引用信息。 [CITATION.cff](../CITATION.cff)

```bibtex
@software{chen_onlyideas_papers_2026,
  author = {Chen, Lachlan},
  title = {OnlyIdeas-papers: Read deeply, think together},
  year = {2026},
  url = {https://github.com/lachlanchen/OnlyIdeas-papers}
}
```
