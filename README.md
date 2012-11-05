chisel
===========

My fork of [chisel](https://github.com/dz/chisel), a static blog generator.

Requires

* jinja2
* markdown

Github syntax highlighting requires a change in the fenced_code extension for markdown.

```
r'(?P<fence>^`{3,})[ ]*(?P<lang>[a-zA-Z0-9_-]*)[ ]*\n(?P<code>.*?)(?P=fence)[ ]*$'
```

Tested on Python 2.7.3 only.