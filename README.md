# Mark Tree

The **Mark Tree** library is a markdown to JSON converter that transforms Markdown documents into a structured JSON format, ideal for working with long documents like books.

## Installation

Install the library using pip:

```bash
pip install mark-tree
```

## Basic Usage

Basic conversion example:

```python
from mark_tree import from_mark

with open('file.md', 'r', encoding='utf-8') as f:
  markdown_content = f.read()

json_tree = from_mark(markdown_content)

print(json_tree)
```

## Conversion Rules

### Frontmatter

The Markdown document MUST start with a frontmatter block that includes:

- **Title**: The title of the document.

- **Author**: The author of the document.

- **Language**: The language of the document.

- **Translator**: The translator of the document (if applicable).

- **Date**: The publication or creation date of the document.

### Sections and content

In the conversion process, each markdown heading represents a section within the document. The depth of each section is determined by the level of the heading.

Content that appears immediately below each heading is considered part of that section. This content is preserved as string in Markdown format in the content field of the section object.

## Example Conversion

### Markdown

```markdown
---
title: The Pathway of Life
author: Leo Tolstoy
language: en
translator: Archibald J. Wolfe
date: 1919-01-01
---

# The Pathway of Life

## Force

One of the main causes of human misery is the erroneous idea that some men may by force order or improve the life of others.

### The Inefficiency of Force

The fact that it is possible to make men amenable to justice by the use of force, does not yet prove that it is just to subject people to force.

_Pascal_
```

### JSON

```json
{
  "title": "The Pathway of Life",
  "author": "Leo Tolstoy",
  "language": "en",
  "translator": "Archibald J. Wolfe",
  "date": "1919-01-01",
  "sections": [
    {
      "depth": 1,
      "title": "The Pathway of Life",
      "content": null,
      "position": 1
    },
    {
      "depth": 2,
      "title": "Force",
      "content": "One of the main causes of human misery is the erroneous idea that some men may by force order or improve the life of others.",
      "position": 2
    },
    {
      "depth": 3,
      "title": "The Inefficiency of Force",
      "content": "The fact that it is possible to make men amenable to justice by the use of force, does not yet prove that it is just to subject people to force. _Pascal_",
      "position": 3
    }
  ]
}
```

## Contributions

Open an issue or submit a pull request for suggestions or improvements.

## License

This project is licensed under the [MIT License](LICENSE).
