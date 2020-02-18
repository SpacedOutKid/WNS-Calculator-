#Determines how much money to transfer to what account
from tkinter import *
#A function to calculate the amount for wants,needs,saving and investing
def transferAmount():
    wantsPercent=20
    needsPercent=55
    saveInvestPercent=25
    #Converts percentageinto a decimal
    needsDec=needsPercent/100
    wantsDec=wantsPercent/100
    saveandInvestDec=saveInvestPercent/100
    #Sets and converts the wants,needs,and save into dollar format
    #also links up to the entry boxes and dispalys the result in the dollar format
    wantsTotal=(eval(transferEnt.get()))*wantsDec
    wantsConvert=(f'{wantsTotal:,.2f}')
    wants.set(wantsConvert)
    needsTotal=(eval(transferEnt.get()))*needsDec
    needsConvert=(f'{needsTotal:,.2f}')
    needs.set(needsConvert)
    saveInvestTotal=(eval(transferEnt.get()))*saveandInvestDec
    saveInvestConvert=(f'{saveInvestTotal:,.2f}')
    saveInvest.set(saveInvestConvert)




master=Tk()
master.title('Money To Transfer')
master.configure(bg='dark grey')

#A label and entry to enter the amount to transfer 
transferAmt=Label(master,bg='dark grey',fg='white',text="Enter the amount you are trasnferring:", font=('Californian FB',14))
transferAmt.grid(row=0,column=0,padx=3,pady=10,sticky=E)
transferSign=Label(master,bg='dark grey',fg='white',text='$',font=('Californian FB',14))
transferSign.grid(row=0,column=1,padx=0,pady=30,sticky=W)
transferEnt=Entry(master)
transferEnt.grid(row=0,column=1,pady=30,padx=15,sticky=W)


#A button to caclculate the amount to transfer 
calcBtn=Button(master,text="Calculate",font=('Californian FB',14),command=transferAmount)
calcBtn.grid(row=1,column=0,columnspan=2,sticky=SW,padx=195,pady=20)
#calcBtn.configure(width=2,height=2)

#A label and entry to show the amount for wants
#Wans are considered as consumer purchases, phone, vacation, entertainment, haircuts, clothing 
wants=StringVar()
wantslbl=Label(master, bg='dark grey',fg='white',text='Amount for Wants:',font=('Californian FB',14))
wantslbl.grid(row=2,column=0, sticky=W,pady=15,padx=12)
wantsEnt=Entry(master,state='readonly',fg='green',textvariable=wants)
wantsEnt.grid(row=2,column=1,pady=15,padx=15,sticky=W)
wantsSign=Label(master,bg='dark grey',fg='white',text='$',font=('Californian FB',14))
wantsSign.grid(row=2,column=1,padx=0,pady=15,sticky=W)

#A label and entry to show the amount for needs
#Meeds are consifered as #housing, food, health, utilities, bills, Transportation
needs=StringVar()
needslbl=Label(master, bg='dark grey',fg='white',text='Amount for Needs:',font=('Californian FB',14))
needslbl.grid(row=3,column=0, sticky=W,pady=3,padx=13)
needsEnt=Entry(master,state='readonly',textvariable=needs,fg='green')
needsEnt.grid(row=3,column=1,pady=3,padx=15,sticky=W)
needsSign=Label(master,bg='dark grey',fg='white',text='$',font=('Californian FB',14))
needsSign.grid(row=3,column=1,padx=0,pady=3,sticky=W)


#A label and entry to show the amount for Saving and Investing 
#Saving & Investing are considered IRA, 401k, debt. emergency fund
saveInvest=StringVar()
saveInvestlbl=Label(master, bg='dark grey',fg='white',text='Amount for Saving/Investing:',font=('Californian FB',14))
saveInvestlbl.grid(row=4,column=0, sticky=W,pady=12,padx=13)
saveInvestEnt=Entry(master,state='readonly',text=saveInvest,fg='green')
saveInvestEnt.grid(row=4,column=1,pady=12,padx=15,sticky=W)
saveInvestSign=Label(master,bg='dark grey',fg='white',text='$',font=('Californian FB',14))
saveInvestSign.grid(row=4,column=1,padx=0,pady=12,sticky=W)





master.mainloop()
