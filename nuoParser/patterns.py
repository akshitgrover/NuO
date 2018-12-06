import re

_range = re.compile("{\\s*range .*}")
_rangeEnd = re.compile("{\\s*endRange\\s*}")

_var = re.compile("{{\\s*[A-Za-z0-9_\-\.]*\\s*}}")

_define = re.compile("{{\\s*define\\s*[A-Za-z0-9_\-]*\\s*[A-Za-z0-9_\-\.]*\\s*}}")