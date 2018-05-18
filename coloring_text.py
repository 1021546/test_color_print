from colorama import init
init()
ok = '\033[92m'
fail = '\033[91m'
close = '\033[0m'
print(ok + '☑' + close, end=' ')

# https://stackoverflow.com/questions/48445616/why-printing-in-color-in-a-windows-terminal-in-python-does-not-work
# pip install colorama