from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import ContactForm, UserForm
from django.contrib import messages
from general_app.forms import ContactForm
from openai import OpenAI
import json

def home_page(request):
    return render(request, 'general_app/home_page.html')

@csrf_exempt
@require_POST
def refine_text_endpoint(request):
    try:
        data = json.loads(request.body)
        user_input_text = data.get("input_text", "").strip()

        if not user_input_text:
            return JsonResponse({
                "success": False,
                "error": "متنی برای اصلاح دریافت نشد."
            }, status=400)

        client = OpenAI(
            api_key= '61f6197f08421a461944ec844d469920',
            base_url="https://llm-test.ssl.qom.ac.ir/llm/v1"
        )

        ai_prompt_text = (
            " شما یک ویراستار حرفه‌ای زبان فارسی هستید."
            "وظیفه شما اصلاح املایی، دستوری و بهبود روانی متن است."
            "لحن، سبک نوشتار و منظور نویسنده را کاملاً حفظ کن."
            "  از افزودن توضیح، تیتر، بولت پوینت یا متن اضافی خودداری کن."
            "خروجی فقط متن اصلاح‌شده نهایی باشد."
            
            "متن زیر را بدون تغییر لحن و بدون اضافه‌کردن هیچ توضیحی،"
            "فقط از نظر املایی، دستوری و روانی جمله‌ها اصلاح کن و اگر کلمه بهتری میتوانی جایگزین کن"
            
            f"{user_input_text}"
        )

        response = client.chat.completions.create(
            model="gpt-oss",
            messages=[ #type_ignore
                {"role": "system", "content": "شما یک ویراستار حرفه‌ای فارسی هستید."},
                {"role": "user", "content": ai_prompt_text}
            ]
        )

        ai_response = response.choices[0].message.content

        return JsonResponse({
            "success": True,
            "refined_text": ai_response.strip()
        })

    except Exception as e:
        print("AI ERROR:", e)
        return JsonResponse({
            "success": False,
            "error": "خطایی در سرور رخ داد."
        }, status=500)


def about_us(request):
    return render(request, 'general_app/about-us.html')


def contact_us(request):
    form = ContactForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            contact = form.save(commit=False)
            contact.user_ip = request.META.get('REMOTE_ADDR')

            contact.save()
            return redirect("contact-us")
    else:
        form = ContactForm()

    return render(request, "general_app/contact-us.html",
                  {"form": form, "message": messages})


def sign_in(request):
    return render(request, 'general_app/sign-in.html')

def sign_up(request):
    form = UserForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("homepage")
    else:
        form = UserForm()

    return render(request, 'general_app/sign-up.html', {"form": form})


