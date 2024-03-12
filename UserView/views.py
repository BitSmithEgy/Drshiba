from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
from users.models import CustomUser
from .models import Quiz
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def index(request):
    courses = models.Course.objects.all()
    return render(request, 'UserView/index.html', {'courses': courses})


@login_required(login_url='login')
def d1(request):
    videos = {
        'إنشاء مشروع جديد': 'https://drive.google.com/file/d/1MItD6X2r9lpoFRfomfgH0XA7IwwV-nO2/preview',
        'تعديل الإعدادات السابقة': 'https://drive.google.com/file/d/1s0dV_AhJ_cgZF8WV4Fl1WE6W-FeJ9852/preview',
        'حفظ الإعدادات المسبقة': 'https://drive.google.com/file/d/1CFg8WufnEnhr0o3fzREslcYjDiQq_pqL/preview'
    }

    return render(request, 'UserView/video.html', {'videos': videos, 'quiz':'q1'})


@login_required(login_url='login')
def d11(request):
    User = get_user_model()
    user = User.objects.get(email=request.user.email)

    if user.d1 == True:
        videos = {
            'إنشاء مشروع جديد': 'https://drive.google.com/file/d/1MItD6X2r9lpoFRfomfgH0XA7IwwV-nO2/preview',
            'تعديل الإعدادات السابقة': 'https://drive.google.com/file/d/1s0dV_AhJ_cgZF8WV4Fl1WE6W-FeJ9852/preview',
            'حفظ الإعدادات المسبقة': 'https://drive.google.com/file/d/1CFg8WufnEnhr0o3fzREslcYjDiQq_pqL/preview',
            'إستخدام الإصدارات الأقدم': 'https://drive.google.com/file/d/11KC14CJ5HeX_k4g3VrPyT4NTo4V112BA/preview'
        }

        return render(request, 'UserView/video.html', {'videos': videos, 'quiz':'q11'})
    
    else:
        return HttpResponse('You are not allowed here')


@login_required(login_url='login')
def d12(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview'
    }

    return render(request, 'UserView/video.html', {'videos': videos, 'quiz':'q12'})


@login_required(login_url='login')
def d13(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'psd': 'https://drive.google.com/file/d/19ndOq4_AVriDVG2aKbG7rkluoDPw5mmX/preview',
        'jpeg': 'https://drive.google.com/file/d/1rmXnl5Ch1JTOIkAQX20iLVCEgwD9lC0P/preview'

    }

    return render(request, 'UserView/video.html', {'videos': videos, 'quiz':'q13'})


@login_required(login_url='login')
def d111(request):
    videos = {
        'إنشاء مشروع جديد': 'https://drive.google.com/file/d/1MItD6X2r9lpoFRfomfgH0XA7IwwV-nO2/preview',
        'تعديل الإعدادات السابقة': 'https://drive.google.com/file/d/1s0dV_AhJ_cgZF8WV4Fl1WE6W-FeJ9852/preview',
        'حفظ الإعدادات المسبقة': 'https://drive.google.com/file/d/1CFg8WufnEnhr0o3fzREslcYjDiQq_pqL/preview',
        'إستخدام الإصدارات الأقدم': 'https://drive.google.com/file/d/11KC14CJ5HeX_k4g3VrPyT4NTo4V112BA/preview'
    }

    return render(request, 'UserView/video.html', {'videos': videos, 'quiz':'q11'})


@login_required(login_url='login')
def d112(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview'
    }

    return render(request, 'UserView/video.html', {'videos': videos, 'quiz':'q112'})


@login_required(login_url='login')
def d113(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q113'})


@login_required(login_url='login')
def d121(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview',
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q121'})


@login_required(login_url='login')
def d122(request):
    videos = {
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q122'})


@login_required(login_url='login')
def d123(request):
    videos = {
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'psd': 'https://drive.google.com/file/d/19ndOq4_AVriDVG2aKbG7rkluoDPw5mmX/preview',
        'jpeg': 'https://drive.google.com/file/d/1rmXnl5Ch1JTOIkAQX20iLVCEgwD9lC0P/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q123'})


@login_required(login_url='login')
def d131(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'psd': 'https://drive.google.com/file/d/19ndOq4_AVriDVG2aKbG7rkluoDPw5mmX/preview',
        'jpeg': 'https://drive.google.com/file/d/1rmXnl5Ch1JTOIkAQX20iLVCEgwD9lC0P/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q131'})


@login_required(login_url='login')
def d132(request):
    videos = {
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'png':'https://drive.google.com/file/d/1ERlhaSdGLmOZmBQLK3_ZZkUYr4aVOBba/preview',
        'pdf':'https://drive.google.com/file/d/1LSmA31c6kuESqQELajyKgqJba2ba-8YD/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q132'})


