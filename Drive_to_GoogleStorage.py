# This program will upload drive folder to Google Storage
from google.colab import drive
drive.mount('/content/drive')

from google.colab import auth
auth.authenticate_user()

# project id of the GCP
project_id = ""
!gcloud config set project {project_id}
!gsutil ls

# data = Path of folder of the drive
data = " "
folderArray = np.array(os.listdir(data))
def main():

  #bucket_name is the name of main bucket in Google Cloud Storage
  bucket_name = " "
  #1st-for-loop to traverse folders of the Dataset Folder
  for currentFolder in folderArray:
    data2 = bucket_name + currentFolder + "/"
    # Moount data from Drive to Google Storage
    
    !gsutil -m cp -rn '''path of the drive folders''' gs://{data2}/

if __name__ == '__main__':
    main()
