from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
import cv2
import numpy as np

def index(request):
    return render(request, 'strip/index.html')

@csrf_exempt
def upload_image(request):
    if request.method == 'POST' and request.FILES.get('image'):
        image = request.FILES['image']
        file_name = default_storage.save(image.name, image)
        file_path = default_storage.path(file_name)
        
        colors = process_image(file_path)
        
        color_map = {
            'URO': colors[0],
            'BIL': colors[1],
            'KET': colors[2],
            'BLD': colors[3],
            'PRO': colors[4],
            'NIT': colors[5],
            'LEU': colors[6],
            'GLU': colors[7],
            'SG': colors[8],
            'PH': colors[9]
        }
        
        return JsonResponse(color_map)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def process_image(file_path):
    image = cv2.imread(file_path)
    
    height, width, _ = image.shape
    step = width // 10
    
    colors = []
    for i in range(10):
        x = i * step + step // 2
        color = image[:, x, :].mean(axis=0)
        colors.append(color.astype(int).tolist())
    
    return colors
