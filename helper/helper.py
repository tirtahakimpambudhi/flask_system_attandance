from config.config import Config
from werkzeug.utils import secure_filename
import os
import base64



def save_file_blob(blob_data,filename) :
        blob_data = blob_data.split(",")[1]
        photo = base64.b64decode(blob_data)
        filename = secure_filename(filename)
        filepath = os.path.join(os.getcwd(),Config.UPLOAD_PATH, filename)
        with open(filepath, 'wb') as f:
            f.write(photo)
def blob_to_base64(blob_data):
        try : 
                blob_data = blob_data.split(",")[1]
                return base64.b64decode(blob_data)
        except Exception as e:
               raise e