@login_required(login_url='login')
def d133(request):
    videos = {
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'png':'https://drive.google.com/file/d/1ERlhaSdGLmOZmBQLK3_ZZkUYr4aVOBba/preview',
        'pdf':'https://drive.google.com/file/d/1LSmA31c6kuESqQELajyKgqJba2ba-8YD/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'tiff':'https://drive.google.com/file/d/1GbPR0Mi3QhDh_dIFrcDYNnQ7FWyBMncQ/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q133'})


@login_required(login_url='login')
def d1111(request):
    videos = {
        'نافذة الأدوات': 'https://drive.google.com/file/d/1iXOKIOmeoiYYy0bKLq02sxDKj3gaO_2o/preview',
        'تخصيص شريط الأدوات': 'https://drive.google.com/file/d/1xY_LGDRMxzvb4C_5b1_4P6jMOQID4Edj/preview',
        'شريط الخيارات': 'https://drive.google.com/file/d/1ZW_35CbfdeJgsnAzPyCxJQKfGwtz7ySv/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview',
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q1111'})


@login_required(login_url='login')
def d1112(request):
    videos = {
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'psd': 'https://drive.google.com/file/d/19ndOq4_AVriDVG2aKbG7rkluoDPw5mmX/preview',
        'jpeg': 'https://drive.google.com/file/d/1rmXnl5Ch1JTOIkAQX20iLVCEgwD9lC0P/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q1112'})


@login_required(login_url='login')
def d1113(request):
    videos = {
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'psd': 'https://drive.google.com/file/d/19ndOq4_AVriDVG2aKbG7rkluoDPw5mmX/preview',
        'jpeg': 'https://drive.google.com/file/d/1rmXnl5Ch1JTOIkAQX20iLVCEgwD9lC0P/preview',
        'png':'https://drive.google.com/file/d/1ERlhaSdGLmOZmBQLK3_ZZkUYr4aVOBba/preview',
        'pdf':'https://drive.google.com/file/d/1LSmA31c6kuESqQELajyKgqJba2ba-8YD/preview',
        'tiff':'https://drive.google.com/file/d/1GbPR0Mi3QhDh_dIFrcDYNnQ7FWyBMncQ/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q1113'})


@login_required(login_url='login')
def d1221(request):
    videos = {
        'تفضيلات الارت بورد':'https://drive.google.com/file/d/1rVxqSYeQ2t78CYb1FKFeOxWeYR3pav8K/preview',
        'الشبكة والأدلة':'https://drive.google.com/file/d/1dzG-dVwTczasKJ4DHVBk6Ya2Xc1p-18Y/preview',
        'إدراج الملفات': 'https://drive.google.com/file/d/1BelnmxGZF6l934IOwEVOr2JiKz738GeD/preview',
        'الكتابة': 'https://drive.google.com/file/d/1xGm4_-A1GzdvGulVcToekt0wtHYVRPUx/preview',
        'الأشكال الهندسية':'https://drive.google.com/file/d/1ilJcnXNtk9nEou2zaBg7HUAWUzvaVm1w/preview',
        'معرض أدوات التنقل':'https://drive.google.com/file/d/1nAc2gyGrr4Z5a2iFWhxkvOEunoyi_rHC/preview',
        'png':'https://drive.google.com/file/d/1ERlhaSdGLmOZmBQLK3_ZZkUYr4aVOBba/preview',
        'pdf':'https://drive.google.com/file/d/1LSmA31c6kuESqQELajyKgqJba2ba-8YD/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q1221'})


@login_required(login_url='login')
def d1222(request):
    videos = {
        'png':'https://drive.google.com/file/d/1ERlhaSdGLmOZmBQLK3_ZZkUYr4aVOBba/preview',
        'pdf':'https://drive.google.com/file/d/1LSmA31c6kuESqQELajyKgqJba2ba-8YD/preview',
        'tiff':'https://drive.google.com/file/d/1GbPR0Mi3QhDh_dIFrcDYNnQ7FWyBMncQ/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q1222'})



