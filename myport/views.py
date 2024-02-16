from django.shortcuts import render, HttpResponse,redirect
from myport.models import mail
from django.core.mail import send_mail
# Create your views here.


def index(request):
    return render(request, "index.html")


def send_mail_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        obj = mail(name=name, email=email, message=message)
        obj.save()
        # data = mail.objects.get(id=id)
        # data.mail = request.POST.get("mail")
        # data.save()
        subject = "Hello Dear"  
        msg     = "We glad to recieve from you and we get in touch with you soon!!"+" "
        from_email = "joshuaakototamakloe@gmail.com"
        recipient_list = [email]
        
        d=send_mail(subject, msg, from_email, recipient_list)
        if d == 1:
            return redirect('/response')
    else:
        return render(request, 'response.html')
    
    
def Response_my(request):
    return render (request,"response.html")


# def contact(request):
#     id = request.GET.get("id",None)
#     if id is not None:
#         obj = mail.objects.filter(pk=id).first()
#         return render(request,"contact.html",{"obj":obj})
#     else:
#         q = request.GET.get("q","")
#         objs = mail.objects.filter(Q(name__icontains=q)|Q(email__icontains=q)).order_by("-id")
#         return render(request,"contact.html",{"objs":objs,"q":q})