from django.shortcuts import render, redirect, get_object_or_404
from .models import Certificate
from .forms import CertificateForm


def home(request):
    return render(request, 'certificates/home.html')


def certificate_list(request):

    search = request.GET.get('search')

    if search:
        certificates = Certificate.objects.filter(
            student_name__icontains=search
        )
    else:
        certificates = Certificate.objects.all()

    return render(
        request,
        'certificates/certificate_list.html',
        {
            'certificates': certificates
        }
    )



def add_certificate(request):

    if request.method == 'POST':

        form = CertificateForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('certificate_list')

    else:
        form = CertificateForm()

    return render(
        request,
        'certificates/add_certificate.html',
        {'form': form}
    )


def edit_certificate(request, id):

    certificate = get_object_or_404(
        Certificate,
        id=id
    )

    if request.method == 'POST':

        form = CertificateForm(
            request.POST,
            instance=certificate
        )

        if form.is_valid():
            form.save()
            return redirect('certificate_list')

    else:

        form = CertificateForm(
            instance=certificate
        )

    return render(
        request,
        'certificates/edit_certificate.html',
        {'form': form}
    )


def delete_certificate(request, id):

    certificate = get_object_or_404(
        Certificate,
        id=id
    )

    if request.method == 'POST':
        certificate.delete()
        return redirect('certificate_list')

    return render(
        request,
        'certificates/delete_certificate.html',
        {'certificate': certificate}
    )


def certificate_view(request, id):

    certificate = get_object_or_404(
        Certificate,
        id=id
    )

    return render(
        request,
        'certificates/certificate_view.html',
        {'certificate': certificate}
    )

