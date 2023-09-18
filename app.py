import streamlit as st
input_string = st.text_area("Amounts :")

if st.button("Split"):
  idlist = []

for i in range (1, 22):
    idlist.append("L" + str(i))

id = {}

for i in locals():
    if i in idlist:
        id[i] = locals()[i]


for i,j in enumerate(id.copy()):
    id[str(i+ 1)+"-"+ j] = id[j]
    del id[j]

print(id)
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
    

print(odd, sum(valueodd))
print(even, sum (valueEven))
if sum(valueodd) > sum(valueEven): st.write(sum(valueodd) - sum(valueEven), "odd > even")
else: st.write((sum(valueodd) - sum(valueEven))*-1, "even>odd")
