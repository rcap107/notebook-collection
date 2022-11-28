import xml
import xml.etree.ElementTree as ET
import pandas as pd

import os
import os.path as osp



def read_file_to_dict(fpath):
    tree = ET.parse(fpath)
    root = tree.getroot()
    info_dict = {}
    print(fpath)
    this_obj, this_obj_values = None, None
    for item in root.findall(".//projectile/../"):
        if item.tag == "label":
            # print(item.text)
            this_obj = item.text
        elif item.tag == "projectile":
            item_children = item.findall(".//")
            this_obj_values = {}
            for child in item_children:
                this_obj_values[child.tag] = child.text
        else:
            continue
        info_dict[this_obj] = this_obj_values 
    return info_dict

tgt_dir = "Rifle"
data_dir = osp.join("data/CE-ammo-stats/Ammo/")
df_data = pd.DataFrame()
for ff in os.listdir(osp.join(data_dir, tgt_dir)):
    f_path = osp.join(data_dir, tgt_dir, ff)
    print(ff)
    info_dict = read_file_to_dict(f_path)
    this_df = pd.DataFrame().from_dict(info_dict, orient='index')
    df_data = pd.concat([df_data, this_df])

df_filtered = df_data.reset_index()[["index", "damageAmountBase", "armorPenetrationSharp", "armorPenetrationBlunt"]].dropna()
df_filtered['ammoType'] = df_filtered['index'].apply(lambda x: x.rsplit(" ", maxsplit=1)[1])

df_filtered.to_csv("rifle_proj_dmg.csv", index=False)
