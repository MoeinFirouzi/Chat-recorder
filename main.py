import json
from datetime import *

with open("chat-data.json", 'r', encoding="UTF-8") as data_file:
    readable_data = json.load(data_file)

number_of_words_of_contact, number_of_words_of_you = 0, 0
number_of_messages_of_contact, number_of_messages_of_you = 0, 0

words_set = {}

for item in readable_data['messages']:
    if item['from'] == "contact's name":
        number_of_messages_of_contact += 1
        number_of_words_of_contact += str(item['text']).count(' ') + 1

    elif item['from'] == "M.Moein Firouzi":
        number_of_messages_of_you += 1
        number_of_words_of_you += str(item['text']).count(' ') + 1

print("contact", "messages :", number_of_messages_of_contact, "\twords :", number_of_words_of_contact)
print("You", "messages :", number_of_messages_of_you, "\twords :", number_of_words_of_you)


def convert_to_second(date, time, start):
    start_time = datetime(int(start[0][0]), int(start[0][1]), int(start[0][2]),
                          int(start[1][0]), int(start[1][1]), int(start[1][2]))
    timesince = datetime(int(date[0]), int(date[1]), int(date[2]), int(time[0]), int(time[1]),
                         int(time[2])) - start_time
    seconds = int(timesince.total_seconds())
    return seconds


def preparing_data(data):
    temp = str(data).split('T')
    date_data = temp[0].split('-')
    date_data[0] = date_data[0].lstrip('0')
    date_data[1] = date_data[1].lstrip('0')
    time_data = temp[1].split(':')
    return date_data, time_data


start = preparing_data(readable_data['messages'][0]["date"])
result = 0
temp_time = 0
time_line = []

for item in readable_data['messages']:
    item_data = preparing_data(item["date"])
    time_in_second = convert_to_second(item_data[0], item_data[1], start)
    time_line.append(time_in_second)

first_point = 0
for item in time_line:
    if item - first_point > 600:
        result += temp_time
        temp_time = 0
    else:
        temp_time += item - first_point
    first_point = item

result += temp_time
print("#" * 20)
seconds_in_day = 86400
seconds_in_hour = 3600
seconds_in_minute = 60

seconds = result

days = seconds // seconds_in_day
seconds = seconds - (days * seconds_in_day)

hours = seconds // seconds_in_hour
seconds = seconds - (hours * seconds_in_hour)

minutes = seconds // seconds_in_minute
seconds = seconds - (minutes * seconds_in_minute)

print("{0:.0f} days, {1:.0f} hours, {2:.0f} minutes, {3:.0f} seconds active in chat.".format(
    days, hours, minutes, seconds))
