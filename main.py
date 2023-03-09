import os
import openai
from gpt import ai

with open('key.txt', 'r') as f:
    openai.api_key = f.read()

with open('example_mail.txt', 'r') as f:
    var1 = f.read()

with open('info.txt', 'r') as f:
    var2 = f.readline().replace('\n', '')

for i in var2:
    url = 'https://github.com/Rukiren/create_your_list'
    prompt = f'<<mail>> = {var1}, <<name_list>> = {i}, 請以 <<mail>> 為模板，生成給<<name_list>>的信件，信件開頭與結尾不要做變更，內容結構不要過多修改，依據廠商有點不同小變動，輸出信件須為中文，廠商名稱需要完整，信件完成加上三行換行，便於存檔'
    response = ai(prompt)

    print(response)
    with open('output.txt', 'a') as f:
        f.write(response)

    