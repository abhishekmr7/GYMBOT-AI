import re


def validate_lead(data: dict):

    if not data.get("customer_name"):
        return False

    if not data.get("phone"):
        return False

    if not data.get("interested_in"):
        return False

    phone = data["phone"].strip()

    if not re.fullmatch(r"\d{10}", phone):
        return False

    return True