#
# * 図を作成する際に共通で使える関数をまとめる *
#

# ['00:00', '00:20', '00:40', '01:00', ...., '23:40']
def slots():
    return [str(hour).zfill(2) + ':' + minute for hour in range(0, 24) for minute in['00', '20', '40']]


# ['0:00', '', '', '1:00', '', '', '2:00', '', ...., '13:00', '', '']
def slots_axis_label():
    slots_label = []
    slots_hour = [[str(hour) + ":" + "00", "", ""] for hour in range(0, 24)]
    for h in slots_hour:
        slots_label.extend(h)
    return slots_label
