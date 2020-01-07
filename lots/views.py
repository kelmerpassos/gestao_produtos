from django.shortcuts import render

from lots.models import InputLot, OutputLot


def include_value(list, value, is_input):
    if is_input:
        dado = {
            'type': 'entrada',
            'quant': value.quantity,
            'created_at': value.created_at,
            'product': value.product.name,
        }
        list.append(dado)
    else:
        dado = {
            'type': 'saida',
            'quant': value.quantity,
            'created_at': value.created_at,
            'product': value.product.name,
        }
        list.append(dado)


def list_lots(request):
    dados = []
    i = 0
    o = 0
    inputs = InputLot.objects.order_by('-created_at')
    outputs = OutputLot.objects.order_by('-created_at')
    quant_in = len(inputs)
    quant_out = len(outputs)
    for u in range(quant_out + quant_in):
        if o < quant_out and i < quant_in:
            if inputs[i].created_at > outputs[o].created_at:
                include_value(dados, inputs[i], True)
                i += 1
            else:
                include_value(dados, outputs[o], False)
                o += 1
        elif i < quant_in:
            include_value(dados, inputs[i], True)
            i += 1
        elif o < quant_out:
            include_value(dados, outputs[o], False)
            o += 1
    return render(request, 'list_lots.html', {'data': dados})


def new_lots(request):
    pass


def update_lots(request):
    pass


def delete_lots(request):
    pass
