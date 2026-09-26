[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# OnlyIdeas-papers

*깊이 읽고, 함께 생각하세요.*

[OnlyIdeas](https://agent.onlyideas.art) · [GitHub Sponsors](https://github.com/sponsors/lachlanchen) · [OnlyIdeas-papers](https://github.com/lachlanchen/OnlyIdeas-papers)

## 개요

이 저장소는 OnlyIdeas의 간결한 공개 논문 묶음을 보관합니다. 기준 Mathpix Markdown, 작은 메타데이터 파일, 영구 보관하는 그림으로 구성됩니다. 업로드된 원본 PDF, 개인 메모, 계정 데이터는 포함하지 않습니다.

각 논문의 라이선스와 출처 표기를 유지합니다. 공개하려면 본문과 그림 모두에 대한 허가가 필요합니다. 초기 CC0 샘플은 직접 만든 시연 자료이며 발표된 연구 논문이 아닙니다.

## 시작하기

묶음을 추가하기 전에 본문 해시, 메타데이터, 라이선스, 모든 그림 경로를 검증하세요.

```bash
python3 tools/validate.py
```

[FORMAT.md](../FORMAT.md) · [papers/](../papers/) · [OnlyIdeasApp](https://github.com/lachlanchen/OnlyIdeasApp)

## 설계

기준 텍스트와 그림을 한 벌만 보관합니다. 파생 JSON과 전체 TeX 내보내기는 필요할 때 만들 수 있습니다. 큰 PDF 자료는 일반 Git 기록에 넣지 않습니다.

## 상태

라이브러리는 직접 만든 읽기 샘플 하나로 시작합니다. 새 논문에는 명확한 권리 검토가 필요합니다. 형식 문서를 읽고 OnlyIdeasApp으로 가져오거나 읽으세요.

## 후원

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## 인용

연구에 이 저장소를 활용하면 인용해 주세요. GitHub는 CITATION.cff를 읽어 인용 정보를 제공합니다. [CITATION.cff](../CITATION.cff)

```bibtex
@software{chen_onlyideas_papers_2026,
  author = {Chen, Lachlan},
  title = {OnlyIdeas-papers: Read deeply, think together},
  year = {2026},
  url = {https://github.com/lachlanchen/OnlyIdeas-papers}
}
```
