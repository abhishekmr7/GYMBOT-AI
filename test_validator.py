from app.ai.validator import validate_lead

lead = {
    "customer_name": "",
    "phone": "123",
    "interested_in": ""
}

print(validate_lead(lead))