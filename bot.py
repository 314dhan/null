import os

for i in range(400):
    d = str(i) + ' days ago'
    with open('test.txt','a') as file:
        file.write(d+'\n')
    os.system('git add test.txt')
    os.system(f'git commit --date="{d}" -m "Commit from {d}"')
os.system('git push -u origin main')