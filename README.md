<!--
https://readme42.com
-->



[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-tag-sync.svg?maxAge=3600)](https://pypi.org/project/mac-tag-sync/)
[![](https://img.shields.io/npm/v/mac-tag-sync.svg?maxAge=3600)](https://www.npmjs.com/package/mac-tag-sync)[![](https://img.shields.io/badge/License-Unlicense-blue.svg?longCache=True)](https://unlicense.org/)
[![](https://github.com/andrewp-as-is/mac-tag-sync/workflows/tests42/badge.svg)](https://github.com/andrewp-as-is/mac-tag-sync/actions)

### Installation
```bash
$ [sudo] pip install mac-tag-sync
```

```bash
$ [sudo] npm i -g mac-tag-sync
```

#### Requirements
```bash
$ brew install tag
```

#### Examples
```bash
$ find ~/git -type d -mindepth 1 -maxdepth 1 | xargs tag-sync "repo"
$ find ~/git -type d -name "*.py" -mindepth 1 -maxdepth 1 | xargs tag-sync "py"
```

#### Links
+   [github.com/jdberry/tag](https://github.com/jdberry/tag)

<p align="center">
    <a href="https://readme42.com/">readme42.com</a>
</p>
