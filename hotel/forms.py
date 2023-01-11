from django import forms


class AvailabiltyForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NO-AC'),
        ('LUX', 'LUXURY'),
        ('KIN', 'KING'),
        ('QEE', 'QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ])
    check_out = forms.DateTimeField(
        required=True, input_formats=["%Y-%m-%dT%H:%M", ])
