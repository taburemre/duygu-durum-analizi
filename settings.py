import os

# Proje dizini
BASE_DIRECTORY = os.path.abspath(os.getcwd())

# Analiz kaynakları
SOURCES = {
    'picture': 'Picture',
    'camera': 'Camera',
}

# DataSet
DATA = {
    'cascades': {
        # Yüz tespiti için gerekli XML dosyasının yolu
        'face': os.path.join(BASE_DIRECTORY, 'models', 'haarcascade_frontalface_default.xml'),
        # Göz tespiti için gerekli XML verisi
        'eye': os.path.join(BASE_DIRECTORY, 'data', 'cascades', 'haarcascade_eye.xml'),
        # Gülümseme tespiti için gerekli XML verisi
        'smile': os.path.join(BASE_DIRECTORY, 'data', 'cascades', 'haarcascade_smile.xml'),
    },
    'models': {
        # Yüz ifadesi modeli
        'emotion': os.path.join(BASE_DIRECTORY, 'models', 'fer2013_mini_XCEPTION.110-0.65.hdf5'),
        # Cinsiyet modeli
        'gender': os.path.join(BASE_DIRECTORY, 'models', 'gender_mini_XCEPTION.21-0.95.hdf5'),
    },
}

# Duygu durumları
EMOTIONS = ['Angry', 'Disgurd', 'Afraid', 'Happy', 'Sad', 'Suprizing', 'Notr']

# Cinsiyetler
GENDERS = ['Woman', 'Man']
