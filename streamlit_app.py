import streamlit as st
import datetime
from datetime import date, timedelta
import base64
from PIL import Image
from cryptography.fernet import Fernet
import pandas as pd
import streamlit_nested_layout
import numpy as np

st.set_page_config(layout="wide", page_icon="🎓",
                   page_title="Generator")
st.title("🎓 Generator")
left, right = st.columns([1, 3])

right.write("Hasil:")


left.write("Isi datanya:")

jenis = left.selectbox(
    "Matkul",
    ["STD"],
    index=0,
)

if jenis == "STD":
    kelas = left.selectbox(
        "Kelas",
        ("DS-45-GABREM", "IF-45-01", "IF-45-02", "IF-45-03", "IF-45-04", "IF-45-05", "IF-45-06", "IF-45-07", "IF-45-08", "IF-45-09", "IF-45-10", "IF-45-11",
            "IF-45-12", "IF-45-INT", "IF-45-01.1PJJ", "IF-45-02.1PJJ", "IT-45-01", "IT-45-02", "IT-45-03", "IT-45-04", "SE-45-01", "SE-45-02", "SE-45-03")
    )
    left.write('Pilih nomor meja yang tidak bisa digunakan:')
    A, B, C, D, E = left.columns(5)
    option_1 = A.checkbox('1')
    option_2 = A.checkbox('2')
    option_3 = A.checkbox('3')
    option_4 = A.checkbox('4')
    option_5 = A.checkbox('5')
    option_6 = A.checkbox('6')
    option_7 = A.checkbox('7')
    option_8 = A.checkbox('8')
    option_9 = A.checkbox('9')
    option_10 = A.checkbox('10')
    option_11 = B.checkbox('11')
    option_12 = B.checkbox('12')
    option_13 = B.checkbox('13')
    option_14 = B.checkbox('14')
    option_15 = B.checkbox('15')
    option_16 = B.checkbox('16')
    option_17 = B.checkbox('17')
    option_18 = B.checkbox('18')
    option_19 = B.checkbox('19')
    option_20 = B.checkbox('20')
    option_21 = C.checkbox('21')
    option_22 = C.checkbox('22')
    option_23 = C.checkbox('23')
    option_24 = C.checkbox('24')
    option_25 = C.checkbox('25')
    option_26 = C.checkbox('26')
    option_27 = C.checkbox('27')
    option_28 = C.checkbox('28')
    option_29 = C.checkbox('29')
    option_30 = C.checkbox('30')
    option_31 = D.checkbox('31')
    option_32 = D.checkbox('32')
    option_33 = D.checkbox('33')
    option_34 = D.checkbox('34')
    option_35 = D.checkbox('35')
    option_36 = D.checkbox('36')
    option_37 = D.checkbox('37')
    option_38 = D.checkbox('38')
    option_39 = D.checkbox('39')
    option_40 = D.checkbox('40')
    option_41 = E.checkbox('41')
    option_42 = E.checkbox('42')
    option_43 = E.checkbox('43')
    option_44 = E.checkbox('44')
    option_45 = E.checkbox('45')
    option_46 = E.checkbox('46')
    option_47 = E.checkbox('47')
    option_48 = E.checkbox('48')
    option_49 = E.checkbox('49')
    option_50 = E.checkbox('50')

    left.write('Pilih NIM yang tidak akan digunakan:')
    df = pd.read_excel("listNamaPraktikan.xlsx")
    df_kelas = df[df["Kelas"] == kelas].reset_index(drop=True)
    k = 1
    A1, B1 = left.columns(2)
    for i, todo_text in df_kelas["NIM"].iteritems():
        if k >= 1 and k <= np.ceil(len(df_kelas["NIM"])/2):
            A1.checkbox(f'{todo_text}',
                        key='optionNIM_'+str(k))
            k += 1
        elif k >= np.ceil(len(df_kelas["NIM"])/2)+1 and k <= len(df_kelas["NIM"]):
            B1.checkbox(f'{todo_text}', key='optionNIM_'+str(k))
            k += 1

if jenis == "STD":
    df = pd.read_excel("listNamaPraktikan.xlsx")

ATable, BTable, CTable, DTable, ETable = right.columns(5)
d = []
for x in range(1, 51):
    if (eval("option_{0}".format(x)) == True):
        d.append(x)


def get_selected_checkboxes():
    return [i.replace('optionNIM_', '') for i in st.session_state.keys() if i.startswith('optionNIM_') and st.session_state[i]]


NIMhapus = []
res = [eval(i) for i in get_selected_checkboxes()]
for x in range(1, 51):
    if (x in res):
        NIMhapus.append(int(df_kelas["NIM"][x-1]))


