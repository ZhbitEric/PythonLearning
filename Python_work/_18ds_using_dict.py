# 字典,键值对，键不能相同，无序
ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

print(ab)
print(ab['Swaroop'])

del ab['Swaroop']
print(ab)

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# 增加
ab['google'] = 'google.com'
if 'google' in ab:
    print(ab['google'])

# 删除
ab.pop('Larry')
print(ab)
