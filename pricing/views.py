from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .forms import MarketingInputsForm
from .models import MarketingData, MarketingData2, MarketingData3
import time
import pandas as pd
from rest_framework.response import Response


def marketing_inputs_form(request):

    return render(request, 'main/index.html')


def update_price(request):
    start_time = time.time()

    inputA = request.GET.get('inputA', 0)
    inputB = request.GET.get('inputB', 0)
    inputC = request.GET.get('inputC', 0)
    marketing_input = MarketingData.objects.get(A=inputA, B=inputB, C=inputC)
    price = marketing_input.Price

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for update_price: {execution_time} seconds")
    return JsonResponse({'price': price})


def upload_excel(request):
    if request.method == "POST":
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        for index, row in df.iterrows():
            MarketingData2.objects.create(width=row['Width'], length=row['Length'], height=row['Height'], price=row['Price'])
        return JsonResponse("success")
    return render(request, "main/upload.html")


def upload_excel_3(request):
    if request.method == "POST":
        excel_file = request.FILES['excel_file']
        df = pd.read_excel(excel_file)
        for index, row in df.iterrows():
            print(row)
            MarketingData3.objects.create(name=row['Название варианта'], width=row['Ширина'], length=row['Длина'], height=row['Высота'],
              price=row['Стоимость'], frame_type=row['Тип каркаса'], roof_type=row['Тип кровли'], wall_type=row['Тип стен'],
              roof_panels=row['Кровельные панели'], wall_panels=row['Стеновые панели'], membrane=row['Тип кровельной мембраны'],
              snow=row['Снеговой район'], wind=row['Ветровой район'])
        return JsonResponse("success")
    return render(request, "main/upload.html")


def update_price2(request):
    start_time = time.time()

    width = request.GET.get('width', 0)
    length = request.GET.get('length', 0)
    height = request.GET.get('height', 0)
    print(f"width    {width}")
    print(f"length    {length}")
    print(f"height    {height}")
    marketing_input = MarketingData2.objects.filter(width=width, length=length, height=height).first()
    price = marketing_input.price

    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for update_price: {execution_time} seconds")
    return JsonResponse({'price': price})


def update_price3(request):
    start_time = time.time()

    name = request.GET.get('name', '')
    width = request.GET.get('width', 0)
    length = request.GET.get('length', 0)
    height = request.GET.get('height', 0)
    frame_type = request.GET.get('frame_type', '')
    roof_type = request.GET.get('roof_type', '')
    wall_type = request.GET.get('wall_type', '')
    roof_panels = request.GET.get('roof_panels', '')
    wall_panels = request.GET.get('wall_panels', '')
    membrane = request.GET.get('membrane', '')
    snow = request.GET.get('snow', '')
    wind = request.GET.get('wind', '')
    # print(f"name: {name}")
    # print(f"width: {width}")
    # print(f"length: {length}")
    # print(f"height: {height}")
    # print(f"frame_type: {frame_type}")
    # print(f"roof_type: {roof_type}")
    # print(f"wall_type: {wall_type}")
    # print(f"roof_panels: {roof_panels}")
    # print(f"wall_panels: {wall_panels}")
    # print(f"membrane: {membrane}")
    # print(f"snow: {snow}")
    # print(f"wind: {wind}")
    marketing_input = MarketingData3.objects.filter(
        # name=name,
        width=width, length=length, height=height,
        frame_type=frame_type,
        roof_type=roof_type,
        wall_type=wall_type, roof_panels=roof_panels,
        wall_panels=wall_panels,
        membrane=membrane,
        snow=snow, wind=wind).first()
    # print(marketing_input)

    try:
        price = marketing_input.price
    except Exception as e:
        price = "Таких параметров нет в базе"
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"Execution time for update_price: {execution_time} seconds")
    return JsonResponse({'price': price,})


def marketing_inputs_form2(request):
    return render(request, 'main/index2.html')


def marketing_inputs_form3(request):
    return render(request, 'main/index3.html')




