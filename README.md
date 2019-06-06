<!--
https://pypi.org/project/readme-generator/
https://pypi.org/project/python-readme-generator/
-->

[![](https://img.shields.io/badge/OS-macOS-blue.svg?longCache=True)]()
[![](https://img.shields.io/pypi/v/mac-tag-sync.svg?maxAge=3600)](https://pypi.org/project/mac-tag-sync/)
[![](https://img.shields.io/npm/v/mac-tag-sync.svg?maxAge=3600)](https://www.npmjs.com/package/mac-tag-sync)
[![Travis](https://api.travis-ci.org/looking-for-a-job/mac-tag-sync.svg?branch=master)](https://travis-ci.org/looking-for-a-job/mac-tag-sync/)

#### Installation
```bash
$ [sudo] npm i -g mac-tag-sync
```
```bash
$ [sudo] pip install mac-tag-sync
```

#### Requirements
```bash
$ brew install tag
```

#### Scripts usage
command|`usage`
-|-
`tag-sync` |`usage: tag-sync tag path ...`

#### Examples
```bash
$ find ~/git -type d -mindepth 1 -maxdepth 1 | xargs tag-sync "repo"
$ find ~/git -type d -name "*.py" -mindepth 1 -maxdepth 1 | xargs tag-sync "py"
```

#### Links
+   [github.com/jdberry/tag](https://github.com/jdberry/tag)

<p align="center">
    <a href="https://pypi.org/project/python-readme-generator/">python-readme-generator</a>
</p>