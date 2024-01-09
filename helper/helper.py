from config.config import Config
from werkzeug.utils import secure_filename
import os
import base64

import base64
def save_file_blob(photo_data, filename):
    photo_data.save(os.path.join(Config.UPLOAD_PATH, filename))

def blob_to_base64(blob_data):
    try: 
        blob_data = blob_data.getvalue().decode()  # Konversi dari BytesIO ke string
        blob_data = blob_data.split(",")[1]  # Pisahkan data blob dari prefix "data:image/png;base64,"
        return base64.b64decode(blob_data)
    except Exception as e:
        raise e
