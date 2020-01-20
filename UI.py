
label = Label(root,text = "Music Player")
label.pack()


#listbox to store all songs

listbox = Listbox(root)
listbox.pack()

#inserting songs to the Listbox
# but the listbox will show them in reverse order
# so displaying the reverse of the list will help

realnames.reverse()

for items in realnames:
    listbox.insert(0,items)

realnames.reverse()

#BUTTONS

nextbutton = Button(root,text = "Next")
nextbutton.pack()

prevbutton = Button(root,text = "Previous")
prevbutton.pack()

stopbutton = Button(root,text = "Stop")
stopbutton.pack()

#binding buttons the functions

nextbutton.bind("<Button-1>",nextsong)
prevbutton.bind("<Button-1>",prevsong)
stopbutton.bind("<Button-1>",stopsong)

songlabel.pack()

root.mainloop
