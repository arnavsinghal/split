import streamlit as st
import re

splits = st.text_area("Enter Splitup")

def get_name_value(input_Str):
    name = re.findall(r'(L\d+)\s+=\s+(\d+)', input_Str)
    if len(name) > 0:
        if len(name[0]) == 2:
            return name[0][0], name[0][1]
    return ""

# def get_name(v):
#     name = re.findall(r'L\d+', v)

#     if len(name) > 0:
#         return name[0]
#     return ""

if st.button("click to compute"):
    local = {}
    local_value = splits.split("\n")
    for  v in local_value:
        name, value = get_name_value(v)
        local[name] = int(value)

    idlist = []

    for i in range (1, 30):
        idlist.append("L" + str(i))

    id = {}

    for i in local.keys():
        if i in idlist:
            id[i] = local[i]


    for i,j in enumerate(id.copy()):
        id[str(i+ 1)+"-"+ j] = id[j]
        del id[j]

    st.write("id", local)
    odd = {}
    even = {}

    idlist = list(id.keys())
    idvalues = list(id.values())

    odd[idlist[0] + "-" + str(idvalues[0]-idvalues[1])] = id[idlist[0]]

    even[idlist[1]] = id[idlist[1]]
    even[idlist[2] + "-" + str(idvalues[2] - (idvalues[0]-idvalues[1]))] = id[idlist[2]]

    valueodd = odd.values()
    valueEven = even.values()

    for i in range(3, len(idlist)):
        if sum(valueEven) > sum(valueodd): odd[idlist[i] + "-" + str (sum(valueEven) - sum(valueodd))] = id[idlist[i]]
        else: even[idlist[i] + "-" + str(sum(valueodd) - sum (valueEven)) ] = id[idlist[i]] 
        

    st.write("odd", odd)
    st.write("odd sum", sum(valueodd))

    st.write("even", even)
    st.write("even sum", sum(valueEven))

    if sum(valueodd) > sum(valueEven): 
        st.write("odd > even",(sum(valueodd) - sum(valueEven)))
    else: 
        st.write("even>odd",(sum(valueodd) - sum(valueEven))*-1)
