text = 'Мама мыла раму!'

print({n: text.lower().count(n) for n in set(text.lower()) if n.isalpha()})
