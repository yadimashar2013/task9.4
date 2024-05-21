def all_variants(txt):
    for start in range(len(txt)):
        for end in range(start + 1, len(txt) + 1):
            yield txt[start:end]


a = all_variants("abc")
for i in a:
    print(i)
