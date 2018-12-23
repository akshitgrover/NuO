import re

_range = re.compile("{\\s*range .*}")
_rangeEnd = re.compile("{\\s*endRange\\s*}")

_var = re.compile("{{\\s*[A-Za-z0-9_\-\.]*\\s*}}")

_define = re.compile("{{\\s*define\\s*[A-Za-z0-9_\-]*\\s*[A-Za-z0-9_\-\.]*\\s*}}")

_arithmeticDefine = re.compile("{\\s*define\\s*[a-zA-Z0-9_\-]+\\s*=\\s*((\\s*[a-zA-Z0-9_\-]+\\s*[+*/-]\\s*[a-zA-Z0-9_\-]+\\s*)|(\\s*[+*/-]\\s*[a-zA-Z0-9]+\\s*))*\\s*}")
_arithmetic = re.compile("{{\\s*((\\s*[a-zA-Z0-9_\-]+\\s*[+*/-]\\s*[a-zA-Z0-9_\-]+\\s*)|(\\s*[+*/-]\\s*[a-zA-Z0-9]+\\s*))*\\s*}}")