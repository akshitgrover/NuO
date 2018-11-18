import re

_range = re.compile("{\\s*range .*}")

_var = re.compile("{{\\s*[A-Za-z0-9_\-\.]*\\s*}}")