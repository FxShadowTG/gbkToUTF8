import os
def file_name(file_dir):
    a=list(os.walk(file_dir))[0][2]
    for files in a:
        if '.csv' not in files:
            list(a).remove(files)
      
        return a
        
#转excel文件scv, utf8 to gbk格式编码
#路径
path='C:\\Users\\FxShadow\\Desktop\\achievement\\achievement'
ttt=file_name(path)
 
 
for target in ttt:
 
    fd = open(path+'\\'+target, 'r',encoding='utf-8')    
    t=fd.readlines()
    with open(path+'\\'+target, 'w', encoding="gbk") as dst:    
        for line in t:
 
            dst.write(line)
    fd.close()
    dst.close()