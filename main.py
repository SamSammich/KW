from utils import get_data, get_filtered_data, get_formatted_data, get_last_data


def main():
    OPERATION_URL = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678630161075&signature=zulZ1Ikga0shV1j3HZjhS7FQyxa5uRvXTQhCkk8tF2U&downloadName=operations.json"
    COUNT_LAST_VALUES = 5
    FILTERED_EMPTY_FROM = True

    data, info = get_data(OPERATION_URL)
    if not data:
        exit(info)
    print(info, end="\n\n")

    data = get_filtered_data(data, FILTERED_EMPTY_FROM)
    data = get_last_data(data, COUNT_LAST_VALUES)
    data = get_formatted_data(data)
    for row in data:
        print(row)

if __name__ == "__main__":
    main()
