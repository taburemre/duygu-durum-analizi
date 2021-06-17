from keras.models import load_model
from keras.preprocessing.image import img_to_array
import numpy as np
import cv2
import settings

# Duygu durum modeli
emotion_model = load_model(settings.DATA['models']['emotion'], compile=False)
 # Cinsiyet modeli
gender_model = load_model(settings.DATA['models']['gender'], compile=False)
# Yüz tespiti için gerekli XML verisi
face_cascade = cv2.CascadeClassifier(settings.DATA['cascades']['face'])


gender = ["women", "man"]

emolation = ["angry", "disgurd", "afraid", "happy", "sad", "suprizing", "notr"]


def cam_detect ( frame ) :
    # Görüntüyü gri tona çeviriyoruz
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Oluşturulan gri görüntüden yüzleri tespit ediyoruz
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)


    frameClone = frame.copy()

    for (x, y, w, h) in faces :

        roi = gray[y :y + h, x :x + w]
        roi = cv2.resize(roi, (64, 64))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        preds = emotion_model.predict(roi)[0]
        emotion_probability = np.max(preds)

        preds1 = gender_model.predict(roi)[0]
        gender_probability = np.max(preds1)

        label = [" Duygu durumu: " + str(emolation[preds.argmax()]) + " (%" + str(round(emotion_probability * 100, 2)) + ") ",
                 " Cinsiyet: " + str(gender[preds1.argmax()]) + " (%" + str(round(gender_probability * 100, 2)) + ") "]

        negatifrotate = [62, 30]

        cv2.rectangle(frameClone, (x, y - 90), (x + w, y - 15), (255, 0, 0), 5)
        cv2.rectangle(frameClone, (x, y - 90), (x + w, y - 15), (255, 0, 0), -1)

        for i in range(0, 2) :
            cv2.putText(frameClone, label[i], (x, y - negatifrotate[i]), cv2.FONT_HERSHEY_SIMPLEX, float((w) / 600),
                        (255, 255, 255), 2)

        cv2.rectangle(frameClone, (x, y), (x + w, y + h), (255, 0, 0), 5)

    return frameClone