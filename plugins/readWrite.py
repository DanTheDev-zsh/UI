import csv
import datetime
import json

now = datetime.datetime.now()


def append_CSV(listed_price, discount_percentage, total_after_discount):
    file_path = "logs/record.csv"
    with open(file_path, "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(
            [
                listed_price,
                discount_percentage,
                total_after_discount,
                now.strftime("%x"),
            ]
        )
        print(
            "value appended to csv file: " + listed_price,
            discount_percentage,
            total_after_discount,
        )
    return


def append_JSON(
    eBay_ID, item_ID, listed_price, discount_percentage, total_after_discount
):
    pass  # TODO
