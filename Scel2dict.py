# Scel格式转fcitx5识别的dict格式
# 借助/usr/bin/scel2org5和/usr/bin/libime_pinyindict实现

import os,sys
import subprocess

def scel2dict(input_dir, output_dir):
    # 创建保存路径
    try:
        os.mkdir(output_dir)
    except Exception as e:
        print(e)
    # 遍历文件夹下的文件
    for parent, dirnames, filenames in os.walk(input_dir):
        sub_dir = os.path.join(parent.replace(input_dir, output_dir))
        try:
            os.mkdir(sub_dir)
        except Exception as e:
            print(e)
        # 批量处理文件
        for filename in filenames:
            if os.path.exists(os.path.join(sub_dir, filename.replace('.scel', '.dict'))):
                print(filename + ">>>>>>文件已存在")
            else:
                try:
                    subprocess.run(["/usr/bin/scel2org5", os.path.join(parent, filename), "-o", os.path.join(sub_dir, filename.replace('.scel', '.txt'))])
                    subprocess.run(["/usr/bin/libime_pinyindict", 
                                        os.path.join(sub_dir, filename.replace('.scel', '.txt')), 
                                        os.path.join(sub_dir, filename.replace('.scel', '.dict'))])
                    subprocess.run(["rm", os.path.join(sub_dir, filename.replace('.scel', '.txt'))])
                    print(filename + ">>>>>>dict转换成功")
                except Exception as e:
                    print(e)

if __name__ == '__main__':
    scel2dict('scel', 'dict')