#
#
#
#
#
#
#
#
#
# Here we finished first  level videos and start second level videos.........................................................
#
#
#
#
#
#
#
#
#



def d2(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2'})

def d21(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview',
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q21'})

def d22(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22'})

def d23(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q23'})

def d211(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview',
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q21'})

def d212(request):
    videos = {
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q212'})

def d213(request):
    videos = {
                    'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
                    'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
                    'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
                'Layer mask':'https://drive.google.com/file/d/1uOpiziuXuybHWxJLE8yTTgznJAZ_7gQL/preview',
                'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview'
    }
    
    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q213'})

def d221(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q221'})

def d222(request):
    videos = {
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
        'Layer mask':'https://drive.google.com/file/d/1uOpiziuXuybHWxJLE8yTTgznJAZ_7gQL/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q222'})

def d223(request):
    videos = {
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
        'Layer mask':'https://drive.google.com/file/d/1uOpiziuXuybHWxJLE8yTTgznJAZ_7gQL/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q223'})

def d231(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q231'})

def d232(request):
    videos = {
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'Layer mask':'https://drive.google.com/file/d/1uOpiziuXuybHWxJLE8yTTgznJAZ_7gQL/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q232'})

def d233(request):
    videos = {
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'Layer mask':'https://drive.google.com/file/d/1uOpiziuXuybHWxJLE8yTTgznJAZ_7gQL/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
        'Select Subject':'https://drive.google.com/file/d/1DHA_yF1BAMyHHR7Y9JGtQHBkMNJENpMM/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q232'})


def d2111(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview',
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2111'})

def d2112(request):
    videos = {
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2112'})

def d2113(request):
    videos = {
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'Select Subject':'https://drive.google.com/file/d/1DHA_yF1BAMyHHR7Y9JGtQHBkMNJENpMM/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2113'})

def d2211(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2211'})

def d2212(request):
    videos = {
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2212'})

def d2213(request):
    videos = {
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'Select Subject':'https://drive.google.com/file/d/1DHA_yF1BAMyHHR7Y9JGtQHBkMNJENpMM/preview',
        'ماجيك ويند تول':'https://drive.google.com/file/d/1iVX01Tq3xHPcaDNa1U7zCyAa4pYn4Uzq/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2213'})

def d2311(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'ماجيك ويند تول':'https://drive.google.com/file/d/1iVX01Tq3xHPcaDNa1U7zCyAa4pYn4Uzq/preview'

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2311'})

def d2312(request):
    videos = {
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'ماجيك ويند تول':'https://drive.google.com/file/d/1iVX01Tq3xHPcaDNa1U7zCyAa4pYn4Uzq/preview',
        'B/C':'https://drive.google.com/file/d/1Hq3yRH7ugUS8t9d2zX6RsXNS4K4yM7eg/preview',
        'Hue/Sat':'https://drive.google.com/file/d/1uo8KsPX8dTIGKRW0KPlNLBkYpF-33ChX/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2312'})


def d2313(request):
    videos = {
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'ماجيك ويند تول':'https://drive.google.com/file/d/1iVX01Tq3xHPcaDNa1U7zCyAa4pYn4Uzq/preview',
        'B/C':'https://drive.google.com/file/d/1Hq3yRH7ugUS8t9d2zX6RsXNS4K4yM7eg/preview',
        'Hue/Sat':'https://drive.google.com/file/d/1uo8KsPX8dTIGKRW0KPlNLBkYpF-33ChX/preview',
        'Levels':'https://drive.google.com/file/d/1nF8QeoqF0-HbwhPycUEBqBq3s03tJ13L/preview',
        'Gradiant':'https://drive.google.com/file/d/1WFfzyD0EQsPc7rOrMhqecGecwLRfDV5o/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2313'})

def d23111(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'ماجيك ويند تول':'https://drive.google.com/file/d/1iVX01Tq3xHPcaDNa1U7zCyAa4pYn4Uzq/preview'

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2311'})

def d23112(request):
    videos = {
        'vibrance':'https://drive.google.com/file/d/1tvSy6W2CsEMuYKseuWONgN0DJhavy2sv/preview',
        'color balance':'https://drive.google.com/file/d/1t2ludNapXXi5SxN86Ua1_IgooSnQOQcQ/preview'

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q23112'})

def d23113(request):
    videos = {
        'vibrance':'https://drive.google.com/file/d/1tvSy6W2CsEMuYKseuWONgN0DJhavy2sv/preview',
        'color balance':'https://drive.google.com/file/d/1t2ludNapXXi5SxN86Ua1_IgooSnQOQcQ/preview',
        'black and white':'https://drive.google.com/file/d/1BaNV_kY_0-Pu-XLtuSVbP3CSuOdpdMKZ/preview',
        '':''
        
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q23113'})

def d22111(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22111'})

def d22112(request):
    videos = {
        'B/C':'https://drive.google.com/file/d/1Hq3yRH7ugUS8t9d2zX6RsXNS4K4yM7eg/preview',
        'Hue/Sat':'https://drive.google.com/file/d/1uo8KsPX8dTIGKRW0KPlNLBkYpF-33ChX/preview',
        'Levels':'https://drive.google.com/file/d/1nF8QeoqF0-HbwhPycUEBqBq3s03tJ13L/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22112'})

def d22113(request):
    videos = {
        'B/C':'https://drive.google.com/file/d/1Hq3yRH7ugUS8t9d2zX6RsXNS4K4yM7eg/preview',
        'Hue/Sat':'https://drive.google.com/file/d/1uo8KsPX8dTIGKRW0KPlNLBkYpF-33ChX/preview',
        'Levels':'https://drive.google.com/file/d/1nF8QeoqF0-HbwhPycUEBqBq3s03tJ13L/preview',
        'vibrance':'https://drive.google.com/file/d/1tvSy6W2CsEMuYKseuWONgN0DJhavy2sv/preview',
        'Gradiant':'https://drive.google.com/file/d/1WFfzyD0EQsPc7rOrMhqecGecwLRfDV5o/preview'

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22113'})

def d221111(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22111'})

def d221112(request):
    videos = {
        'color balance':'https://drive.google.com/file/d/1t2ludNapXXi5SxN86Ua1_IgooSnQOQcQ/preview',
        'black and white':'https://drive.google.com/file/d/1BaNV_kY_0-Pu-XLtuSVbP3CSuOdpdMKZ/preview',
        
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q221112'})

def d21111(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview',
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2111'})

def d21112(request):
    videos = {
        'B/C':'https://drive.google.com/file/d/1Hq3yRH7ugUS8t9d2zX6RsXNS4K4yM7eg/preview',
        'Hue/Sat':'https://drive.google.com/file/d/1uo8KsPX8dTIGKRW0KPlNLBkYpF-33ChX/preview',
        'Levels':'https://drive.google.com/file/d/1nF8QeoqF0-HbwhPycUEBqBq3s03tJ13L/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q21112'})

def d21113(request):
    videos = {
        'B/C':'https://drive.google.com/file/d/1Hq3yRH7ugUS8t9d2zX6RsXNS4K4yM7eg/preview',
        'Hue/Sat':'https://drive.google.com/file/d/1uo8KsPX8dTIGKRW0KPlNLBkYpF-33ChX/preview',
        'Levels':'https://drive.google.com/file/d/1nF8QeoqF0-HbwhPycUEBqBq3s03tJ13L/preview',
        'vibrance':'https://drive.google.com/file/d/1tvSy6W2CsEMuYKseuWONgN0DJhavy2sv/preview',

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q21113'})

def d211111(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview',
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2111'})

def d211112(request):
    videos = {
        'color balance':'https://drive.google.com/file/d/1t2ludNapXXi5SxN86Ua1_IgooSnQOQcQ/preview',
        'black and white':'https://drive.google.com/file/d/1BaNV_kY_0-Pu-XLtuSVbP3CSuOdpdMKZ/preview',
        'Gradiant':'https://drive.google.com/file/d/1WFfzyD0EQsPc7rOrMhqecGecwLRfDV5o/preview'

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'d211112'})

def d211113(request):
    videos = {
        'color balance':'https://drive.google.com/file/d/1t2ludNapXXi5SxN86Ua1_IgooSnQOQcQ/preview',
        'black and white':'https://drive.google.com/file/d/1BaNV_kY_0-Pu-XLtuSVbP3CSuOdpdMKZ/preview',
        'Gradiant':'https://drive.google.com/file/d/1WFfzyD0EQsPc7rOrMhqecGecwLRfDV5o/preview',
        'النقطة المرجعية':'https://drive.google.com/file/d/15mUOy44_KflLnR6tXSm2Vh3QSH67h_2n/preview',
        'التدوير والإستدارة':'https://drive.google.com/file/d/1BaadDdn5DXBxcJ9d9tYiRpm58SM7vkar/preview'
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'d211113'})

def d2111111(request):
    videos = {
        'طبقات الفوتوشوب':'https://drive.google.com/file/d/18e57E5OgjfZkthkHvn51-XU_y5eNn2JY/preview',
        'طبقات الضبط':'https://drive.google.com/file/d/1Hj8J-s4Sh13BZm1UtoRBbxx2Z5O5TAhi/preview',
        'تحويل الطبقة الخلفية الي طبقة':'https://drive.google.com/file/d/18umK4v_wOffN3dzgGXanN_udW0yAfNh_/preview',
        'إنشاء وإدارة الطبقات':'https://drive.google.com/file/d/1TUa1o-j6usstozkGdNo_d7Hx1EHXwLAi/preview',
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'التحديد المربع':'https://drive.google.com/file/d/1HRXv1lFD98fsL13DMZwtyT9tzAAzok3Q/preview',
        'التحديد الدائري':'https://drive.google.com/file/d/1EcR96vT0Gky0Lqj0QUENW_eR-20AVV_f/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2111'})

def d2111112(request):
    videos = {
            'Crop tool':'https://drive.google.com/file/d/1BI_BrEbF4Ute_hITfX0gVzMiJpv3uFw4/preview',
            'Transform free':'https://drive.google.com/file/d/1LDsxXu-chv5PxEiDIQUrLVfie4eAW_t0/preview'
        }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'d2111112'})

def d2111113(request):
    videos = {
            'Crop tool':'https://drive.google.com/file/d/1BI_BrEbF4Ute_hITfX0gVzMiJpv3uFw4/preview',
            'Transform free':'https://drive.google.com/file/d/1LDsxXu-chv5PxEiDIQUrLVfie4eAW_t0/preview',
            'Presptive':'https://drive.google.com/file/d/1WgDCMvWcrCuCz7orOPovHVhz561pj7KV/preview',
            'Puppet':'https://drive.google.com/file/d/1wPxMFblNGF1jodmSsJTVjwXSb_TGo5xW/preview',
            'Warp':'https://drive.google.com/file/d/1GDcWg5ILo_e-YKzSRfIXWIjI614bWfsA/preview'
        }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'d2111113'})

def d2211111(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22111'})

def d2211112(request):
    videos = {
            'Puppet':'https://drive.google.com/file/d/1wPxMFblNGF1jodmSsJTVjwXSb_TGo5xW/preview',
            'Warp':'https://drive.google.com/file/d/1GDcWg5ILo_e-YKzSRfIXWIjI614bWfsA/preview',
            'النقطة المرجعية':'https://drive.google.com/file/d/15mUOy44_KflLnR6tXSm2Vh3QSH67h_2n/preview',
            'التدوير والإستدارة':'https://drive.google.com/file/d/1BaadDdn5DXBxcJ9d9tYiRpm58SM7vkar/preview'
        }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2211112'})

def d2211113(request):
    videos = {
            'Puppet':'https://drive.google.com/file/d/1wPxMFblNGF1jodmSsJTVjwXSb_TGo5xW/preview',
            'Warp':'https://drive.google.com/file/d/1GDcWg5ILo_e-YKzSRfIXWIjI614bWfsA/preview',
            'النقطة المرجعية':'https://drive.google.com/file/d/15mUOy44_KflLnR6tXSm2Vh3QSH67h_2n/preview',
            'التدوير والإستدارة':'https://drive.google.com/file/d/1BaadDdn5DXBxcJ9d9tYiRpm58SM7vkar/preview',
            'Presptive':'https://drive.google.com/file/d/1WgDCMvWcrCuCz7orOPovHVhz561pj7KV/preview',

        }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2211113'})

def d22111111(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'move تحديد الطبقة بإستخدام ':'https://drive.google.com/file/d/1A5id4GO67Etfg5OkBW8ngemenoRUGnVV/preview',
        'التحديد المضلع':'https://drive.google.com/file/d/1FzLSnCG89rhxOF0dICHu7z30f9w7sB_5/preview',
        'التحديد المغناطيسي':'https://drive.google.com/file/d/1DIU_t2DE2463UJa9sNoOlCh_E2jfpdec/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22111'})

def d22111112(request):
    videos = {
        'Puppet':'https://drive.google.com/file/d/1wPxMFblNGF1jodmSsJTVjwXSb_TGo5xW/preview',
        'Warp':'https://drive.google.com/file/d/1GDcWg5ILo_e-YKzSRfIXWIjI614bWfsA/preview',
    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q22111112'})

def d231111(request):
    videos = {
        'إظهار وإخفاء الطبقات':'https://drive.google.com/file/d/1FkwolSZn3h2L_7YESqp5YXcwAIbEfDSZ/preview',
        'نسخ الطبقات':'https://drive.google.com/file/d/1cLOwzYa9sscffptHGhMBO0WcpXplLKPt/preview',
        'تجميع وربط الطبقة':'https://drive.google.com/file/d/1NpBoJ_-trhtAzgCeV48Sa6otOGFQX2mo/preview',
        'عتامة الطبقة':'https://drive.google.com/file/d/18womQs5dJyyqz81ixIC1jWR_l-haSKyt/preview',
        'تحديد صيغة مزج الطبقة':'https://drive.google.com/file/d/1oK0MfkEYxJPL-fM00tN7j-0oGICzJaw2/preview',
        'تحديد الطبقة':'https://drive.google.com/file/d/1-xyg9zR72PsZFh1Bjn1Dc9qAVFf-ilxk/preview',
        'كويك سليكشن سول':'https://drive.google.com/file/d/1kcY2NEOU2f-_FZ9Pyx_AJSBHEBwt4S7R/preview',
        'ماجيك ويند تول':'https://drive.google.com/file/d/1iVX01Tq3xHPcaDNa1U7zCyAa4pYn4Uzq/preview'

    }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q2311'})

def d231112(request):
    videos = {
            'Transform free':'https://drive.google.com/file/d/1LDsxXu-chv5PxEiDIQUrLVfie4eAW_t0/preview',
            'Presptive':'https://drive.google.com/file/d/1WgDCMvWcrCuCz7orOPovHVhz561pj7KV/preview',
            'Warp':'https://drive.google.com/file/d/1GDcWg5ILo_e-YKzSRfIXWIjI614bWfsA/preview'
        }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q231112'})

def d231113(request):
    videos = {
            'Transform free':'https://drive.google.com/file/d/1LDsxXu-chv5PxEiDIQUrLVfie4eAW_t0/preview',
            'Presptive':'https://drive.google.com/file/d/1WgDCMvWcrCuCz7orOPovHVhz561pj7KV/preview',
            'Puppet':'https://drive.google.com/file/d/1wPxMFblNGF1jodmSsJTVjwXSb_TGo5xW/preview',
            'Warp':'https://drive.google.com/file/d/1GDcWg5ILo_e-YKzSRfIXWIjI614bWfsA/preview'
        }

    return render(request, 'UserView/video.html', {'videos':videos, 'quiz':'q231113'})













#
#
#
#
#
#
#
#
#
# Here we finished second  level videos and start third level videos.........................................................
#
#
#
#
#
#
#
#
#











































#
#
#
#
#
#
#
#
#
# Here we finished the videos section and we will start the quizes section.......................................
#
#
#
#
#
#
#
#
#










@login_required(login_url='login')
def q1(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q1')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d11')
        elif 50 < percentage_score < 75:
            User = get_user_model()
            user = User.objects.get(email=request.user.email)
            user.d1 = True
            user.save()
            return redirect('d12')
        else:
            User = get_user_model()
            user = User.objects.get(email=request.user.email)
            user.d1 = True
            user.save()
            return redirect('d13')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q1')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q1'})
    

@login_required(login_url='login')
def q11(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q11')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d11')
        elif 50 < percentage_score < 75:
            return redirect('d112')
        else:
            return redirect('d113')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q11')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q11'})


@login_required(login_url='login')
def q112(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q112')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1111')
        elif 50 < percentage_score < 75:
            return redirect('d1112')
        else:
            return redirect('d1113')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q112')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q112'})
    

@login_required(login_url='login')
def q113(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q113')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1111')
        elif 50 < percentage_score < 75:
            return redirect('d1112')
        else:
            return redirect('d1113')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q113')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q113'})
    

