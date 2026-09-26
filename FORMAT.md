# OnlyIdeas paper bundles · version 1

Each `papers/<id>/` directory contains `paper.mmd`, `metadata.json` and its referenced
`figures/`. MMD preserves TeX math and scientific structures. Metadata records title,
authors, source URL, license/permission, original language, category, SHA-256 text
revision and asset paths. Figure names use a content hash. Derived section JSON is
recomputed by the app. No full duplicate JSON or TeX edition is required.

No original PDFs, credentials, private notes or private discussion records belong
here. Every publication requires explicit permission covering figures as well as
text. Open-access availability alone is insufficient. Papers retain their own
licenses; this repository has no blanket license for third-party papers.

The initial original OnlyIdeas sample is CC0 and is explicitly a reading demo, not
a published scientific paper. The app lives in the separate OnlyIdeasApp repository.

Run `python3 tools/validate.py` before publication. Keep ordinary Git bundles small;
move large archives to a dedicated asset store or release downloads as the library
grows. Do not use Git history as a high-volume binary document database.
