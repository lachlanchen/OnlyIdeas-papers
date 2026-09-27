[English](../README.md) · [العربية](README.ar.md) · [Español](README.es.md) · [Français](README.fr.md) · [日本語](README.ja.md) · [한국어](README.ko.md) · [Tiếng Việt](README.vi.md) · [中文 (简体)](README.zh-Hans.md) · [中文（繁體）](README.zh-Hant.md) · [Deutsch](README.de.md) · [Русский](README.ru.md)

[![LazyingArt banner](https://github.com/lachlanchen/lachlanchen/raw/main/figs/banner.png)](https://github.com/lachlanchen/lachlanchen/blob/main/figs/banner.png)

# OnlyIdeas-papers

*Читайте вдумчиво. Размышляйте вместе.*

[OnlyIdeas](https://agent.onlyideas.art) · [GitHub Sponsors](https://github.com/sponsors/lachlanchen) · [OnlyIdeas-papers](https://github.com/lachlanchen/OnlyIdeas-papers)

## Обзор

Репозиторий хранит компактные открытые пакеты статей OnlyIdeas: основной текст в Mathpix Markdown, небольшой файл метаданных и сохранённые рисунки. Здесь нет загруженных оригинальных PDF, личных заметок или данных учётных записей.

Каждая статья сохраняет свою лицензию и указание источника. Для публикации нужны права и на текст, и на рисунки. Первый пример CC0 создан для демонстрации и не является опубликованной научной статьёй.

## Быстрый старт

Перед добавлением пакета проверьте хеш текста, метаданные, лицензию и пути ко всем рисункам.

```bash
python3 tools/validate.py
```

[FORMAT.md](../FORMAT.md) · [papers/](../papers/) · [OnlyIdeasApp](https://github.com/lachlanchen/OnlyIdeasApp)

## Устройство

Хранится один основной текст и его рисунки. Производные JSON и полные экспорты TeX можно создавать по запросу. Большие PDF-архивы не следует помещать в обычную историю Git.

## Состояние

В общей библиотеке теперь две настоящие статьи: OpenAlex (CC0-1.0) и Measuring holographic entanglement entropy on a quantum simulator (CC-BY-4.0), а также явно обозначенный авторский пример. Сохранены четыре исходных рисунка. Обе статьи прошли реальную конвертацию и проверены без входа в аккаунт в читалке шириной с экран телефона.

[OpenAlex](https://arxiv.org/abs/2205.01833v2) · [Quantum simulator](https://www.nature.com/articles/s41534-019-0145-z) · [OnlyIdeas](https://agent.onlyideas.art)

## Поддержка

| Donate | PayPal | Stripe |
| --- | --- | --- |
| [![Donate](https://img.shields.io/badge/Donate-LazyingArt-0EA5E9?style=for-the-badge&logo=kofi&logoColor=white)](https://chat.lazying.art/donate) | [![PayPal](https://img.shields.io/badge/PayPal-RongzhouChen-00457C?style=for-the-badge&logo=paypal&logoColor=white)](https://paypal.me/RongzhouChen) | [![Stripe](https://img.shields.io/badge/Stripe-Donate-635BFF?style=for-the-badge&logo=stripe&logoColor=white)](https://buy.stripe.com/aFadR8gIaflgfQV6T4fw400) |

## Цитирование

При использовании в исследовании цитируйте этот репозиторий. GitHub использует CITATION.cff для оформления ссылки. [CITATION.cff](../CITATION.cff)

```bibtex
@software{chen_onlyideas_papers_2026,
  author = {Chen, Lachlan},
  title = {OnlyIdeas-papers: Read deeply, think together},
  year = {2026},
  url = {https://github.com/lachlanchen/OnlyIdeas-papers}
}
```
