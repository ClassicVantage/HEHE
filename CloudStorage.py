import os
import dropbox
class TransferData():
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
      dbx=dropbox.Dropbox9(self.access_token)
      for root,dirs,files in os.walk(file_from):
          for fileName in files:
            local_path=os.path.join(root,fileName)
            relative_path=os.path.relpath(local_path,file_from)
            dropbox_path=os.path.join(file_to,relative_path)
            with open(local_path,'rb') as f:
                 dbx.files_upload(f.read(), dropbox_path,mode=WriteMode('overWrite'))

            
            
                     
def main():
    access_token = 'sl.AxCDdlu24RvwZQnksZyFLrrlTo93E2QeteFlbMY8sK82gmyomCQm0CirAWU3fRfbKYJk65nYguud-E-0aQxwZahJwRSEMcf0aUz2TIqJONWrQx-3TxFBUhwdG1PM3FBWfuQ7sMc'
    transferData = TransferData(access_token)
    file_from = input("write the file name")
    file_to = input("write the file path")

    transferData.upload_file(file_from,file_to)
    print("file moved")

main()
    