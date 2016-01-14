# Create your views here.
import StringIO
import base64
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render
from invoices.forms import EFacturaForm
from invoices.models import EFactura
from invoices.parser import Parser


def handle_uploaded_file(f):
    text = ""
    for chunk in f.chunks():
        text += str(chunk)
    return text


def home(request):
    if request.user.is_authenticated():
        efacturas = EFactura.objects.filter(Owner=request.user)
        context = {
            'facturas': efacturas
        }
        return render(request, 'invoices/home.html', context)
    else:
        pass
    return render(request, 'invoices/home.html')


@login_required()
def upload_new_efactura(request):
    error_messages = []
    if request.method == 'POST':
        form = EFacturaForm(request.POST, request.FILES)
        if form.is_valid():
            text = handle_uploaded_file(request.FILES['file'])
            p = Parser()
            result = p.parseFacturaE(text)
            if not result:
                error_messages.append("La factura enviada no contiene el formato correcto")
                context = {
                    'errors': error_messages,
                    'form': form,
                }
            else:
                e_factura = p.efactura
                e_factura.Data = base64.encodestring(text)
                e_factura.Owner = request.user
                e_factura.save()
                context = {
                    'errors': error_messages,
                    'form': form,
                    'e_factura': e_factura
                }
    else:
        form = EFacturaForm()
        context = {
            'errors': error_messages,
            'form': form
        }

    return render(request, 'invoices/upload_efactura.html', context)


@login_required()
def download_efactura(request, id):
    error_messages = []
    try:
        if request.user.is_authenticated():
            efactura = EFactura.objects.get(id=id)
            if efactura.Owner == request.user:
                data = base64.decodestring(efactura.Data)
                response = HttpResponse(data, mimetype="text/xml")
                response['Content-Disposition'] = 'attachment; filename=factura.xml'
                return response
    except ObjectDoesNotExist:
        pass
    error_messages.append("Hay algun error con la factura aportada")
    context = {
        'errors': error_messages
    }
    return render(request, 'invoices/download_efactura.html', context)
