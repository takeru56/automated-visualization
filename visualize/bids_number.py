import matplotlib.pyplot as plt
import os
import common

#
# * 入札回数の図を作成 *
#


def png_dir(yyyymm):
    return '../results/diagram/' + str(yyyymm)


def png_path(yyyymm):
    return png_dir(yyyymm) + '/bids' + str(yyyymm)[4:6] + '.png'


def count_bids_per_slot(df, slot):
    return df.query('formatted_slot.str.contains("{}")'.format(slot), engine='python')['history'].apply(lambda x: len(json.loads(x))).sum()


def all_bids_count_per_slot(df):
    count = []
    for slot in common.slots():
        count.append(count_bids_per_slot(df, slot))
    return count


def draw_hist(df, yyyymm):
    bids = all_bids_count_per_slot(df)

    _, ax = plt.subplots(figsize=(16, 10))
    plt.xticks(rotation=90, fontsize=15)
    plt.ylabel('Bids', fontsize=20)
    plt.yticks(fontsize=15)
    ax.grid(axis='y')
    ax.set_ylim(0, 15)
    plt.bar(common.slots(), bids, tick_label=common.slots_axis_label())

    os.makedirs(png_dir(yyyymm), exist_ok=True)
    plt.savefig(png_path(yyyymm))
