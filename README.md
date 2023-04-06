# README

## Overview

A brief description. Be clear about the purpose of the hook,
its capabilities and limitations.

## Installation

Installation instructions

To install directly from PyPI
```shell
pip install sceptre-hook-template
```

To install from the git repo
```shell
pip install git+https://github.com/Sceptre/sceptre-hook-template.git
```

## Usage/Examples

```yaml
parameters|sceptre_user_data:
  <name>: !custom <args>
```

## Example

```yaml
before_create:
  - !custom "HelloWorld"
```