def highlight(x): return ['background: red'
                          if x.name in d
                          else '' for i in x]


df_ATemplate = pd.DataFrame()
df_BTemplate = pd.DataFrame()
df_CTemplate = pd.DataFrame()
df_DTemplate = pd.DataFrame()
df_ETemplate = pd.DataFrame()

df_ATemplate["NO"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
df_ATemplate["NIM"] = ["", "", "", "", "", "", "", "", "", ""]
df_ATemplate["ASPRAK"] = ["", "", "", "", "", "", "", "", "", ""]

df_BTemplate["NO"] = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
df_BTemplate["NIM"] = ["", "", "", "", "", "", "", "", "", ""]
df_BTemplate["ASPRAK"] = ["", "", "", "", "", "", "", "", "", ""]

df_CTemplate["NO"] = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
df_CTemplate["NIM"] = ["", "", "", "", "", "", "", "", "", ""]
df_CTemplate["ASPRAK"] = ["", "", "", "", "", "", "", "", "", ""]

df_DTemplate["NO"] = [31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
df_DTemplate["NIM"] = ["", "", "", "", "", "", "", "", "", ""]
df_DTemplate["ASPRAK"] = ["", "", "", "", "", "", "", "", "", ""]

df_ETemplate["NO"] = [41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
df_ETemplate["NIM"] = ["", "", "", "", "", "", "", "", "", ""]
df_ETemplate["ASPRAK"] = ["", "", "", "", "", "", "", "", "", ""]

if ("{}".format(kelas)) not in st.session_state:
    st.session_state["{}".format(kelas)] = df[df["Kelas"] ==
                                              kelas].sample(frac=1).reset_index(drop=True)
df_acak = st.session_state["{}".format(kelas)]
for i in NIMhapus:
    df_acak = df_acak.drop(
        df_acak.index[(df_acak["NIM"] == int(i))], axis=0)
df_acak = df_acak.reset_index(drop=True)

i = 0
for x in range(1, 51):
    if x >= 1 and x <= 10:
        if x not in d and i < len(df_acak):
            df_ATemplate["NIM"][x-1] = df_acak["NIM"][i]
            df_ATemplate["ASPRAK"][x-1] = df_acak["ASPRAK"][i]
            i += 1
    elif x >= 11 and x <= 20:
        if x not in d and i < len(df_acak):
            df_BTemplate["NIM"][x-11] = df_acak["NIM"][i]
            df_BTemplate["ASPRAK"][x-11] = df_acak["ASPRAK"][i]
            i += 1
    elif x >= 21 and x <= 30:
        if x not in d and i < len(df_acak):
            df_CTemplate["NIM"][x-21] = df_acak["NIM"][i]
            df_CTemplate["ASPRAK"][x-21] = df_acak["ASPRAK"][i]
            i += 1
    elif x >= 31 and x <= 40:
        if x not in d and i < len(df_acak):
            df_DTemplate["NIM"][x-31] = df_acak["NIM"][i]
            df_DTemplate["ASPRAK"][x-31] = df_acak["ASPRAK"][i]
            i += 1
    elif x >= 41 and x <= 50:
        if x not in d and i < len(df_acak):
            df_ETemplate["NIM"][x-41] = df_acak["NIM"][i]
            df_ETemplate["ASPRAK"][x-41] = df_acak["ASPRAK"][i]
            i += 1

df_ATemplate = df_ATemplate.astype(
    {"NO": int, "NIM": str, "ASPRAK": str})
df_BTemplate = df_BTemplate.astype(
    {"NO": int, "NIM": str, "ASPRAK": str})
df_CTemplate = df_CTemplate.astype(
    {"NO": int, "NIM": str, "ASPRAK": str})
df_DTemplate = df_DTemplate.astype(
    {"NO": int, "NIM": str, "ASPRAK": str})
df_ETemplate = df_ETemplate.astype(
    {"NO": int, "NIM": str, "ASPRAK": str})
# right.table(df[df["Kelas"] == kelas].sample(frac=1).reset_index(drop=True))

ATable.table(df_ATemplate.set_index('NO').style.apply(highlight, axis=1))

BTable.table(df_BTemplate.set_index('NO').style.apply(highlight, axis=1))

CTable.table(df_CTemplate.set_index('NO').style.apply(highlight, axis=1))

DTable.table(df_DTemplate.set_index('NO').style.apply(highlight, axis=1))

ETable.table(df_ETemplate.set_index('NO').style.apply(highlight, axis=1))

# right.write('## Selected')
# selected_row = grid_table["selected_rows"]
# video.dataframe(selected_row)
