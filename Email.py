def full_email(people):
  result=[]
  for email, name in people:
    result.append(f'{name} <{email}>')
  return result

print(full_email([('sam@gmail.com', 'sam john')]))