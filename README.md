[English](README.md) · [العربية](i18n/README.ar.md) · [Español](i18n/README.es.md) · [Français](i18n/README.fr.md) · [日本語](i18n/README.ja.md) · [한국어](i18n/README.ko.md) · [Tiếng Việt](i18n/README.vi.md) · [中文 (简体)](i18n/README.zh-Hans.md) · [中文（繁體）](i18n/README.zh-Hant.md) · [Deutsch](i18n/README.de.md) · [Русский](i18n/README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://lazying.art)

# OnlyIdeas-papers

*Read deeply. Think together.*

[OnlyIdeas](https://agent.onlyideas.art) · [GitHub Sponsors](https://github.com/sponsors/lachlanchen) · [OnlyIdeas-papers](https://github.com/lachlanchen/OnlyIdeas-papers)

## Overview

This repository holds compact, public paper bundles for OnlyIdeas: canonical Mathpix Markdown, a small metadata manifest, and durable figures. It contains no original PDF uploads, private notes or account data.

Each paper retains its own license and source attribution. Publication requires permission for both text and figures. The initial CC0 sample is original demonstration material, not a published research paper.

## Quick start

Validate the text hash, metadata, license and all figure paths before adding a bundle.

```bash
python3 tools/validate.py
```

[FORMAT.md](FORMAT.md) · [papers/](papers/) · [OnlyIdeasApp](https://github.com/lachlanchen/OnlyIdeasApp)

## Design

Keep one canonical text plus its figures. Derived JSON and full TeX exports can be created on demand. Large PDF archives do not belong in ordinary Git history.

## Status

The public reading room now includes two real papers: OpenAlex (CC0-1.0) and Measuring holographic entanglement entropy on a quantum simulator (CC-BY-4.0), alongside the clearly labeled original sample. Four original figures are retained. Both papers were imported through the real conversion workflow and checked in a phone-width reader without signing in.

[OpenAlex](https://arxiv.org/abs/2205.01833v2) · [Quantum simulator](https://www.nature.com/articles/s41534-019-0145-z) · [OnlyIdeas](https://agent.onlyideas.art)

## Support

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Citation

Cite this repository when using it in research. GitHub reads CITATION.cff to offer a citation. [CITATION.cff](CITATION.cff)

```bibtex
@software{chen_onlyideas_papers_2026,
  author = {Chen, Lachlan},
  title = {OnlyIdeas-papers: Read deeply, think together},
  year = {2026},
  url = {https://github.com/lachlanchen/OnlyIdeas-papers}
}
```
