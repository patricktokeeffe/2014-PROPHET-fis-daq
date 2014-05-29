#!python
import sys, re, subprocess

target = 'crbasic/default.cr3'
template = 'Const VERSION = "%s"'
regexp = r'[\.0-9a-zA-Z-]*'
to_find = re.compile(template % regexp)

if sys.argv[1] == '--insert': # post-commit hook
    vstr = subprocess.check_output('git describe --tags --dirty', shell=True)
    new_str = template % vstr.strip()
    input = open(target, mode='r').read()
    open(target, mode='w').write(re.sub(to_find, new_str, input))
elif sys.argv[1] == '--remove': # clean filter (smudge is no-op)
    new_str = template % ''
    sys.stdout.write(re.sub(to_find, new_str, sys.stdin.read()))
else:
    raise RuntimeError()
