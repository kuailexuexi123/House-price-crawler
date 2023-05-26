def writefile(file_name,content_str):
    with open(file_name,'a',encoding='utf-8') as f:
        f.write(content_str)
        f.close()