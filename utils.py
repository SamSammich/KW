from datetime import datetime
import requests


def get_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json(), "Info : Everything okeey!"
    return None, f"ERROR: {response.status_code}"


"""Checking Errors"""


def get_filtered_data(data, filtered_empty_from=False):
    data = [x for x in data if "state" in x and x["state"] == 'EXECUTED']
    if filtered_empty_from:
        data = [x for x in data if "from" in x]
    return data


"""Returning state == EXECUTED and filtering data without from"""


def get_last_data(data, count_last_values):

    data = sorted(data, key=lambda x: x["date"], reverse=True)
    return data[:count_last_values]


"""Returning last Values"""


def get_formatted_data(data):

    formatted_data = []
    for row in data:
        date = datetime.strptime(row["date"], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        description = row["description"]

        sender = row["from"].split()
        sender_bill = sender.pop(-1)
        sender_bill = f'{sender_bill[:4]} {sender_bill[4:6]}** ****{sender_bill[-4:]}'
        sender_info = "".join(sender)

        recipient = f"**{row['to'][-4:]}"
        amount = f'{row["operationAmount"]["amount"]} {row["operationAmount"]["currency"]["name"]}'
        formatted_data.append(f"""\
{date} {description} 
{sender_info} {sender_bill} --> :Счет {recipient}
{amount} """)
        return formatted_data



