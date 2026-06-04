import telebot
from django.conf import settings
from django.utils import timezone
from django.shortcuts import render, redirect

import main.models as models

group_id = settings.GROUP_ID
bot = telebot.TeleBot(settings.BOT_TOKEN)


def generate_text(name, email, phone, message):
    return (f"New Contact"
            f"Name: {name}\n"
            f"Email: {email}\n"
            f"Phone: {phone}\n"
            f"Message: {message}\n"
            f"Added at: {timezone.now().strftime('%Y-%m-%d %H:%M')}")


# Create your views here.
def home(request):
    faqs = models.Faq.objects.all()  # [item, item,]
    members = models.TeamMember.objects.all()
    if request.POST:
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get('phone')
        message = request.POST.get('comments')
        models.Contact.objects.create(
            name=name, email=email,
            phone=phone, message=message
        )
        text = generate_text(name, email, phone, message)
        bot.send_message(group_id, text)
        return redirect("/")
    context = {
        "faqs_list": faqs,
        "members": members
    }
    return render(request, "index.html", context)
