import os
import time

source = 'E:\TestArchive'
target_dir = 'E:\Backup'
target = target_dir + os.sep + time.strftime('%d%b%Y%%%H%M%S') + ' .zip'
zip_command = "zip -qr {0} {1}".format(target, source)

#print(zip_command)

if os.system(zip_command) == 0:
    print("Резервная копия успешно создана в", source)
else:
    print("Создание резервной копии не удалось")