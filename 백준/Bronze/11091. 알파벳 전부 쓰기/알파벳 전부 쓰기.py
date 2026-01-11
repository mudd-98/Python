N = int(input())

for _ in range(N):
    s = input().lower()
    letters = {c for c in s if c.isalpha()}
    
    if len(letters) == 26:
        print("pangram")
    else:
        missing = ""
        for i in range(26):
            ch = chr(ord('a') + i)
            
            if ch not in letters:
                missing += ch
        print(f"missing {missing}")