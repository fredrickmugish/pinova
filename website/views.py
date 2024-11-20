from django.shortcuts import render
from django.core.mail import EmailMessage
from django.conf import settings
from django.http import JsonResponse
import os

# Create your views here.
def home(request):
    return render(request, 'index.html')
def about_page(request):
    return render(request, 'about.html')
def services_page(request):
    return render(request, 'services.html')
def work_page(request):
    return render(request, 'work.html')
def contact_page(request):
    return render(request, 'contact.html')

def contact_data(request):
    if request.method == "POST":
        # Retrieve form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        description = request.POST.get("description")
        requirements_doc = request.FILES.get("requirements_doc")

        # Save the uploaded file if it exists
        file_path = None
        if requirements_doc:
            file_path = os.path.join(settings.MEDIA_ROOT, requirements_doc.name)
            with open(file_path, "wb+") as destination:
                for chunk in requirements_doc.chunks():
                    destination.write(chunk)

        # Prepare the email
        subject = f"New Contact Submission from {name}"
        message = f"Name: {name}\nEmail: {email}\n\nDescription:\n{description}"
        email_message = EmailMessage(
            subject=subject,
            body=message,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=['fredrickgotfried@gmail.com'],  # Replace with your recipient email
        )

        # Attach file if uploaded
        if file_path:
            email_message.attach_file(file_path)

        # Attempt to send the email
        try:
            email_message.send()
            return JsonResponse({
                'status': 'success',
                'message': 'Your message has been sent successfully! We will get back to you soon.'
            })
        except Exception as e:
            return JsonResponse({
                'status': 'error',
                'message': f'Failed to send email: {e}'
            }, status=500)

    return JsonResponse({
        'status': 'error',
        'message': 'Invalid request method.'
    }, status=400)