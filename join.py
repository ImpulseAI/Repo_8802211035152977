
import os
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(1000000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['zeowx.zip.000.COOL'],'zeowx.zip')
