import os
import base64
from google.oauth2 import service_account

from .settings import BASE_DIR

GS_BUCKET_NAME = os.getenv('GS_BUCKET_NAME')
GS_PROJECT_ID = os.getenv('GS_PROJECT_ID')


credentials_base64 = os.getenv('GOOGLE_CREDENTIALS')
if credentials_base64:
    credentials_json = base64.b64decode(credentials_base64).decode('utf-8')
    with open('credentials.json', 'w') as f:
        f.write(credentials_json)

GS_CREDENTIALS = service_account.Credentials.from_service_account_file(os.path.join(BASE_DIR, 'credentials.json'))

# STATICFILES_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage' # static 파일들을 모두 Cloud Storage에 올릴 경우 설정
