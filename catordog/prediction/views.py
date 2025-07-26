from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .forms import ImageUploadForm
import random

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
            # 4章で、判定結果のロジックを追加
            # 暫定で、ダミーの判定結果としてpredictionにランダムで「猫」か「犬」を格納
            prediction = random.choice(["猫", "犬"])
            return render(request, 'home.html', {'form': form, 'prediction': prediction})
        else:
            form = ImageUploadForm()
            return render(request, 'home.html', {'form': form})