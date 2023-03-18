from django.core.exceptions import ValidationError

from re import fullmatch


def validate_isbn(value: str) -> None:
    pattern = r'^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$'
    value = value.strip()

    if not fullmatch(pattern, value):
        raise ValidationError(f'"{value}" is not a correct isbn.')


def validate_topic(value: str) -> None:
    if not value.islower():
        raise ValidationError(f'"{value}" topic should be in a lowercase.')


# def validate_topic_count(value: object) -> None:
#     topics_amount = value.count()
#
#     if topics_amount > 20:
#         raise ValidationError(f'The maximum amount of topics is 20 but you have {topics_amount}.')