@login_required(login_url='login')
def q1111(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q1111')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1111')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q1111')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q1111'})
    

@login_required(login_url='login')
def q1112(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q1112')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1112')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q1112')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q1112'})
    

@login_required(login_url='login')
def q1113(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q1113')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1113')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q1113')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q1113'})
    
    

@login_required(login_url='login')   
def q12(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q12')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d121')
        elif 50 < percentage_score < 75:
            return redirect('d122')
        else:
            return redirect('d123')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q12')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q12'})
    

@login_required(login_url='login')  
def q121(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q121')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1221')
        else:
            return redirect('d1222')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q121')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q121'})


@login_required(login_url='login')   
def q122(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q122')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1221')
        else:
            return redirect('d1222')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q122')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q122'})
    

@login_required(login_url='login')   
def q123(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q123')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1221')
        else:
            return redirect('d1222')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q123')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q123'})
    

@login_required(login_url='login')   
def q1221(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q1221')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1221')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q1221')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q1221'})
    
    
@login_required(login_url='login')
def q1222(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q1222')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d1222')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q1222')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q1222'})
    
    
@login_required(login_url='login')
def q13(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q13')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d131')
        elif 50 < percentage_score <= 75:
            return redirect('d132')
        else:
            return redirect('d133')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q13')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q13'})


