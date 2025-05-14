def extract_file(data):
    needed_information = data[-1].split('.')
    file_name = needed_information[0]
    extension = needed_information[1]

    print(f'File name: {file_name}')
    print(f'Extension: {extension}')



d = input().split('\\')

extract_file(d)

#В тази задача задаваме име на файл и неговото разширение
# и програмата извлича само името и разширението без целия адрес
#примерен вход-------------------------------
# C:\Internal\training-internal\Template.pptx