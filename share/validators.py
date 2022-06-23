from django.core.exceptions import ValidationError

def file_size(value):
    filesize=value.size
    if filesize>41943040:
        raise ValidationError("maximum size is 5 mb")