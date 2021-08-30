import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a folder to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.A3VBQIhl62QQ6BKxWCmkvO4n3QCqG5vzbcVN8gpqiFRJtELB93C887yyx42sgbTsKJrvn_pRYdpovoD3n7SXygtpHtCJ_xBjslmkHKDV4Ui5PCboYrXkNl1aafIulQ_l1CsI3qw'
    transferData = TransferData(access_token)

    file_from = input("Enter the folder path to transfer")
    file_to = input("Enter the full path to upload to dropbox (/cloudstorage/sample2.txt)")

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()