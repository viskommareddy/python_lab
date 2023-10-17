row1=['X','X','X']
row2=['X','X','X']
row3=['X','X','X']
map=[row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
position=(input('where do you want to put your treasure? '))
horizontal=int(position[0])
vertical=int(position[1])
map[horizontal-1][vertical-1]="🎁"
print(f'{row1}\n{row2}\n{row3}')