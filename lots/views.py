from django.shortcuts import render

from lots.models import InputLot, OutputLot
from products.models import Product


def my_formatdate(list_data):
    for data in list_data:
        data.created_at = data.created_at.strftime('%d/%m/%y às %H:%M:%S')

def include_value(datas, value, is_input):
    if is_input:
        data = {
            'type': 'Entrada',
            'quant': value.quantity,
            'created_at': value.created_at.strftime('%d/%m/%y às %H:%M:%S'),
            'product': value.product.name,
        }
        datas.append(data)
    else:
        data = {
            'type': 'Saida',
            'quant': value.quantity,
            'created_at': value.created_at.strftime('%d/%m/%y às %H:%M:%S'),
            'product': value.product.name,
        }
        datas.append(data)


def balance_mov(request):
    produts = Product.objects.all()
    balances = []
    for product in produts:
        quantity = 0
        for prod_input in product.inputlot_set.all():
            quantity = prod_input.quantity
        for prod_output in product.outputlote_set.all():
            quantity = prod_output.quantity
        balances.append({'name': product.name, 'quantity': quantity})
    return render(request, 'balance.html', {'balances': balances})
        


def list_mov(request):
    datas = []
    i = 0
    o = 0
    inputs = InputLot.objects.order_by('-created_at')
    outputs = OutputLot.objects.order_by('-created_at')
    quant_in = len(inputs)
    quant_out = len(outputs)
    for u in range(quant_out + quant_in):
        if o < quant_out and i < quant_in:
            if inputs[i].created_at > outputs[o].created_at:
                include_value(datas, inputs[i], True)
                i += 1
            else:
                include_value(datas, outputs[o], False)
                o += 1
        elif i < quant_in:
            include_value(datas, inputs[i], True)
            i += 1
        elif o < quant_out:
            include_value(datas, outputs[o], False)
            o += 1
    return render(request, 'list_mov.html', {'datas': datas})


def list_input(request):
    inputs = InputLot.objects.all()
    my_formatdate(inputs)
    return render(request, 'list_input.html', {'inputs': inputs})


def new_input(request):
    pass


def update_input(request):
    pass


def delete_input(request):
    pass


def list_output(request):
    outputs = OutputLot.objects.all()
    format(outputs)
    return render(request, 'list_output.html', {'outputs': outputs})


def new_output(request):
    pass


def update_output(request):
    pass


def delete_output(request):
    pass
