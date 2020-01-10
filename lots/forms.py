from lots.models import InputLot, OutputLot
from django.forms import ModelForm


class InputLotForm(ModelForm):
    """Form definition for InputLot."""

    class Meta:
        """Meta definition for InputLotform."""

        model = InputLot
        fields = ('number_input','quantity', 'product')

class OutputLotForm(ModelForm):
    """Form definition for OutputLot."""

    class Meta:
        """Meta definition for OutputLotform."""

        model = OutputLot
        fields = ('number_output', 'quantity', 'product')  
