from django.shortcuts import render
from django.template import RequestContext
# Create your views here.
info_list=[]

def userInfor(req):

    if req.method=="POST":
        username=req.POST.get("username",None)
        sex=req.POST.get("sex",None)
        email=req.POST.get("email",None)

        info={"username":username,"sex":sex,"email":email}
        info_list.append(info)

    return render(req, "../templates/userInfor.html", {"info_list":info_list})