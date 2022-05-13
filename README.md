# LiteralCopy

[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/copy-syntax)](https://pypi.org/project/copy-syntax/)
[![PyPI Status](https://badge.fury.io/py/copy-syntax.svg)](https://badge.fury.io/py/copy-syntax)
[![PyPI Status](https://pepy.tech/badge/copy-syntax)](https://pepy.tech/project/copy-syntax)
![Tests](https://github.com/cemde/LiteralCopy/actions/workflows/tests.yml/badge.svg)
[![codecov](https://codecov.io/gh/cemde/copy-syntax/branch/main/graph/badge.svg)](https://codecov.io/gh/cemde/copy-syntax)
[![ReadTheDocs](https://readthedocs.org/projects/copysyntax/badge/?version=stable)](https://copysyntax.readthedocs.io/en/stable/)
[![license](https://img.shields.io/badge/License-%20GPLv3-blue.svg)](https://github.com/cemde/CopySyntax/blob/master/LICENSE)

## Features

Literal copy is a light-weight Python library to create the syntax string of objects in memory.

For example:

```python
import copy_syntax as cs
supercoolexample = "Here"
cs.syntax("Hello World")
cs.syntax([1,2])
cs.syntax_like([1,5,2])
```

## Install

To install stable version from PyPI use

```
pip install copy-syntax
```

To install from git use

```
pip install git+iNSERT LINK
```

## Documentation

The documentation is published at [ReadTheDocs](https://copysyntax.readthedocs.io/en/stable/).

The docs contain:

-   Api Reference
-   Examples

## Contribute

Any contributions welcome. Please open a PR.
