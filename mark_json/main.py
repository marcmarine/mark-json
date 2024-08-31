
import re
import yaml

def from_mark(markdown_content):
  frontmatter, content = split_frontmatter(markdown_content)

  metadata = yaml.safe_load(frontmatter)

  sections = parse_markdown_structure(content)

  json = {
    'title': metadata.get('title', ''),
    'author': metadata.get('author', ''),
    'language': metadata.get('language', ''),
    'translator': metadata.get('translator', ''),
    'date': str(metadata.get('date', '')),
    'sections': sections
  }

  return json

def split_frontmatter(markdown_content):
  frontmatter_match = re.match(r'^---\s*\n(.*?)\n---\s*\n(.*)', markdown_content, re.DOTALL)

  if frontmatter_match:
    frontmatter = frontmatter_match.group(1)
    content = frontmatter_match.group(2)
  else:
    frontmatter = ''
    content = markdown_content

  return frontmatter, content

def parse_markdown_structure(markdown_content):
  sections = []
  current_section = None
  header_level = None
  position = 1

  lines = markdown_content.splitlines()

  for line in lines:
    match = re.match(r'^(#+)\s+(.*)', line)

    if match:
      if current_section:
          current_section['content'] = current_section['content'].strip()
          if not current_section['content']:
              current_section['content'] = None
          sections.append(current_section)

      header_level = len(match.group(1))
      current_title = match.group(2).strip()
      current_section = {
          'depth': header_level,
          'title': current_title,
          'content': '',
          'position': position
      }
      position += 1
    else:
      if current_section:
          current_section['content'] += line + '\n'

  if current_section:
    current_section['content'] = current_section['content'].strip()
    if not current_section['content']:
        current_section['content'] = None
    sections.append(current_section)

  return sections