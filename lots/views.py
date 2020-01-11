from django.shortcuts import get_object_or_404, redirect, render

from lots.forms import InputLotForm, OutputLotForm
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
        for prod_output in product.outputlot_set.all():
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
    inputs = InputLot.objects.order_by('-created_at')
    my_formatdate(inputs)
    return render(request, 'list_input.html', {'inputs': inputs})

def new_input(request):
    form = InputLotForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('list_input')
    return render(
        request, 
        'generic_form.html',{
            'form': form,
            'title': 'Cadastrar Entrada',
            'roth': 'http://localhost:8000/lots/input/list/'
        }
    )

def update_input(request, id):
    input_lot = get_object_or_404(InputLot, pk=id)
    form = InputLotForm(request.POST or None, instance=input_lot)
    if form.is_valid():
        form.save()
        return redirect('list_input')
    return render(
        request, 
        'generic_form.html',{
            'form': form,
            'title': f'Editar Saída {str(input_lot.number_input)}',
            'roth': 'http://localhost:8000/lots/input/list/'
        }
    )


def delete_input(request, id):
    input_lot = get_object_or_404(InputLot, pk=id)
    input_lot.delete()
    return redirect('list_input')


def list_output(request):
    outputs = OutputLot.objects.order_by('-created_at')
    format(outputs)
    return render(request, 'list_output.html', {'outputs': outputs})


def new_output(request):
    form = OutputLotForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect ('list_output')
    return render(
        request,
        'generic_form.html',{
            'form': form,
            'title': 'Cadastrar Saída',
            'roth': 'http://localhost:8000/lots/output/list/'
        }
    )


def update_output(request, id):
    output_lot = get_object_or_404(OutputLot, pk=id)
    form = OutputLotForm(request.POST or None, instance=output_lot)
    if form.is_valid():
        form.save()
        return redirect ('list_output')
    return render(
        request,
        'generic_form.html',{
            'form': form,
            'title': f'Editar Saída {str(output_lot.number_output)}',
            'roth': 'http://localhost:8000/lots/output/list/'
        }
    )


def delete_output(request, id):
    output_lot = get_object_or_404(OutputLot, pk=id)
    output_lot.delete()
    return redirect('list_output')
