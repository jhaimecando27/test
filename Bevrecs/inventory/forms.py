from django import forms

# Mga database
from .models import Stocks

# Mga constant
from .models import STOCK_CATEGORY


# Eto yung tricky part. May 3 form tayo na isa lng papasukan which is mahirap
# ata


class IngridientsForm(forms.ModelForm):
    category = forms.ChoiceField(
        choices=STOCK_CATEGORY,
        widget=forms.RadioSelect,
    )

    class Meta:
        model = Stocks  # Eto yung table na gagamitin
        fields = ["name", "category", "quantity", "price", "date_in", "expiration"]
