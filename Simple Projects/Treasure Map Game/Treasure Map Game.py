#Day 4 Treasure Map
row1=['🔐','🔐','🔐']
row2=['🔐','🔐','🔐']
row3=['🔐','🔐','🔐']
print("     1     2    3 ")
print(f"1  {row1}\n2 {row2}\n3 {row3}")
position=input("Select column and row: ")
column=int(position[0])
row=int(position[1])
map=[row1,row2,row3]
map[row-1][column-1]="X"
print("     1     2    3 ")
print(f"1  {row1}\n2 {row2}\n3 {row3}")



'''horizontal=int(position[0])
vertical=int(position[1])
if vertical==1:
    row1[horizontal-1]="X"
    print("     1     2    3 ")
    print(f"1  {row1}\n2  {row2}\n3  {row3}")
elif vertical==2:
    row2[horizontal-1]="X"
    print("     1     2    3 ")
    print(f"1  {row1}\n2  {row2}\n3  {row3}")
elif vertical==3:
    row3[horizontal-1]="X"
    print("     1     2    3 ")
    print(f"1  {row1}\n2  {row2}\n3  {row3}")  
'''
