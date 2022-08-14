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
  #bucket_name is the name of main bucket
  bucket_name = " "

  # Mount data from Drive to Google Storage
  #Dataset is the folder in my drive which contains the images
  !gsutil -m cp -rn /content/drive/MyDrive/Dataset/* gs://{bucket_name}/
    
if __name__ == '__main__':
    main()