@login_required(login_url='login')
def q131(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q131')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d131')
        elif 50 < percentage_score <= 75:
            return redirect('d2')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q131')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q131'})
    
@login_required(login_url='login')   
def q132(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q132')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d132')
        elif 50 < percentage_score <= 75:
            return redirect('d2')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q132')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q132'})
    
@login_required(login_url='login')    
def q133(request):
    if request.method == 'POST':
        # Process the form data
        score = 0

        # Fetch correct answers from the database
        quiz = Quiz.objects.get(name='q133')
        correct_answers = [question.correct_answer_q for question in quiz.questions.all()]

        # Check answers
        for i in range(1, len(correct_answers) + 1):
            question_answer = request.POST.get(f'question{i}')
            if question_answer and question_answer == correct_answers[i - 1]:
                score += 1

        # Calculate percentage score
        total_questions = len(correct_answers)
        percentage_score = (score / total_questions) * 100
        if percentage_score <= 50:
            return redirect('d133')
        elif 50 < percentage_score <= 75:
            return redirect('d2')
        else:
            return redirect('d2')
    else:
        # Fetch questions and options from the database
        quiz = Quiz.objects.get(name='q133')
        questions = {}
        for idx, question in enumerate(quiz.questions.all(), start=1):
            options = [
                question.q_option1,
                question.q_option2,
                question.q_option3,
                question.q_option4
            ]
            questions[idx] = {'question': question.q, 'options': options}

        return render(request, 'UserView/quiz.html', {'questions': questions, 'quiz': 'q133'})
    
    
    
    
