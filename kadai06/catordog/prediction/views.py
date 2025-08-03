# Create your views here.
from django.shortcuts import render
from .forms import ImageUploadForm
import random
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.models import save_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.vgg16 import decode_predictions
from PIL import Image
from tensorflow.keras.applications.vgg16 import preprocess_input

model = VGG16(weights='imagenet')
save_model(model, 'dummy_vgg16.h5')

def predict(request):
    if request.method == 'GET':
        form = ImageUploadForm()
        return render(request, 'home.html', {'form': form})
    if request.method == 'POST':
        # POSTリクエストによるアクセス時の処理を記述
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            img_file = form.cleaned_data['image']

            # 4章で、画像ファイル（img_file）の前処理を追加

            # PILで開いて画像前処理
            img = Image.open(img_file).convert('RGB')
            img = img.resize((224, 224))  # VGG16の入力サイズにリサイズ
            unknown_array = img_to_array(img)
            unknown_array.shape
            unknown_array = unknown_array.reshape((1, 224, 224, 3))
            unknown_array = preprocess_input(unknown_array)
            # 4章で、判定結果のロジックを追加
            result = model.predict(unknown_array)        
            prediction = decode_predictions(result)[0]            
            return render(request, 'home.html', {
                'form': form, 
                'prediction': prediction
            })
        else:
            form = ImageUploadForm()
            return render(request, 'home.html', {'form': form})