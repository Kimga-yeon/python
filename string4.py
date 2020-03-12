
print('to {}.Lorem ipsum dolor sit amet {}, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.{} Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat{}. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format('gayeon','12','gayeon','gayeon'))

#포지셔닝 포맷팅 positional formating 위치기반
#{}안에 있는데이터를 순서대로 바꿀때

print('to {name}.Lorem ipsum dolor sit amet {age:d}, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.{name} Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat{name}. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.format(name='ga yeon', age = 12))

#네임드 포맷팅 named pomating 이름기반

#{age:d} 라고 쓰면 무조건 숫자 ..문자쓰면 에러남
