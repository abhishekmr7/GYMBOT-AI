from app.ai.extractor import extract_customer_info

conversation = """
Hi, I'm Rahul Sharma.

My phone number is 9876543210.

I want MMA coaching.
"""

result = extract_customer_info(conversation)

print(result)