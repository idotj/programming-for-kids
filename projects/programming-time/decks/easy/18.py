# | computer memory             |
# |.............................|
# |..1 6........................|
# |..^..........................|
# |..|..........................|
# |..|........1 3...............|
# |..|........|.................|
# '--+--------+-----------------'
#    |        |
# a -+        |
# a ----------+
#
# The variable 'a' in hello()
# is different than the 'a'
# defined outside.

def hello():
  a = 3

a = 6
hello()

print(a)
