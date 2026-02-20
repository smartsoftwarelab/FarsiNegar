import json
import re
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from openai import OpenAI
from .models import QuickEdit, DetailedEdit
from django.db.models import Q
from itertools import chain
from operator import attrgetter


def documents(request):
    # دریافت همه داده‌ها بدون فیلتر user (چون این فیلد را ندارید)
    fast_docs = QuickEdit.objects.all()
    detailed_docs = DetailedEdit.objects.all()

    # ادغام و مرتب‌سازی بر اساس زمان ایجاد (time_created)
    combined_documents = sorted(
        chain(fast_docs, detailed_docs),
        key=attrgetter('time_created'),  # نام فیلد زمان شما طبق ارور
        reverse=True
    )

    context = {
        'documents': combined_documents,
    }

    return render(request, 'grammar_app/documents.html', context)

def mood_selection(request):
    return render(request, "grammar_app/mood-selection.html")


def general_correction(request):
    return render(request, "grammar_app/general-correction.py.html")



@csrf_exempt
@require_POST
def general_correction_endpoint(request):
    try:
        data = json.loads(request.body)
        user_input_text = data.get("input_text", "").strip()

        if not user_input_text:
            return JsonResponse({"success": False, "error": "متنی دریافت نشد."}, status=400)

        client = OpenAI(
            api_key="61f6197f08421a461944ec844d469920",
            base_url="https://llm-test.ssl.qom.ac.ir/llm/v1"
        )

        response = client.chat.completions.create(
            model="gpt-oss",
            messages=[
                {
                    "role": "system",
                    "content": """متن زیر را از نظر اشکالات نگارشی، املایی و دستور زبان فارسی بررسی کن. 
        غلط‌ها را اصلاح کن، نگارش را درست کن و در صورت استفاده نادرست از یک کلمه آن را جایگزین کن. 
        همه این کارها را بدون تغییر لحن، سبک، ساختار و محتوای متن انجام بده. 
        کاراکترهای اضافی و غیر مجاز مثل ستاره و ایموجی های غیر ضروری را نیز حذف کن. 
        فقط متن نهاییِ اصلاح‌شده را تحویل بده و هیچ توضیح یا سخن اضافه‌ای ننویس."""
                },
                {
                    "role": "user",
                    "content": user_input_text
                }
            ]
        )

        ai_response = response.choices[0].message.content.strip()
        return JsonResponse({"success": True, "refined_text": ai_response})

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)



@csrf_exempt
@require_POST
def save_document_endpoint(request):
    try:
        data = json.loads(request.body)
        input_text = data.get("input_text", "")
        corrected_text = data.get("corrected_text", "")

        # ساخت عنوان خودکار از ۳۰ کاراکتر اول متن
        title = input_text[:30] + "..." if len(input_text) > 30 else input_text

        new_doc = QuickEdit.objects.create(
            input_text=input_text,
            corrected_text=corrected_text,
            document_title=title
        )
        return JsonResponse({"success": True, "message": "سند ذخیره شد", "id": new_doc.id})
    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


def detailed_correction(request):
    return render(request, "grammar_app/detailed-correction.html")


# Add this to your views.py file

@csrf_exempt
@require_POST
def detailed_correction_endpoint(request):
    """
    دریافت متن و برگرداندن لیست خطاها
    """
    try:
        data = json.loads(request.body)
        user_input_text = data.get("input_text", "").strip()

        if not user_input_text:
            return JsonResponse({"success": False, "error": "متنی دریافت نشد."}, status=400)

        client = OpenAI(
            api_key="61f6197f08421a461944ec844d469920",
            base_url="https://llm-test.ssl.qom.ac.ir/llm/v1"
        )

        # پرامپت برای دریافت خطاها به صورت JSON
        system_prompt = """شما یک ویراستار حرفه‌ای فارسی هستید. 
         
        غلط‌ها را اصلاح کن، نگارش را درست کن و در صورت استفاده نادرست از یک کلمه آن را جایگزین کن. 
        همه این کارها را بدون تغییر لحن، سبک، ساختار و محتوای متن انجام بده. 
        کاراکترهای اضافی و غیر مجاز مثل ستاره و ایموجی های غیر ضروری را نیز حذف کن. 
        فقط متن نهاییِ اصلاح‌شده را تحویل بده و هیچ توضیح یا سخن اضافه‌ای ننویس
        
متن را بررسی کنید و لیست خطاها را به صورت JSON برگردانید.
فرمت پاسخ شما باید دقیقاً به این صورت باشد:
[
  {
    "wrong": "کلمه یا عبارت اشتباه",
    "correct": "پیشنهاد صحیح",
    "type": "نوع خطا (املایی/نگارشی/دستوری)"
  }
]
فقط JSON را برگردانید، بدون توضیح اضافی."""

        response = client.chat.completions.create(
            model="gpt-oss",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input_text}
            ]
        )

        ai_response = response.choices[0].message.content.strip()

        # پاکسازی پاسخ از markdown code blocks
        ai_response = re.sub(r'^```json\s*', '', ai_response)
        ai_response = re.sub(r'\s*```$', '', ai_response)
        ai_response = ai_response.strip()

        # تبدیل به JSON
        try:
            error_list = json.loads(ai_response)
        except json.JSONDecodeError:
            # اگر پاسخ JSON معتبر نبود، لیست خالی برگردانید
            error_list = []

        return JsonResponse({
            "success": True,
            "errors": error_list
        })

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)


@csrf_exempt
@require_POST
def save_detailed_document_endpoint(request):
    """
    ذخیره متن و لیست خطاها در دیتابیس
    """
    try:
        data = json.loads(request.body)
        content = data.get("content", "")
        error_list = data.get("error_list", [])

        # ساخت عنوان خودکار از ۳۰ کاراکتر اول متن
        title = content[:30] + "..." if len(content) > 30 else content

        new_doc = DetailedEdit.objects.create(
            content=content,
            error_list=error_list,
            document_title=title
        )

        return JsonResponse({
            "success": True,
            "message": "سند با موفقیت ذخیره شد",
            "id": new_doc.id
        })

    except Exception as e:
        return JsonResponse({"success": False, "error": str(e)}, status=500)