import sys
A = open(sys.argv[1]).read().strip()
lines = A.split('\n')

B = [[c for c in row] for row in lines]
C = len(B)
D = len(B[0])

for r in range(C):
  for c in range(D):
    if B[r][c]=='S':
      sr,sc = r,c
      Up = (B[r-1][c] in ['|','7','F'])
      Right = (B[r][c+1] in ['-','7','J'])
      Down = (B[r+1][c] in ['|','L','J'])
      Left = (B[r][c-1] in ['-','L','F'])
      assert sum([Up, Right, Down, Left]) == 2
      if Up and Down:
        B[r][c]='|'
        sd = 0
      elif Up and Right:
        B[r][c]='L'
        sd = 0
      elif Up and Left:
        B[r][c]='J'
        sd = 0
      elif Down and Right:
        B[r][c]='F'
        sd = 2
      elif Down and Left:
        B[r][c]='7'
        sd = 2
      elif Left and Right:
        B[r][c]='-'
        sd = 1
      else:
        assert False

AB = [-1,0,1,0]
CD = [0,1,0,-1]
r = sr
c = sc
d = sd
dist = 0
while True:
  dist += 1
  r += AB[d]
  c += CD[d]
  if B[r][c]=='L':
    if d not in [2,3]:
      break
    elif d==2:
      d = 1
    else:
      d = 0
  if B[r][c]=='J':
    if d not in [1,2]:
      break
    elif d==1:
      d = 0
    else:
      d = 3
  if B[r][c]=='7':
    if d not in [0,1]:
      break
    elif d==0:
      d = 3
    else:
      d = 2
  if B[r][c]=='F':
    if d not in [0,3]:
      break
    elif d==0:
      d = 1
    else:
      d = 2
  assert B[r][c] != '.'
  if (r,c) == (sr,sc):
    print(dist//2)
    break