states = ['Alabama', 'California', 'Oklahoma', 'Florida']
vowels = list('aeiou')
result = []
for state in states:
  state_list = list(state.lower())
  for letter in vowels:
    while True:
      try:
        state_list.remove(letter)
      except:
        break
  result.append(''.join(state_list).capitalize())
  
print(result)
      