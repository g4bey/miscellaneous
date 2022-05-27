import os
import  csv
import requests

#
# This script simply download every singled attachement referenced in your discord archive.
#

working_directory = 'D:\Librairies\Downloads\package\messages'
result_directory = "D:\Librairies\Downloads\discord_attachements"

os.chdir(working_directory)
items = os.listdir(working_directory)

attachments = []

for item in items:
    if os.path.isdir(item):
        with open(f'{item}/messages.csv', 'r', encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                if (attachment := row[3]) and attachment != 'Attachments':
                    [attachments.append(url) for url in attachment.split(' ')]


if not os.path.exists(result_directory):
    os.makedirs(result_directory) 
    
os.chdir(result_directory)
                    
with open('links.txt', 'w') as result:
    result.write('\n'.join(attachments))

nb_attachements = len(attachments)

print(nb_attachements)
for i, url in enumerate(attachments):
    response = requests.get(url)
    name = url.split('/')[-1]
    
    if response.status_code == 200:
        with open(f'{name}.{i}', 'wb') as file:
             file.write(response.content)
             print('Downloading', name, '---' ,nb_attachements - (i + 1), 'more to go!')