#
#
#
#
#
#
#
#
#
# User auth system.....................................................................
#
#
#
#
#
#
#
#
#

def login_user(request):
    page = 'login'
    if request.method == 'POST':
        email = request.POST['username']
        password = request.POST['password']
        User = get_user_model()
        try:
            user = User.objects.get(email=email)
            authenticated_user = authenticate(request, username=email, password=password)
            if authenticated_user is not None:
                login(request, authenticated_user)
                return redirect('home')
            else:
                messages.error(request, "Incorrect password")
        except User.DoesNotExist:
            messages.error(request, "User does not exist")
    
    return render(request, 'UserView/login-register.html', {'page': page,  'messages': messages.get_messages(request)})

def logoutUser(request):
    logout(request)
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = form.cleaned_data['username']  # Add this line to get the username
            phone = form.cleaned_data['phone_number']
            # Use the custom user model manager to create the user
            User = get_user_model()  # Get the custom user model
            user = User.objects.create_user(username=username, phone_number=phone, email=email, password=password)  # Pass the username
            
            # Authenticate and login the user
            authenticated_user = authenticate(request, username=email, password=password)  # Pass the username
            print(authenticated_user)
            if authenticated_user:
                login(request, authenticated_user)
                return redirect('home')  # Redirect to the 'home' URL
    else:
        form = NewUserForm()
        print(form)

    return render(request, 'UserView/login-register.html', {'form': form})