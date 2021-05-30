   # -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 14:31:32 2019

@author: Maimuna Zabair Unoiza

Simple bank ussd code
"""

"""
Algorithim
Enter code:
1.Quick banking
2.Transfer
3.Airtime(self)
4.Airtime(others)
5.enquiry services
6.Data
7.pay bills
8.Open an account
9.Loans
10.lfirstmonie
11.next page
12.exit"""

interator=True
first_bank_ussd= "*894#"
balance= 20000
reg_pin=12345
def bank_uba():
    print('Transfer N',trnf_amount,'to UBA',acnt_number,'account number')
def bank_first():
    print('Transfer N',trnf_amount,'to First bank',acnt_number,'account number')
def bank_union():
    print('Transfer N',trnf_amount,'to Union bank',acnt_number,'account number')
def bank_access():
    print('Transfer N',trnf_amount,'to Access bank',acnt_number,'account number')
def pin_check():
 if reg_pin == pin:
     print('succesful!!! An sms will be sent to you shortly!')
 else:
     print('wrong pin!!')    
    
    
        
while interator:
    print("Welcome!!")
    ussd_code= input("dial ussd code: ")
    if ussd_code == first_bank_ussd:
        print('Welcome to *894# banking')
        option= int(input('1. Quick banking\n2. Open an account\n3. Loans\n4. First monie\n\ninput here: '))
        if option == 1:
             print('\n1. Transfer money\n2. Airtime (self)\n3. Airtime (others)\n4. Enquiry services\n5. Data\n6.Paybills')
             choice = int(input("input here:"))
             if choice == 1:                                                    #transfers
                 trnf_amount = int(input('enter amount: '))
                 acnt_number = int(input('enter account no: '))
                 print('\nSelect bank\n1. UBA\n2. Fbn\n3. Union bank\n4. Access bank')
                 bank_choice = int(input())
                 if bank_choice == 1:
                     print(bank_uba())
                 elif bank_choice == 2:
                     print(bank_first())
                 elif bank_choice == 3:
                     print(bank_union())
                 elif bank_choice == 4:
                     print(bank_access())
                 else:
                     print('Your option is not in our database! bank:')
                 if trnf_amount<balance:
                     print('Transaction succesful!')
                 else:
                     print('Insuficient fund!')
             elif choice == 2:                                                  #airtime self
                 card_amount = int(input('enter amount: '))
                 pin = int(input('input your 5 digit pin: '))
                 print(pin_check)                     
             elif choice == 3:                                                  #airtime others
                 others_number = int(input('number of recipent: '))
                 card_amount = int(input('enter amount: '))
                 print('transfer N',card_amount,' airtime to',others_number,'input your 5 digit pin to continue: ')
                 pin = int(input())
                 print(pin_check())
             elif choice == 4:                                                  #enquiry
                 print('1.balance enquiry\n2.BVN enquir\n3.account number\n4.mini statement')
                 enquiry= int(input('\n'))
                 if enquiry== 1:                                                #balance enquiry
                     pin=int(input('input 5 digit pin to continue'))
                     print(pin_check)
                 elif enquiry == 2:                                             #bvn enquiry
                     pin=int(input('input 5 digit pin to continue'))
                     print(pin_check())
                 elif enquiry == 3:                                             #account number enquiry
                     pin=int(input('input 5 digit pin to continue'))
                     print(pin_check())
                 elif enquiry == 4:                                             #statement enquiry
                     pin=int(input('input 5 digit pin to continue'))
                     print(pin_check())
             elif choice==5:                                                        #Data
                  data_choice = int(input('1. self\n2. others'))
                  if data_choice==1:                                                 #Data self
                      data_amount= int(input('input amount: N'))
                      pin=int(input('input 5 digit pin to continue'))
                      print(pin_check())
                  elif data_choice ==2:                                              #Data others
                      recipent_num = int(input('input recipent phone number: '))
                      data_amount= int(input('input amount: N'))
                      pin=int(input('input 5 digit pin to continue'))
                      print(pin_check())
             elif choice == 6:                                                       #Pay bill 
                  print ('1.cable Tv\n2.electricity\n3.renewable energy\n4.gift and reward')
                  choiece= int(input('\n'))
                  if choice == 1:                                                      #Cable Tv recharge
                      cable=int(input('1.GoTv\n2.DSTV\n3.Startimes\n4.Iroko Tv\n'))
                      cable_recharge = int(input('input amount'))
                      decoder_number= int(input('input decoder number: '))
                      pin=int(input('input 5 digit pin to continue'))
                      print(pin_check())
                  elif choice == 2:                                                       #Electricity
                      electricity=int(input('1.AEDC\n2.Enugu Electricity Distribution Company\n3.Ikeja Electricity\n'))
                      meter_number= int(input('input Meter Number: '))
                      electric_amount = int(input('input amount : '))
                      pin=int(input('input 5 digit pin to continue : '))
                      print(pin_check())
        elif option == 2:                                                           #open account
            open_account= int(input('1.open with BVN\n2.Without BVN'))
            if open_account == 1:
                BVN = int(input('Enter BVN : '))
                print('your bvn has been received')
                first_name= input('enter first name:\t ')
                mid_name= input('enter middle name:\t ')
                last_name = input('enter last name:\t ')
                dob = input('enter DOB(ddmmyyyy):\t ') 
                gender = int(input('select gender\n1.Male\t2.Female:\t '))
                new_pin= int(input('create new 5-digit pin:\t:'))
                confirm_pin =int(input('confirm pin:\t '))
                if gender == 1:
                    print('Dear Mr ',first_name,mid_name,last_name,' your details have successfully been recieved you will recieve an sms containing your account number shortly,thank you.')
                else:
                    print('Dear Miss/Mrs ',first_name,mid_name,last_name,' your details have successfully been recieved you will recieve an sms containing your account number shortly,thank you.')
        elif option ==3:                                       
           choice=int(input('1.Get loans.\n2.Repay loan'))           #Loans
           if choice ==1:
               print('Accept terms and conditions http://www.firstbanknigeria.com\n1. Accept.\n2. Decline.')
               choice=int(input('input here: '))
               if choice==1:                                   #accept
                   loan_amount=int(input('Enter amount:'))
                   pin=int(input('Enter 5-digit pin: '))
                   print(pin_check())
               elif choice==2:                                #Decline
                    print('You have declined the terms and conditions!')
           elif choice==2:                                    #Repay loans
               print('You are not profiled!')
        elif option==4:                                        #first monie
            print('link account to first monie wallet!')
    else:
        print('invalid Ussd dailed!\ntry again')     
    restarter=input('would you like to dial ussd code again and run another transaction?: ') 
    if restarter in ('no','NO','No','n','N'):
        print('Good bye!!\nHave a nice day')
        break
        
