import os
import shutil
import time

del main():
  deleted_folder_counts-0
    deleted_file_counts-0

    path= "C:\Users\LENOVO\Desktop\Class\BuzzApp"

    days=30

    seconds = time.time() - (days*24*60*60)

    if os.path.exists(path):

        for root_folder,folders,files in os.walk(path):

            if seconds >= get_file_or_folder_age(root_folder):

                remove_folder(root_folder)
                deleted_folder_counts +=1

                break:

            else:

                for folder in folders:

                    folder_path = os.path.join(root_folder,folder)
                    if seconds >= get_file_or_folder_age(folder_path):
                        remove_folder(folder_path)
                        deleted_folder_counts+=1

            else:
                print(f"{path}is not found")
                deleted_folder_counts+=1
                print('Total folders deleted':{deleted_folder_counts})
                print('Total files deleted':{deleted_file_counts})

del remove_folder(path):

    if not shutil.rmtree(path):
          print(f"{path}is removed successfully")

    else:
        print(f"unable to delete the"+path)

del remove_file(path):
    if not os.remove(path):
         print(f"{path}is not found")
    else:
        print("not removed successfully"+path)
    
  





