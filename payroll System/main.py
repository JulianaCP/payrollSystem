__author__ = 'Juliana Campos and Johanna'
#solicitudAmi: here are the different applications that workers perform their supervisor
#userList: here all the information of the users of the company
#ListOfPost: here are the different jobs that are in the company
#listOfplanilla: here are all the information about the payroll of avery one in the compay
#insentiveList: here is all the information regarding each evaluation for each employee of the company
#listOfAguinaldo: here all the information about the calculations obtained the bonus of employees
#respSolicitud: the answer the requests done for employees of the company are stored here
#infVacaEmpleados: all information regarding user holidays and days available to the user to make use of free days and the number of days requested this
solicitudAdmi=[{"identification":"12345","FullName":"johanna Ruiz","Dias Solicitados":"2"},
               {"identification":"1234","FullName":"marianita","Dias Solicitados":"6"}]

usersList = [{"identification": "12345","FullName":"johanna Ruiz","UserName": "johannita", "Password": "joha123", "Address": "pavas","Telephone": "85649475",
              "dateIncome": "19/01/2015","Type": "administrator","IDjob": "ADM", "state":"active"},
             {"identification": "123456","FullName":"carlos","UserName": "carlos", "Password": "carlos", "Address": "pavas","Telephone": "85649475",
              "dateIncome": "19/01/2015","Type": "employee","IDjob": "CNT", "state":"active"},
             {"identification": "1234","FullName":"marianita","UserName": "mariposa", "Password": "mari123", "Address": "pavas","Telephone": "123456",
              "dateIncome": "19/01/2015","Type": "employee","IDjob": "SCT", "state": "inactive"}] 

ListOfPosts= [{"IDjob": "ADM","jobName": "administrator","salaryPerHour": 4000,"nameOfSupervisor": " "},
              {"IDjob": "SCT","jobName": "secretary", "nameOfSupervisor": "johanna Ruiz","salaryPerHour":2000 },
              {"IDjob": "CNT","jobName": "contador","salaryPerHour": 3000,"nameOfSupervisor": "johanna Ruiz"},
              {"IDjob": "SSS","jobName": "ninguno","salaryPerHour": 4000,"nameOfSupervisor": " "}]

listOfplanilla= [{'extrahours': 8, 'grossSalary': 352000, 'netEarnings': 347840.0, 'insentive': 24640, 'identification': '1234', 'saryOrdinary': 320000,
                  'month': '2', 'overtimeSalary': 32000, 'regularHours': 160, 'year': "2015", 'totalhours': 168, 'deductions': 28800.0,"FullName":"marianita"}]

insentivelist= [{'month': '2', 'calification': 90, 'identification': '1234', 'insentive': 0.07, 'FullName': 'marianita', 'IDjob': 'SCT'},
                {'month': '3', 'calification': 80, 'identification': '123456', 'insentive': 0.05, 'FullName': 'carlos', 'IDjob': 'CNT'}]

listOfAguinaldo=[]

respSolicitud=[]

infVacaEmpleados=[{"FullName":"marianita","identification":"1234","Dias Disponibles":"0","Dias Totales Solicitados":"2"},
                  {"FullName":"johanna Ruiz","identification":"12345","Dias Disponibles":"12","Dias Totales Solicitados":"2"}]

def login():
#program inputs: the user name and password of the person
#program outputs: the main menu (employee menu or administrator menu) depend what type is the worker, a note warning the user of a problem occurred in if necessary
#restrictions: must be a worker of the company, can not leave empty spaces
#Description: It ensures that the person can enter to the program(for login)verifies that both the username and password are correct and belong to a user traveling userList
    userName = input("type the username: ")
    password = input("type the password: ")
    cont     = 0
    x= 0
    while cont < len(usersList):
        if userName=='' or password=='':
            print("You can not leave empty fields","\n")
            login()
        elif usersList[cont]["UserName"]==userName and usersList[cont]['Password']==password:
            type= usersList[cont]["Type"]
            x= 1
            if usersList[cont]['Type']=='administrator':
                menuAdministrator(type)
                break

            else:
                employeeMenu(type)
                break
        else:
            cont += 1
    if x == 0:
        print("ERROR: the person don't be found")
        print("")
        login()


def continuarEvaluacionAño(obtencioDatoFechaFinal, prinCont,identification,fullName,userName,password,address,telephone,userType,IDJob):
#program inputs: the date income of the worker(obtencioDatoFechaFinal), a special program summation(prinCont), the employee :identification, full name, user name, password, address, telephone, user type and id
#program outputs: the employee :identification, full name, user name, password, address, telephone, user type and id job and go to the addUser method
#restrictions: have a correct format,  have to be only 2015, only numbers
#Description: the program evaluates if the entered year is 2015,To accomplish this the program evaluates the positions of the user typed whith the prinCont(special program summation)

    if obtencioDatoFechaFinal[prinCont] == "/":
        prinCont += 1
        if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 2:
            prinCont += 1
            if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 0:
                prinCont += 1
                if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 1:
                    prinCont += 1
                    if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 5:
                        prinCont += 1
                        addUser(obtencioDatoFechaFinal,identification,fullName,userName,password,address,telephone,userType,IDJob)

def continuarEvaluacionMes(obtencioDatoFechaFinal, prinCont,identification,fullName,userName,password,address,telephone,userType,IDJob):
#program inputs: the date income of the worker, a special program summation(prinCont), the employee :identification, full name, user name, password, address, telephone, user type and id
#program outputs:a note warning the user of a problem occurred in if necessary. The date income of the worker, a special program summation, employee: identification, full name, user name, password, address, telephone, user and go to continuarEvaluacionAño method
#restrictions: have the correct format , only numbers, cant to be more than 12
#Description: the program evaluates if the entered date is in the correct format and cant to be more than 12,To accomplish this the program evaluates the positions of the user typed whith the prinCont(special program summation)

    if obtencioDatoFechaFinal[prinCont] == "/":
        prinCont += 1
        if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) < 2:
            prinCont += 1
            if obtencioDatoFechaFinal[prinCont -1] == "0" and int(obtencioDatoFechaFinal[prinCont]) > 0 and int(obtencioDatoFechaFinal[prinCont]) <= 9:
                prinCont += 1
                continuarEvaluacionAño(obtencioDatoFechaFinal, prinCont,identification,fullName,userName,password,address,telephone,userType,IDJob)

            elif obtencioDatoFechaFinal[prinCont -1] == "1" and int(obtencioDatoFechaFinal[prinCont]) <= 2:
                prinCont += 1
                continuarEvaluacionAño(obtencioDatoFechaFinal, prinCont,identification,fullName,userName,password,address,telephone,userType,IDJob)

            else:
                print("ERROR")
                obtainUserData()
        else:
            print("ERROR")
            obtainUserData()
    else:
        print("error you type wrong")
        obtainUserData()

def evaluarFecha(contadorSec, dateIncome,identification,fullName,userName,password,address,telephone,userType,IDJob):
#program inputs: the date income of the worker, a special program summation, the employee :identification, full name, user name, password, address, telephone, user type and id
#program outputs: the employee :the date income of the worker, the length of the characters typed by the user(contadorSec), employee: identification, full name, user name, password, address, telephone, user and go to continuarEvaluacionMes method
#restrictions: only numbers, cant to be more than 31
#the program evaluates if the entered date is in the correct format and cant to be more than 31,To accomplish this the program evaluates the positions of the user typed
#Description: the special program sumation is for to have the position of the different characters typed by the user(prinCont)

    prinCont = 0
    while prinCont < contadorSec:

        if dateIncome[prinCont].isdigit() and int(dateIncome[prinCont]) <= 3:
            prinCont += 1

            if dateIncome[prinCont -1] == 3:

                if dateIncome[prinCont] > 1:
                    print("Date format error, please try again")
                    obtainUserData()
                else:
                    prinCont += 1
                    continuarEvaluacionMes(dateIncome, prinCont,identification,fullName,userName,password,address,telephone,userType,IDJob)

            else:
                prinCont += 1
                continuarEvaluacionMes(dateIncome, prinCont,identification,fullName,userName,password,address,telephone,userType,IDJob)

        else:
            print("Date format error, please try again")
            obtainUserData()

def obtainUserData():
#program inputs: the date income of the worker, the employee :identification, full name, user name, password, address, telephone, user type and id that the user will be typed
#program outputs: the date income of the worker, a special program summation fo to know how long is the date income(contadorSec), employee: identification, full name, user name, password, address, telephone, user and all go to evaluarFecha method
#a note warning the user of a problem occurred in if necessary, go to main menu or continue with the program if you choise that if you are wrong
#restrictions: have to be only employee or administrator in the user type,can't be a worker of the company in list, can not leave empty spaces, format of date:  dd/mm/aaaa  only
#Description: This method performs the function prompt the user's personal data, analyzes them to be valid according to the applied constraints and sends other methods to specify the revision of some data and finally to store these in a list

    choise= input("please press 1 add new employee or press 2 for go to menu: ")
    if choise == "1":
        identification = input("type the identification: ")
        fullName = input("type the full name of the person: ")
        userName = input("type the username: ")
        password = input("type the password: ")
        address = input("type the address of the user: ")
        telephone= input("type the telephone number: ")
        if identification == "" or fullName == "" or userName == "" or password== "" or address =="" or telephone =="":
            print("ERROR: plese try again")
            obtainUserData()
        c= 0
        while c < len(usersList):
            if usersList[c]["identification"]== identification:
                print("the employee exist in the program")
                obtainUserData()
            c +=1
        userType= input("type the user type(administrator/employee): ")
        if userType == "employee" or userType == "administrator":
            IDJob = input("type the ID of the job: ")
            conta= 0
            x= 1
            while conta < len(ListOfPosts):
                if ListOfPosts[conta]["IDjob"]== IDJob:
                    x= 0
                    dateIncome=input("Type the date income dd/mm/aaaa : ")
                    if dateIncome == '':
                        print("Date format error, please try again")
                        obtainUserData()

                    contadorSec = 0
                    prinCont = 0
                    for element in dateIncome:
                        contadorSec += 1

                    if contadorSec > 10:#10 because the format have only 10 characters
                        print("ERROR")
                        obtainUserData()
                    if contadorSec == 10:
                        try:
                            from datetime import datetime
                            formato_fecha = "%d/%m/%Y"#a format to get the date correctly
                            datetime.strptime(dateIncome,formato_fecha)# to the date of admission by the user has typed format
                            evaluarFecha(contadorSec, dateIncome,identification,fullName,userName,password,address,telephone,userType,IDJob)
                        except ValueError:
                            print("ERROR: the date is incorrect")
                            obtainUserData()


                    else:
                        print("ERROR")
                        obtainUserData()
                conta+=1
            if x == 1:
                print("ERROR: the ID it's not in the company")
                choise= input("please press 1  for to try again or press 2 for go to menu: ")
                if choise == "1":
                    obtainUserData()
                if choise == "2":
                    admin= "administrator"#to send as parameter "administrator" to recognize the type so the user when a function is shared between the manager and the employee
                    menuAdministrator(admin)
                else:
                    print("ERROR")
                    obtainUserData()

        else:
            print("ERROR: You can just type in what appears on screen")
            obtainUserData()

    if choise == "2":
        admin= "administrator" #to send as parameter "administrator" to recognize the type so the user when a function is shared between the manager and the employee
        menuAdministrator(admin)
    else:
        print("ERROR")
        obtainUserData()

def addUser(btencioDatoFechaFinal,identification,fullName,userName,password,address,telephone,userType,IDJob):

#Description: save all information from the function continuarEvaluacionAño in a dicctionary an then go to the userList
##program inputs: the employee :identification, full name, user name, password, address, telephone, user type and id job and date income
#program outputs:save all information in the userList

    global  usersList
    diccionarioPrincipal = {}
    diccionarioPrincipal["identification"]= identification
    diccionarioPrincipal["FullName"]= fullName
    diccionarioPrincipal["UserName"]= userName
    diccionarioPrincipal["Password"] = password
    diccionarioPrincipal ["Address"]= address
    diccionarioPrincipal["Telephone"] = telephone
    diccionarioPrincipal ["dateIncome"] = btencioDatoFechaFinal
    diccionarioPrincipal["Type"] = userType
    diccionarioPrincipal["state"]= "active" 
    diccionarioPrincipal["IDjob"]= IDJob
    usersList.append(diccionarioPrincipal)
    admin= 'administrator' #to send as parameter "administrator" to recognize the type so the user when a function is shared between the manager and the employee
    print("saved data")
    menuAdministrator(admin)

def createSince():
#program inputs: the id and name of the new job, supervisor name, and salary per hour of the new job
#program outputs: a note warning the user of a problem occurred in if necessary, go to the main menu, the information about the new job
#restictions: the supervisor have to be an administrator, can not leave empty spaces, the new id job and name can't exist in the program, the salary only can be numbers
#Description: this method cre new post requesting information regarding restrictions and following protocols approved once everything is done and the information stored in a diccionary an then in a ListOfPosts

    global ListOfPosts
    diccionarioDePuestos= {}
    IDJob = input("type the ID of the job: ")
    jobName = input("type the job name: ")
    nameOfSupervisor= input("type the name of supervisor: ")
    if IDJob != "" and jobName != "" and nameOfSupervisor != "":
        try:
            salaryPerHour= int(input("type the salary per hour: "))

        except:
            salaryPerHour= str
            print("ERROR: please insert numbers")
            createSince()
        cont = 0
        while cont < len(ListOfPosts):
            if ListOfPosts[cont]["IDjob"] == IDJob or ListOfPosts[cont]["jobName"]== jobName:
                print("this work already exists")
                createSince()
            cont += 1

        contador= 0
        while contador < len(usersList):
            if usersList[contador]["FullName"]== nameOfSupervisor and usersList[contador]["Type"]== "administrator":
                diccionarioDePuestos["IDjob"]=  IDJob
                diccionarioDePuestos["jobName"]= jobName
                diccionarioDePuestos["nameOfSupervisor"]= nameOfSupervisor
                diccionarioDePuestos["salaryPerHour"]= salaryPerHour
                ListOfPosts.append(diccionarioDePuestos)
                conta= 0
                while conta < len(ListOfPosts):
                    if ListOfPosts[conta]["IDjob"]== IDJob:
                        print(ListOfPosts[conta])
                        d= "administrator"
                        menuAdministrator(d)
                    conta +=1
            contador += 1
        if contador == len(usersList):
            print("ERROR: the supervisor is not found")

    else:
        print("ERROR: you can't leave empty spaces")
        createSince()
    admin= 'administrator'
    menuAdministrator(admin)

def changeSince():
#program inputs: the worker identification, full name, the id job, the user type and a number if the user is wrong and want to go to another functions
#program outputs: the new information of the employee and a note warning the user of a problem occurred in if necessary
#restictions:can not leave empty spaces, the id and the user have to exist in the information of the program, have to be only employee or administrator in the user type
#Description: this method changes the job by exchanging the last for new information given by the administrator through a cycle verified that there is the list of users and also the position of the information is verified to change past and replaced by the new

    global  usersList
    identification = input("type the identification of the person: ")
    fullName = input("type the full name of the person: ")
    if identification != "" and fullName != "":
        cont= 0
        x = False
        while cont < len(usersList):
            if usersList[cont]["identification"]== identification and usersList[cont]["FullName"]== fullName:
                x = True
                userType= input("type the new user type(administrator/employee): ")
                if userType == "employee" or userType == "administrator":
                    IDJob = input("type the new ID of the job: ")
                    contando= 0
                    enterData= 1
                    while contando < len(ListOfPosts):
                        if ListOfPosts[contando]["IDjob"]== IDJob:
                            enterData= 0
                            usersList[cont]["Type"]= userType
                            usersList[cont]["IDjob"]= IDJob
                            print(usersList[cont])
                            admin= "administrator"
                            menuAdministrator(admin)
                            break
                        contando += 1
                    if enterData == 1:
                        print("the ID not exist")
                        choise= input("please press 1  for to try again or press 2 for go to menu: ")
                        if choise == "1":
                            changeSince()
                        if choise == "2":
                            admin= 'administrator'
                            menuAdministrator(admin)
                        else:
                            print("ERROR")
                            changeSince()

                else:
                    print("error has typed wrong")
                    choise= input("please press 1  for to try again or press 2 for go to menu: ")
                    if choise == "1":
                        changeSince()
                    if choise == "2":
                        admin= 'administrator'
                        menuAdministrator(admin)
                    else:
                        print("ERROR")
                        changeSince()
            else:
                cont += 1

        if x == False:
            print("ERROR: the person don't be found")
            choise= input("please press 1  for to try again or press 2 for go to menu: ")
            if choise == "1":
                changeSince()
            if choise == "2":
                admin= "administrator"
                menuAdministrator(admin)
            else:
                print("ERROR")
                changeSince()
    else:
        print("ERROR: you can't leave empty spaces")
        choise= input("please press 1  for try again or press 2 for go to menu: ")
        if choise == "1":
            changeSince()
        if choise == "2":
            admin= 'administrator'#to send as parameter "administrator" to recognize the type so the user when a function is shared between the manager and the employee
            menuAdministrator(admin)
        else:
            print("ERROR")
            changeSince()

def saveDataAbouthPlanilla(overtimeT,salaryOrdinary,grossSalary1,deductions,netEarnings,insentive,identification,month,TotalHours,ExtraHours,RegularHours):
#program inputs: the worker: extra salary, salary ordinary, gross salary, deduction on wage, mont of the insentive, user identification, extra hours worked and regular hours too
# progran outputs: the information going to be save in a diccionary an then in a userList, a message indicating that the information is saved
#Description: the information received from the parameters is stored in this method

    cont= 0
    while cont < len(usersList):
        if usersList[cont]["identification"]== identification:
            fullname= usersList[cont]["FullName"]
            diccionary= {}
            diccionary["insentive"]= insentive
            diccionary["identification"]= identification
            diccionary["grossSalary"]= grossSalary1
            diccionary["overtimeSalary"]= overtimeT
            diccionary["deductions"]= deductions
            diccionary["netEarnings"]= netEarnings
            diccionary["saryOrdinary"]= salaryOrdinary
            diccionary["month"]= month
            diccionary["FullName"]= fullname
            diccionary["regularHours"]= RegularHours
            diccionary["totalhours"]= TotalHours
            diccionary["extrahours"]= ExtraHours
            diccionary["year"]= "2015"
            listOfplanilla.append(diccionary)
            print("were saved data")
            x= "administrator"
            menuAdministrator(x)
            break

        else:
            cont+= 1


def calculoincentivo(grossSalary,month,deductions,identification,salaryOrdinary,overtimeT,TotalHours,ExtraHours,RegularHours):
#program inputs: the gross salary, month, deductions mont, user identification, salary ordinary, extra salary, hours worked, extra hours and regular hours, a number if the person going to put the answer to the question for go to some function
#program outputs: a note warning the user of a problem occurred in if necessary,the gross salary, month, deductions mont, user identification, salary ordinary, extra salary, hours worked, extra hours and regular hours
#restrictions: have to be the insentive for can to do the calculations, have to put only one or two if goig to to the answer for the question if the user was wrong
#Description: checks whether the uncommitted already been evaluated and sent to company data for calculation of net salary and incentive paid by the company

    cont= 0
    d=0
    while cont < len(insentivelist):
        if insentivelist[cont]["month"]== month and insentivelist[cont]["identification"]== identification:
            d= 1
            insentive= insentivelist[cont]["insentive"]
            insentive = int(insentive * grossSalary)
            print("incentive bonus",".....................",insentive )
            netEarnings= grossSalary - deductions + insentive
            print("net earnings: ","......................",str(int(netEarnings)))
            saveDataAbouthPlanilla(overtimeT,salaryOrdinary,grossSalary,deductions,netEarnings,insentive,identification,month,TotalHours,ExtraHours,RegularHours)

        cont += 1
    if d== 0:
        print("can not show the other calculations as the incentive or bonus is still not added")
        choise= input("please press 1  for try again or press 2 for go to menu: ")
        if choise == "1":
            addHoursEmployee()
        if choise == "2":
            admin= 'administrator'
            menuAdministrator(admin)
        else:
            print("ERROR")
            changeSince()

def planilla(salaryxh,identification,TotalHours,ExtraHours,RegularHours):
#program inputs:  the month the salary per hour of the worker, identification total hours worked extra and regular hours worked for the employee
#program outputs: iformation for the calculo insentivo like: the gross salary, month deductions user identification salary ordinary salary extra ordinary total, extra and regulars hours worked
#restrictions: the month have to be 1,2,3...12 , can not be assessed the same month which has already been calculated payroll
#Description: verifies that the correct fingering month also performs calculations to also take the different types of wage Company,with a cycle is found that the fingering month is not in the ListOfPlanilla

    salaryOrdinary = (salaryxh * 8)* 5 * 4 #5 days, #8 hours, 4 weeks(month)
    month= input("month: ")
    if month=="1" or month=="2" or month=="3" or month=="4" or month=="5" or month=="6" or month=="7" or month=="8" or month=="9" or month=="10" or month=="11" or month=="12":
        contador= 0
        while contador < len(listOfplanilla):
            if listOfplanilla[contador]["month"] == month and listOfplanilla[contador]["identification"] == identification:
                print("ERROR: the payroll of this month already exists in list")
                admin= 'administrator'
                menuAdministrator(admin)
            contador += 1
            
        overtimeT =  (salaryxh * 2)* ExtraHours
        print( "overtime worked","....................",str(overtimeT))
        grossSalary= overtimeT + salaryOrdinary
        print( "gross salary",".......................",str(grossSalary))
        print("regular salary","......................",str(salaryOrdinary))
        deductions= (0.09 * salaryOrdinary)
        print("deduction of wages","..................",str(int(deductions)))
        calculoincentivo(grossSalary,month,deductions,identification,salaryOrdinary,overtimeT,TotalHours,ExtraHours,RegularHours)
    else:
        print("the month not exist")
        choise= input("please press 1  for to try again or press 2 for go to menu: ")
        if choise == "1":
            planilla(salaryxh,identification,TotalHours,ExtraHours,RegularHours)
        if choise == "2":
            admin= 'administrator'
            menuAdministrator(admin)
        else:
            print("ERROR")
            confirmIdForPlanilla(TotalHours,ExtraHours,RegularHours)

def confirmIdForPlanilla(TotalHours,ExtraHours,RegularHours):
#program inputs: the total, extra and regular hours worked by the employee, the answer of the user if this user was wrong
#program outputs: a note warning the user of a problem occurred in if necessary,go to the main menu if the user type two when the program say, the salary per hour, identification, total extra and regular hours of the employee
#restrictions: the worker have to exist previusly in the program
#Description: confirm if the employee works in the company for can to do the calculations of payroll in another method

    global ListOfPosts
    global usersList
    IDJob = input("type the ID of the job: ")
    identification = input("please type the worker identification: ")
    x = True
    cont= 0
    while cont < len(ListOfPosts):
        if ListOfPosts[cont]["IDjob"]== IDJob:
            salaryxh = ListOfPosts[cont].get("salaryPerHour")
            contado=0
            while contado < len(usersList):
                if usersList[contado]["identification"]== identification and usersList[contado]["IDjob"]== IDJob:
                    planilla(salaryxh,identification,TotalHours,ExtraHours,RegularHours)
                contado +=1
        cont += 1
    if x == True:
        choise= input("the ID or the identification are incorrects, please press 1  for to try again or press 2 for go to menu: ")
        if choise == "1":
            confirmIdForPlanilla(TotalHours,ExtraHours,RegularHours)
        if choise == "2":
            admin= 'administrator'
            menuAdministrator(admin)
        else:
            print("ERROR")
            confirmIdForPlanilla(TotalHours,ExtraHours,RegularHours)

def addHoursEmployee():
#inputs: Requires ID of the employee and amount hours worked obtained by input
#outputs: Total hours worked, overtime and regular hours obtained by mathematical calculations (subtraction),error message if the established restrictions are not met
#restrictions: Only you can type 1 or 2 for program continuity,Only you can add hours to an employee that exist in the company,the hours can not be greater than 192 or less than 160
#the function is responsible for registering the extras, regular and total employee hours for sending data parameters to another function
    global usersList
    global listOfplanilla
    wantAddHours=input("1. want to add hours to an employee 2. other process: ")
    if wantAddHours=="1":
        IDEmpleadoAgregar=input("ID of the employee ")
        cont=0
        while cont<len(usersList):
            if usersList[cont]["identification"]==IDEmpleadoAgregar:
                try:
                    existe="si"
                    howManyHours=int(input("monthly hours worked "))
                except:
                    howManyHours=str
                    print("ERROR: try again")
                    print("prueba")
                    addHoursEmployee()

                if existe =="si":
                    if howManyHours<=192 and howManyHours>=160:
                        TotalHours=int(howManyHours)
                        ExtraHours=TotalHours-160
                        RegularHours=160
                        print("total hours:",TotalHours)
                        print("extra hours:",ExtraHours)
                        print("regular hours:",RegularHours)
                        
                        confirmIdForPlanilla(TotalHours,ExtraHours,RegularHours)


                    elif howManyHours >192:
                        print("hours out of limits, 'the limit is 192'")
                        addHoursEmployee()
                    elif howManyHours<160:
                        print("the hours are lowers, can't do the math, try again")
                        addHoursEmployee()

            else:
                cont=cont+1
        if cont==len(usersList):
            print("the employee is not found, enter the data again")
            addHoursEmployee()

    elif wantAddHours=="2":
        w= "administrator"
        menuAdministrator(w)

    else:
        print("Data input error")
        addHoursEmployee()

def deletePosts():
# inputs: ID of the Post to be deleted.
#outputs:a note warning the user of a problem occurred in if necessary, a information note saying the post be remove
#restrictions: the Post can't be deleted if the ID job is associated to a person, the id of the job have to exist in the program
#Description: delete some job of the company when the administratos typed it. with a cycle searches the job id does not belong to anyone, equally satisfying the constraints

    global  usersList
    global  ListOfPosts
    postdelete= input("Type the ID of the Post to be deleted: ")
    contador=0
    m= False
    while contador < len(ListOfPosts):
        if ListOfPosts[contador]["IDjob"]== postdelete:
            cont = 0
            while cont < len(usersList):
                if usersList[cont]["IDjob"]== postdelete:
                    print("ERROR: The Post can't be deleted because the ID job is associated to a person")
                    admin= 'administrator'
                    menuAdministrator(admin)

                    break
                cont+=1
            conta = 0
            while conta < len(ListOfPosts):
                if ListOfPosts[conta]["IDjob"] == postdelete:
                    m= True
                    print("The post " ,postdelete, " has been removed")
                    del ListOfPosts[conta]
                    admin= 'administrator'
                    menuAdministrator(admin)
                    break
                conta +=1

        contador +=1
    if m == False:
        print("ERROR: ID not exist")
        choise= input("please press 1  for try again or press 2 for go to menu: ")
        if choise == "1":
            deletePosts()
        if choise == "2":
            admin= 'administrator'
            menuAdministrator(admin)
        else:
            print("ERROR")
            deletePosts()

def printListOfPost():
#outputs:  The information to Post List contains
# Description: show all the information about the diferents post of the company

    cont = 0
    print("The Post List contains: ")
    while cont<len(ListOfPosts):
        print(ListOfPosts[cont])
        cont+=1
    print("\n")

def employeeState():
#inputs: the identification and full name of the employee
#outputs: a note saying if the employee is active or inactive,note warning the user of a problem occurred in if necessary
#restrictions: the person have to be a user work of the company
#Description: show the state of the worker. through the userList and positions where the information is located on the employee's status
    global  usersList
    identification = input("type the identification: ")
    fullName = input("type the full name of the person: ")
    cont= 0
    notification= True
    while cont < len(usersList):
        if identification == usersList[cont]["identification"] and fullName == usersList[cont]["FullName"]:
            notification = False
            if usersList[cont]["state"]== "active":
                print("the employee is active")
                x= "administrator"
                menuAdministrator(x)
                break
            else:
                print("the employee is not active")
                x= "administrator"
                menuAdministrator(x)
        cont += 1

    if notification == True:
        print("ERROR. the full Name or the identification are incorrects, please try again")
        employeeState()

def inactiveEmployes():
#output: the name and identification of all the inactives workers of the company or if nobody is active show all the workers are actives
#Description: the name and identification of all the inactives workers of the company. to scroll through the list of users the state is located and if it is inactive and identification of the name is displayed this

    cont= 0
    x= True
    while cont < len(usersList):
        if usersList[cont]["state"] != "active":
            x= False
            print("name: ",usersList[cont]["FullName"])
            print("identification:",usersList[cont]["identification"],"\n")
        cont += 1
    if x == True:
        print("all the workers are actives")
        d= "administrator"
        menuAdministrator(d)
    else:
        d= "administrator"
        menuAdministrator(d)
def history(volver):
#inputs: the worker full name and identification, (volver) a information for to know if the user is a employee or is administrator for can to come again to the respective menu
#output: all the worker information,note warning the user of a problem occurred in if necessary,
#restrictions: the person have to be a user worker of the company
#Description: once found the worker in userList of all your personal information is printed
    global  usersList
    name= input("type the full name: ")
    identification= input("type the identification: ")
    cont= 0
    x= True
    while cont < len(usersList):
        if usersList[cont]["FullName"] == name and usersList[cont]["identification"] == identification:
            x= False
            print("identification is:",usersList[cont]["identification"])
            print("the full name is:", usersList[cont]["FullName"])
            print("adress: ", usersList[cont]["Address"])
            print("telephone number: ", usersList[cont]["Telephone"])
            print("type: ", usersList[cont]["Type"])
            print("date income: ", usersList[cont]["dateIncome"])
            print("ID job: ", usersList[cont]["IDjob"])
            print("state: ", usersList[cont]["state"])
            
            if volver == "administrator":
                menuAdministrator(volver)
            else:
                employeeMenu(volver)
            break
        else:
            cont += 1
    if x == True:
        print("ERROR. the persond don't be found")
        history(volver)

def saveInsentive(insent,month,worker,job,califucation,identification):
#inputs: the insentive worker, worker,job,calification and identification of the worker. the answer option if the person have to do another calification or want to go to the main menu
#output: the saved information, return the saved iformation
#restriccion: to return to the menu or continue only you can type what prompted
# Description: save the information about the worker calification in a diccionary and then in insentiveList

    global  insentivelist
    dictionary= {}
    dictionary["identification"]= identification
    dictionary["insentive"]= insent
    dictionary["month"]= month
    dictionary["FullName"]= worker
    dictionary["IDjob"]= job
    dictionary["calification"]= califucation
    insentivelist.append(dictionary)
    print(dictionary)
    choise= input("please press 1  for another calification, or press 2 for go to menu: ")
    if choise == "1":
        incentive()
    if choise == "2":
        admin= 'administrator'
        menuAdministrator(admin)
    else:
        print("ERROR: try again")
        incentive()

def incentive():
#inputs: the worker identification and name . Supervisor full name
#outputs: a note warning the user of a problem occurred in if necessary the following information will be sent insent,month and calification  typed by he administrator and  the worker identification and job and go to saveInsentive
#restrictions: the month evaluate can't be in the same month of another, the month have to exist, only the worker administrator can evaluate him, the calification can't be more than 100 or less than 0
#Description: can qualify an employee for their commitment to the company from 1 to 100 also will have an extra percentage of salary. it will tour some lists to verify that everything is in rule

    global ListOfPosts
    cont = 0
    x= False
    identification = input("type the worker identification: ")
    supervisor= input("type your name: ")
    worker= input("type the worker name: ")
    while cont < len(ListOfPosts):
        if ListOfPosts[cont]["nameOfSupervisor"]== supervisor:
            job= ListOfPosts[cont]["IDjob"]
            conta= 0
            while conta < len(usersList):
                if usersList[conta]["IDjob"]== job and usersList[conta]["FullName"]== worker and usersList[conta]["identification"]== identification :
                    x= True
                    try:
                        calification= int(input("type the calification(0/100): "))
                        month= input("type the month: ")
                        contando=0
                        while contando < len(insentivelist):
                            if insentivelist[contando]["month"]== month and insentivelist[contando]["identification"]== identification:
                                print("ERROR the evaluation is in list")
                                w= "administrator"
                                menuAdministrator(w)
                            contando += 1
                        if month=="1" or month=="2" or month=="3" or month=="4" or month=="5" or month=="6" or month=="7" or month=="8" or month=="9" or month=="10" or month=="11" or month=="12":
                            if calification < 0:
                                print("ERROR calification not exist")
                                w="administrator"
                                menuAdministrator(w)
                            if calification == 0 or calification <= 20:
                                insent= 0
                                saveInsentive(insent,month,worker,job,calification,identification)
                            if calification >20 and calification <= 40:
                                insent= 0.02
                                saveInsentive(insent,month,worker,job,calification,identification)
                            if calification > 40 and calification <= 60:
                                insent= 0.03
                                saveInsentive(insent,month,worker,job,calification,identification)
                            if calification > 60 and calification <= 80:
                                insent= 0.05
                                saveInsentive(insent,month,worker,job,calification,identification)
                            if calification > 80 and calification <= 100:
                                insent= 0.07
                                saveInsentive(insent,month,worker,job,calification,identification)
                                break
                            else:
                                print("ERROR calification not exist")
                                w="administrator"
                                menuAdministrator(w)
                    except:
                        calification = str
                        print("ERROR: type wrong, please try again")
                        incentive()
                    else:
                        print("ERROR: the month not exist")
                        w="administrator"
                        menuAdministrator(w)

                conta += 1


        cont += 1

    if x == False:
        print("ERROR: you can't to evaluate this worker")
        admin= 'administrator'
        menuAdministrator(admin)



        
def totalBonusesIncentives():
#output: show the sum total of all insentivos paid by the company
# in this method we'll be adding all incentives paid by the company, once completed it will be sent to the main menu administrators

    cont = 0
    suma= 0
    while cont < len(listOfplanilla):
        suma=  suma + listOfplanilla[cont]["insentive"]
        cont += 1
    print("Total Insentive: ",suma)
    w= "administrator"
    menuAdministrator(w)

def seeTheCalification(volver):
#inputs:the worker :identification, the month of the calification , the complete name of the worker,(volver) a information for to know if the user is a employee or is administrator for can to come again to the respective menu
#outputs:  a note warning the user of a problem occurred in if necessary, go to the main menu if the user wishes
#restrictions: the uncommitted must exist in the data list,to return or continue running must be pressed only what appears on screen
#Description: verifies that the user typed is already stored in the insentivelist for the company once found displays the information of what was the rate and percentage will go to their respective salary

    identification = input("type the identification: ")
    fullName = input("type the full name: ")
    month= input("type the month: ")
    cont= 0
    x= True
    while cont < len(insentivelist):
        if insentivelist[cont]["FullName"] == fullName and insentivelist[cont]["identification"] == identification and insentivelist[cont]["month"]== month:
            x= False
            print("calification: ",insentivelist[cont]["calification"] )
            print("insentive: ",insentivelist[cont]["insentive"],"on gross earnings")
            if volver == "administrator":
                menuAdministrator(volver)
            else:
                employeeMenu(volver)
            break
        cont +=1

    if x == True:
        print("ERROR: the full name, identification or the month are not in list, please press (1) for try again or (2) for go to main menu")
        choise= input("option: ")
        if choise == "1":
            seeTheCalification(volver)
        elif choise == "2":
            if volver == "administrator":
                menuAdministrator(volver)
            else:
                employeeMenu(volver)
        else:
            print("ERROR: data is incorrect")
            seeTheCalification(volver)

def editOrDellinsentive():
#inputs:the answer option if the person have to do another calification or want to go to the main menu, the identification, full name of the worker. The month of the previous rate to be deleted or edited
#outputs: a note warning the user of a problem occurred in if necessary
#restrictions: the insentive of the employee have to exist in the program previously, the calification can't be more than 100 or less than 0
#Description: verified using the information requested that this is in insentivelist by means of route list once found makes the underlying transactions otherwise notifies the user of the possible error.
    choise= input("press one to erase or two to edit information: ")
    if choise== "1":
        identification = input("type the identification: ")
        fullName = input("type the full name: ")
        month= input("type the month: ")
        cont= 0
        entro= True
        while cont < len(insentivelist):
            if insentivelist[cont]["FullName"] == fullName and insentivelist[cont]["identification"] == identification and insentivelist[cont]["month"]== month:
                entro= False
                del insentivelist[cont]
                print(insentivelist)
                e="administrator"
                menuAdministrator(e)
            cont += 1
        if entro== True:
            print("the identification, full name or the month are not in list of information")
            choise= input("please press 1  for try again, or press 2 for go to menu: ")
            if choise == "1":
                editOrDellinsentive()
            if choise == "2":
                admin= 'administrator'
                menuAdministrator(admin)
            else:
                print("ERROR")
                editOrDellinsentive()

    elif choise == "2":
        identification = input("type the identification: ")
        fullName = input("type the full name: ")
        month= input("type the month")
        contad= 0
        x= False
        while contad < len(insentivelist):
            if insentivelist[contad]["FullName"] == fullName and insentivelist[contad]["identification"] == identification and insentivelist[contad]["month"]== month:
                x= True
                try:
                    calification= int(input("type the calification(0/100): "))
                    if calification < 0:
                        print("ERROR calification not exist")
                        w="administrator"
                        menuAdministrator(w)
                    if calification == 0 or calification <= 20:
                        insent= 0
                        insentivelist[contad]["insentive"]= insent
                        insentivelist[contad]["calification"]= calification
                        w= "administrator"
                        menuAdministrator(w)

                    if calification >20 and calification <= 40:
                        insent= 0.02
                        insentivelist[contad]["insentive"]= insent
                        insentivelist[contad]["calification"]= calification
                        w= "administrator"
                        menuAdministrator(w)

                    if calification > 40 and calification <= 60:
                        insent= 0.03
                        insentivelist[contad]["insentive"]= insent
                        insentivelist[contad]["calification"]= calification
                        w= "administrator"
                        menuAdministrator(w)

                    if calification > 60 and calification <= 80:
                        insent= 0.05
                        insentivelist[contad]["insentive"]= insent
                        insentivelist[contad]["month"]= month
                        insentivelist[contad]["calification"]= calification
                        w= "administrator"
                        menuAdministrator(w)

                    if calification > 80 and calification <= 100:
                        insent= 0.07
                        insentivelist[contad]["insentive"]= insent
                        insentivelist[contad]["calification"]= calification
                        w= "administrator"
                        menuAdministrator(w)
                    else:
                        print("ERROR calification not exist")
                        w="administrator"
                        menuAdministrator(w)
                except:
                    calification = str
                    print("ERROR, please try again")
                    editOrDellinsentive()
            contad += 1

        if x == False:
            print("ERROR: please try again")
            editOrDellinsentive()
    else:
        print("ERROR: what digit is not found in the list, please try again")
        editOrDellinsentive()

def contarEmpleados():
#inputs: required of the list "userList" for do his function
#outsputs: amount employees of the company
#Description: the funcyion is responsable to print the amount of employees of the company
    global usersList
    cantidad=len(usersList)
    print("The number of employees of the company are: ",cantidad)
    x= "administrator"
    menuAdministrator(x)


def cambiarEstado():
#inputs: required of the list "userList", ID of the employee, the state of the employee obtained by global an inputs
#outputs: successful modification desired state employee,error message if the established restrictions are not met
#restriction:Only you can type 1 or 2 and active or inactive with the same structure for program continuity, the employee must be in registrated in the company, the date to chance must be different to the original
#Description: the functionis responsable to chance the state of the employee that located in "usersList" (list of employees of the company) according to the person desires
    
    global  usersList
    cambio=input("1. Change the state employee 2. Other proccess: ")
    if cambio=="1":
        IDCambiarEstado=input("type the ID of the employee: ")
        cont=0
        while cont<len(usersList):
            if usersList[cont]["identification"]==IDCambiarEstado:
                hacercambio=input("type the state ")
                if hacercambio == "active" or hacercambio == "inactive":
                    if  usersList[cont]["state"]==hacercambio:
                        print("The data is the same")
                        cambiarEstado()
                    elif usersList[cont]["state"]!=hacercambio:
                        usersList[cont]["state"]=hacercambio
                        print("data changed successfully")
                        cambiarEstado()
                        break
                else:
                    print("ERROR try again")
                    cambiarEstado()
            else:
                cont=cont+1
        if cont==len(usersList):
            print("the employee is not found, enter the data again ")
            cambiarEstado()

    elif cambio=="2":
        admin= 'administrator'
        menuAdministrator(admin)
    else:
        print("Data input error")
        cambiarEstado()

def printAguinaldo(volver):
#inputs: ID of the employee, year of creation of bonus obtained by inputs and the name of the employee obtained by list traversal
#outputs: impression of the bonus list of the desired person,error message if the established restrictions are not met
#restriction:Only can type 1 or 2 for program continuity, the employee must be in registrated in the company, only can type 2015 for the year
#description: print the bonus for the year 2015 according to the person desires
    global listOfAguinaldo
    wantToprintAgui=input("1.want to print bonuses , 2.Other process: ")
    if wantToprintAgui=="1":
        if listOfAguinaldo!=[]:
            IDperson=input("type the identification: ")
            cont=0
            exist="no"
            while cont<len(listOfAguinaldo):
                if listOfAguinaldo[cont]["identification"]==IDperson:
                    exist="si"
                    break
                else:
                    cont=cont+1
            if exist=="no":
                print("ERROR: data not found")
                printAguinaldo(volver)
            elif exist=="si":
                yearToPrint=input("type the year: ")
                if yearToPrint=="2015":
                    cont=0
                    while cont<len(listOfAguinaldo):
                        if listOfAguinaldo[cont]["identification"]==IDperson:
                            a=listOfAguinaldo[cont]["FullName"]
                            print(listOfAguinaldo[cont])
                            print("report to: ", a)
                            printAguinaldo(volver)
                            break
                        else:
                            cont=cont+1

                else:
                    print("ERROR: try again")
                    printAguinaldo(volver)
        if listOfAguinaldo==[]:
            print("DATA is not performed")
            printAguinaldo(volver)

    elif wantToprintAgui=="2":
        if volver == "administrator":
            menuAdministrator(volver)
        else:
            employeeMenu(volver)

    else:
        print("ERROR: try again")
        printAguinaldo(volver)

def performBonuses():
#inputs:ID of the person and year,decision to operate (1 or 2), all type for the user, list of payroll created according the employee for obtained the necessary data to created bonus
#outputs: obtain the amount of bonus according to the employee, error message if the established restrictions are not met, saving the results in the established list
#restriction:Only can type 1 or 2 for program continuity, the employee must be registrated in the company, only can type 2015 for the year, the employee not must be registrated in listOfBonus (list of all the registrated bonus)
#description: creation of bonus according the person desired by mathematical calculations, besides the information storage
    global listOfAguinaldo
    global usersList
    global listOfplanilla
    wantToMakeBonuses=input("1.want to perform bonuses , 2.Other process: ")
    if wantToMakeBonuses=="1":
        if listOfplanilla!=[]:
            numID=input("typer the identification: ")
            cont=0
            exist="no"
            while cont<len(listOfplanilla):
                if listOfplanilla[cont]["identification"]==numID:
                    exist="si"
                    break
                else:
                    cont=cont+1

            if exist=="no":
                print("ERROR: try again")
                performBonuses()

            if exist=="si":
                yearAguinaldo=input("type the year: ")
                if yearAguinaldo=="2015":
                    conta=0
                    estaEnLista="no"
                    while conta<len(listOfAguinaldo):
                        if listOfAguinaldo[conta]["identification"]==numID:
                            estaEnLista="si"
                            break
                        else:
                            conta=conta+1
                              
                    if estaEnLista=="no":
                        SumGrossSalary=0
                        cont=0
                        while cont<len(listOfplanilla):
                            if listOfplanilla[cont]["identification"]==numID:
                                valuegrossSalary=int(listOfplanilla[cont]["grossSalary"])
                                SumGrossSalary=SumGrossSalary+valuegrossSalary
                                cont=cont+1
                                if cont==len(listOfplanilla):
                                    valueAguinaldo=SumGrossSalary/12
                                    break
                            else:
                                cont=cont+1

                        cont=0
                        while cont<len(usersList):
                            if usersList[cont]["identification"]==numID:
                                persoAguinaldo={}
                                a=usersList[cont]["FullName"]
                                b=usersList[cont]["identification"]
                                persoAguinaldo["identification"]=b
                                persoAguinaldo["FullName"]=a
                                persoAguinaldo["Aguinaldo"]=valueAguinaldo
                                persoAguinaldo["year"]="2015"
                                listOfAguinaldo.append(persoAguinaldo)
                                print("")
                                print("Bonus performed Successfully")
                                performBonuses()
                                break
                            else:
                                cont=cont+1          
                    else:
                        print("ERROR: data already exists")
                        performBonuses()

                else:
                    print("ERROR: data not found, try again")
                    performBonuses()
        else:
            print("ERROR: data not perform")
            performBonuses()
    if wantToMakeBonuses=="2":
        w= "administrator"
        menuAdministrator(w)
    if wantToMakeBonuses!="1" and wantToMakeBonuses!="2":
        print("ERROR: try again")
        performBonuses()

def printAmountHours():
#inputs: decision to operate (1 or 2), month and year to analize, all typed by inputs, list of payroll created according the employee for obtained the necessary data to print the information
#outputs: print the total amount of extra hours, regular hours and total hours according filters desired (year or month), error message if the established restrictions are not met
#restriction: only can type the month by numbers, Only can type 1 or 2 for program continuity, the month and year must be in registrated in the company, only can type 2015 for the year and for the month onlycan type values from 1 to 12
#description:print the total amount of extra hours,regular hours and total hours, by way from the list, obtained the amounts and do mathematical calculations(sum) to created the values
    global listOfplanilla           
    wantToprintAmount=input("1.prin amount by extra hours or regular  2.Other process: ")
    if  wantToprintAmount=="1":
        howPrint=input("1.by month 2.by year: ")
        if howPrint=="1":
            monthPrint=input("type the month: ")
            if monthPrint=="1" or monthPrint=="2" or monthPrint=="3" or monthPrint=="4" or monthPrint=="5" or monthPrint=="6" or monthPrint=="7" or monthPrint=="8" or monthPrint=="9" or monthPrint=="10" or monthPrint=="11" or monthPrint=="12":
                exist="no"
                cont=0
                while cont<len(listOfplanilla):
                    if listOfplanilla[cont]["month"] == monthPrint:
                        exist="si"
                        break
                    cont=cont+1
                if exist=="si":
                    sumExtraHours=0
                    SumRegularHours=0
                    SumSaryOrdinary=0
                    SumOvertimeSalary=0
                    cont=0
                    while cont<len(listOfplanilla):
                        if listOfplanilla[cont]["month"]==monthPrint:
                            valueOvertimeSalary=int(listOfplanilla[cont]["overtimeSalary"])
                            SumOvertimeSalary=SumOvertimeSalary+valueOvertimeSalary
                            valueSaryOrdinary=int(listOfplanilla[cont]["saryOrdinary"])
                            SumSaryOrdinary=SumSaryOrdinary+valueSaryOrdinary
                            valueExtraHours=int(listOfplanilla[cont]["extrahours"])
                            sumExtraHours=sumExtraHours+valueExtraHours
                            valueRegularHours=int(listOfplanilla[cont]["regularHours"])
                            SumRegularHours=SumRegularHours+valueRegularHours
                            cont=cont+1
                        else:
                            cont=cont+1

                    if cont==len(listOfplanilla):
                        print("")
                        print("total amount month: ")
                        print("")
                        diccImpresionMesTotal={}
                        diccImpresionMesTotal["saryOrdinary"]=SumSaryOrdinary
                        diccImpresionMesTotal["extrahours"]=sumExtraHours
                        diccImpresionMesTotal["regularHours"]=SumRegularHours
                        diccImpresionMesTotal["overtimeSalary"]=SumOvertimeSalary
                        diccImpresionMesTotal["month"]=monthPrint
                        print(diccImpresionMesTotal)
                        print("report to: ",monthPrint)
                        w= "administrator"
                        menuAdministrator(w)


                if exist=="no":
                    print("ERROR: month not found, type the mount by numbers")
                    printAmountHours()
            else:
                print("ERROR: try again")
                printAmountHours()

        elif howPrint=="2":
            yearToPrint=input("type the year: ")
            if yearToPrint=="2015":
                exist="no"
                cont=0
                while cont<len(listOfplanilla):
                    if listOfplanilla[cont]["year"] == yearToPrint:
                        exist="si"
                        break
                    cont=cont+1
                if exist=="si":

                    sumExtraHours=0
                    SumRegularHours=0
                    SumSaryOrdinary=0
                    SumOvertimeSalary=0
                    cont=0
                    while cont<len(listOfplanilla):
                        if listOfplanilla[cont]["year"]==yearToPrint:
                            valueOvertimeSalary=int(listOfplanilla[cont]["overtimeSalary"])
                            SumOvertimeSalary=SumOvertimeSalary+valueOvertimeSalary
                            valueSaryOrdinary=int(listOfplanilla[cont]["saryOrdinary"])
                            SumSaryOrdinary=SumSaryOrdinary+valueSaryOrdinary
                            valueExtraHours=int(listOfplanilla[cont]["extrahours"])
                            sumExtraHours=sumExtraHours+valueExtraHours
                            valueRegularHours=int(listOfplanilla[cont]["regularHours"])
                            SumRegularHours=SumRegularHours+valueRegularHours
                            cont=cont+1
                        else:
                            cont=cont+1

                    sumAmount=SumOvertimeSalary+SumSaryOrdinary
                    sumHours=sumExtraHours+SumRegularHours
                    if cont==len(listOfplanilla):
                        print("")
                        print("total amount year: ")
                        print("")
                        diccImpresionAñoTotal={}
                        diccImpresionAñoTotal["saryOrdinary"]=SumSaryOrdinary
                        diccImpresionAñoTotal["overtimeSalary"]=SumOvertimeSalary
                        diccImpresionAñoTotal["extrahours"]=sumExtraHours
                        diccImpresionAñoTotal["regularHours"]=SumRegularHours
                        diccImpresionAñoTotal["year"]=yearToPrint
                        diccImpresionAñoTotal["total amount"]=sumAmount
                        diccImpresionAñoTotal["total Hours"]=sumHours
                        print(diccImpresionAñoTotal)
                        print("")
                        print("report to: ",yearToPrint, "TOTAL amount:", sumAmount)
                        w= "administrator"
                        menuAdministrator(w)
                if exist=="no":
                    print("ERROR: year not found")
                    printAmountHours()
            else:
                print("ERROR: try again")
                printAmountHours()
        else:
            print("data error")
            printAmountHours()
    elif wantToprintAmount=="2":
        W= "administrator"
        menuAdministrator(W)

    else:
        print("ERROR: try again")
        printAmountHours()

def sumAguinaldo():
#inputs: is necessary the year,decision to operate (1 or 2),list of payroll created according the employee for obtained the necessary data to print the information
#outputs:print the total amount of bonus, error message if the established restrictions are not met
#restriction: Only can type 1 or 2 for program continuity,the year must be in registrated in the company and can be 2015, must be registrated information in listofAguinaldo (list of all the bonus)
#description: print the total amount of bonus according the year, sum each valueand obtain the total result,
    
    global listOfAguinaldo
    printTotalAgui=input("1.print Total Bonus 2.other process: ")

    if printTotalAgui== "1":
        yearToPrint=input("type the year to print: ")
        if yearToPrint=="2015":
            if listOfAguinaldo!=[]:
                TotalAguinaldo=0
                cont=0
                while cont<len(listOfAguinaldo):
                    if listOfAguinaldo[cont]["year"]==yearToPrint:
                        SumAguinaldo=int(listOfAguinaldo[cont]["Aguinaldo"])
                        TotalAguinaldo=TotalAguinaldo+SumAguinaldo
                        cont=cont+1
                    else:
                        cont=cont+1
                if cont==len(listOfAguinaldo):
                    dicciTotalAguinaldo={}
                    dicciTotalAguinaldo["year"]="2015"
                    dicciTotalAguinaldo["Total Aguinaldo"]=TotalAguinaldo
                    print(dicciTotalAguinaldo)
                    print("")
                    print("report to year: 2015")
                    sumAguinaldo()   
                    
            elif listOfAguinaldo==[]:
                print("ERROR: not exist the data")
                sumAguinaldo()

        elif yearToPrint!="2015":
            print("ERROR: try again")
            sumAguinaldo()

    elif printTotalAgui=="2":
        w="administrator"
        menuAdministrator(w)
        
    else:
        print("ERROR: try again")
        sumAguinaldo()

def imprimirPlanilla(valor):
#inputs: ID of the person, decision to operate (1 or 2), month and year to analize, list of payroll created according the employee for obtained the necessary data to print the information
#outputs: print the total amount of planilla by filters (month or year), error message if the established restrictions are not met
#restriction:only can type the month by numbers, Only can type 1 or 2 for program continuity, the month and year must be in registrated in the company, only can type 2015 for the year and for the month only can type values from 1 to 12
#description: print the total amount of planilla in relation to only the employee type (ID) by month or year, by way from the list obtained the amounts and do mathematical calculations(sum) to created the values

    global listOfplanilla       
    deseaImprimirPlanilla=input("1.wish to print payroll 2.Other process: ")
    if deseaImprimirPlanilla=="1":
        comoImprime=input("1.by month 2.by year: ")
        empleadoImprimirPla=input("Type the ID: ")

        if comoImprime=="1":
            mesImpri=input("type the month: ")
            if mesImpri=="1" or mesImpri=="2" or mesImpri=="3" or mesImpri=="4" or mesImpri=="5" or mesImpri=="6" or mesImpri=="7" or mesImpri=="8" or mesImpri=="9" or mesImpri=="10" or mesImpri=="11" or mesImpri=="12":
                cont=0
                while cont<len(listOfplanilla):
                    if listOfplanilla[cont]["identification"]==empleadoImprimirPla:
                        if listOfplanilla[cont]["month"]==mesImpri:
                            print("***********************************")
                            print("the payroll by month is the next")
                            print(listOfplanilla[cont])
                            a=listOfplanilla[cont]["FullName"]
                            print("")
                            print("report of: ",a)
                            print("***********************************")
                            imprimirPlanilla(valor)
                            break
                        else:
                            cont=cont+1
                    else:
                        cont=cont+1
                if cont==len(listOfplanilla):
                    print("ERROR: check {{'identification' , 'permissions' , 'month payroll performed'}}")
                    imprimirPlanilla(valor)
            else:
                print("ERROR: try again")
                imprimirPlanilla(valor)
        elif comoImprime=="2":
            añoImpre=input("type the year: ")
            if añoImpre=="2015":
                cont=0
                existe="no"
                while cont<len(listOfplanilla):
                    if listOfplanilla[cont]["identification"]==empleadoImprimirPla:
                        nombreEmployee=listOfplanilla[cont]["FullName"]
                        existe="si"
                        break
                    else:
                        cont=cont+1
                if existe=="no":
                    print("ERROR: employee not found")
                    imprimirPlanilla(valor)
                elif existe=="si":
                    cont=0
                    SumaOrdina=0
                    SumaDeduc=0
                    SumaNetEarnings=0
                    SumagrossSalary=0
                    while cont<len(listOfplanilla):
                        if listOfplanilla[cont]["identification"]==empleadoImprimirPla:
                            valorOrdinario=int(listOfplanilla[cont]["saryOrdinary"])
                            SumaOrdina=SumaOrdina+valorOrdinario
                            valorDeduc=int(listOfplanilla[cont]["deductions"])
                            SumaDeduc=SumaDeduc+valorDeduc
                            valorNetEarnings=int(listOfplanilla[cont]["netEarnings"])
                            SumaNetEarnings=SumaNetEarnings+valorNetEarnings
                            valorgrossSalary=int(listOfplanilla[cont]["grossSalary"])
                            SumagrossSalary=SumagrossSalary+valorgrossSalary
                            cont=cont+1
                        else:
                            cont=cont+1
                    if cont==len(listOfplanilla):
                        print("pyroll by year: ")
                        print("")
                        diccImpresionAño={}
                        diccImpresionAño["saryOrdinary"]=SumaOrdina
                        diccImpresionAño["deductions"]=SumaDeduc
                        diccImpresionAño["netEarnings"]=valorNetEarnings
                        diccImpresionAño["grossSalary"]=SumagrossSalary
                        diccImpresionAño["identification"]=empleadoImprimirPla
                        diccImpresionAño["FullName"]=nombreEmployee
                        print(diccImpresionAño)
                        print("report to: ",nombreEmployee)
                        imprimirPlanilla(valor)

            else:
                print("ERROR 'Year': try again")
                imprimirPlanilla(valor)
        else:
            print("data error")
            imprimirPlanilla(valor)
    elif deseaImprimirPlanilla=="2":
        if valor == "administrator":
            menuAdministrator(valor)
        else:
            employeeMenu(valor)

    else:
        print("Data error")
        imprimirPlanilla(valor)

def imprimirInfoVacaciones(valor):
#inputs: ID of the person, decision to operate {by input}-->(1 or 2), obtainment of fullName by way from the list
#outputs: print the information about vacations according the desicion desire
#restriction:Only can type 1 or 2 for program continuity, the ID must be in the userList (list of all the employee),
#description: print the inform of vacations according the ID obtained by input, following the list and obtained the information necessary to complete the fuction 

    global infVacaEmpleados 
    deseaImpriVacaciones=input("1.wish to print informacion about vacations 2.Other process: ")
    if deseaImpriVacaciones=="1":
        if infVacaEmpleados!=[]:
            existe="no"
            IDEmpleImpriVaca=input("Type the ID of the employee: ")
            cont=0
            while cont<len(infVacaEmpleados):
                if infVacaEmpleados[cont]["identification"]==IDEmpleImpriVaca:
                    existe="si"
                    break
                else:
                    cont=cont+1
            if existe=="si":
                print("***************************************")
                print(infVacaEmpleados[cont])
                a=infVacaEmpleados[cont]["FullName"]
                print("")
                print("informe de: ",a)
                print("***************************************")
                imprimirInfoVacaciones(valor)
                
            elif existe=="no":
                print("name not found, not exist inform")
                imprimirInfoVacaciones(valor)

        elif infVacaEmpleados==[]:
            print("not exist inform")
            imprimirInfoVacaciones(valor)

    if deseaImpriVacaciones=="2":
        if valor == "administrator":
            menuAdministrator(valor)
        else:
            employeeMenu(valor)
    else:
        print("data error")
        imprimirInfoVacaciones(valor)

def imprimirPlanillaTotal():
#inputs: decision to operate {by input}-->(1 or 2),obtainment of the month and year, obtainment of values of the variables: SumaOrdina,SumaDeduc,valorNetEarnings,SumagrossSalary by way from the list
#outputs:print the information about payroll according the desicion desire, by filters and the employee
#restriction:only can type the month by numbers, Only can type 1 or 2 for program continuity, the month and year must be in registrated in the company, only can type 2015 for the year and for the month only can type values from 1 to 12
#description:print the total amount of planilla by month or year, by way from the list obtained the amounts and do mathematical calculations(sum) to created the values

    global listOfplanilla       
    deseaImprimirPlanilla=input("1.wish to print payroll total 2.Other process: ")
    if deseaImprimirPlanilla=="1":
        comoImprime=input("1.by month 2.by year: ")
        if comoImprime=="1":
            mesImpri=input("type the month: ")
            if mesImpri=="1" or mesImpri=="2" or mesImpri=="3" or mesImpri=="4" or mesImpri=="5" or mesImpri=="6" or mesImpri=="7" or mesImpri=="8" or mesImpri=="9" or mesImpri=="10" or mesImpri=="11" or mesImpri=="12":
                existe="no"
                cont=0
                while cont<len(listOfplanilla):
                    if listOfplanilla[cont]["month"] == mesImpri:
                        existe="si"
                        break
                    cont=cont+1
                if existe=="si":

                    SumaOrdina=0
                    SumaDeduc=0
                    SumaNetEarnings=0
                    SumagrossSalary=0
                    cont=0
                    while cont<len(listOfplanilla):
                        if listOfplanilla[cont]["month"]==mesImpri:
                            valorOrdinario=int(listOfplanilla[cont]["saryOrdinary"])
                            SumaOrdina=SumaOrdina+valorOrdinario
                            valorDeduc=int(listOfplanilla[cont]["deductions"])
                            SumaDeduc=SumaDeduc+valorDeduc
                            valorNetEarnings=int(listOfplanilla[cont]["netEarnings"])
                            SumaNetEarnings=SumaNetEarnings+valorNetEarnings
                            valorgrossSalary=int(listOfplanilla[cont]["grossSalary"])
                            SumagrossSalary=SumagrossSalary+valorgrossSalary
                            cont=cont+1
                        else:
                            cont=cont+1
                    if cont==len(listOfplanilla):
                        print("")
                        print("pyroll total month: ")
                        print("")
                        diccImpresionMesTotal={}
                        diccImpresionMesTotal["saryOrdinary"]=SumaOrdina
                        diccImpresionMesTotal["deductions"]=SumaDeduc
                        diccImpresionMesTotal["netEarnings"]=valorNetEarnings
                        diccImpresionMesTotal["grossSalary"]=SumagrossSalary
                        diccImpresionMesTotal["month"]=mesImpri
                        print(diccImpresionMesTotal)
                        print("report to: ",mesImpri)
                        w= "administrtor"
                        menuAdministrator(w)
                if existe=="no":
                    print("ERROR: month not found")
                    imprimirPlanillaTotal()
            else:
                print("ERROR: try again")
                imprimirPlanillaTotal()

        elif comoImprime=="2":
            añoImpre=input("type the year: ")
            if añoImpre=="2015":
                existe="no"
                cont=0
                while cont<len(listOfplanilla):
                    if listOfplanilla[cont]["year"] == añoImpre:
                        existe="si"
                        break
                    cont=cont+1
                if existe=="si":

                    SumaOrdina=0
                    SumaDeduc=0
                    SumaNetEarnings=0
                    SumagrossSalary=0
                    cont=0
                    while cont<len(listOfplanilla):
                        if listOfplanilla[cont]["year"]==añoImpre:
                            valorOrdinario=int(listOfplanilla[cont]["saryOrdinary"])
                            SumaOrdina=SumaOrdina+valorOrdinario
                            valorDeduc=int(listOfplanilla[cont]["deductions"])
                            SumaDeduc=SumaDeduc+valorDeduc
                            valorNetEarnings=int(listOfplanilla[cont]["netEarnings"])
                            SumaNetEarnings=SumaNetEarnings+valorNetEarnings
                            valorgrossSalary=int(listOfplanilla[cont]["grossSalary"])
                            SumagrossSalary=SumagrossSalary+valorgrossSalary
                            cont=cont+1
                        else:
                            cont=cont+1
                    sumatoriaMontos=SumagrossSalary+SumaNetEarnings+SumaDeduc+SumaOrdina
                    if cont==len(listOfplanilla):
                        print("")
                        print("pyroll total year: ")
                        print("")
                        diccImpresionAñoTotal={}
                        diccImpresionAñoTotal["saryOrdinary"]=SumaOrdina
                        diccImpresionAñoTotal["deductions"]=SumaDeduc
                        diccImpresionAñoTotal["netEarnings"]=valorNetEarnings
                        diccImpresionAñoTotal["grossSalary"]=SumagrossSalary
                        diccImpresionAñoTotal["year"]=añoImpre
                        diccImpresionAñoTotal["TOTAL"]=sumatoriaMontos
                        print(diccImpresionAñoTotal)
                        print("")

                        print("report to: ",añoImpre, "TOTAL pyroll:", sumatoriaMontos)
                        w="administrator"
                        menuAdministrator(w)

                if existe=="no":
                    print("ERROR: month not found")
                    imprimirPlanillaTotal()
            else:
                print("ERROR: try again")
                imprimirPlanillaTotal()

        else:
            print("data error")
            imprimirPlanillaTotal()
    elif deseaImprimirPlanilla=="2":
        w= "administrator"
        menuAdministrator(w)

    else:
        print("ERROR: try again")
        imprimirPlanillaTotal()


def registrarEmpleado(obtencionDiasSolicitados,a,b,c,diferencia):
#inputs: parameters obtained from the function 'aceptarORechazar'-->(obtencionDiasSolicitados,a,b,c,diferencia), obtainment of the value of the variables: totalDiasSol, diasDisponibles, diasVacaciones , Answer of the request obtain by input
#outputs: obtain if the person have days of vacations, obtain the lists of information about vacations and puting into a global list, print error message if the established restrictions are not met
#restriction: 
#description: send the answer of the employee request to the list of answer for the employee sees, create the informationabout vacation in a global lists, for obtaining data later if required for other methods
    
    global SolicitudAdmi
    global usersList
    global infVacaEmpleados
    if diferencia>=30:
        if diferencia>=30 and diferencia<60:
            totalDiasSoli=0 
            diasVacaciones=1  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+obtencionDiasSolicitados
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-obtencionDiasSolicitados
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif obtencionDiasSolicitados>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=1
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b:
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=60 and diferencia<90:
            totalDiasSoli=0 
            diasVacaciones=2  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")
                
                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=2
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=90 and diferencia<120:
            totalDiasSoli=0 
            diasVacaciones=3  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=3
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont] 
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=120 and diferencia<150:
            totalDiasSoli=0 
            diasVacaciones=4  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=4
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")
                
                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=150 and diferencia<180:
            totalDiasSoli=0 
            diasVacaciones=5  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont] 
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=5
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=180 and diferencia<210:
            totalDiasSoli=0 
            diasVacaciones=6  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=6
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont] 
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=210 and diferencia<240:
            totalDiasSoli=0 
            diasVacaciones=7  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=7
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=240 and diferencia<270:
            totalDiasSoli=0 
            diasVacaciones=8  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont] 
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=8
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b:
                        del solicitudAdmi[cont] 
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=270 and diferencia<300:
            totalDiasSoli=0 
            diasVacaciones=9  
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=9
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]
                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=300 and diferencia<330:
            totalDiasSoli=0 
            diasVacaciones=10
            diasDisponibles=diasVacaciones-totalDiasSoli  

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):  
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont]  
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=10
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b: 
                        del solicitudAdmi[cont] 

                        aceptarORechazar()
                    else:
                        cont=cont+1

        elif diferencia>=330 and diferencia<360:
            totalDiasSoli=0
            diasVacaciones=11
            diasDisponibles=diasVacaciones-totalDiasSoli

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b:
                        del solicitudAdmi[cont]
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=11
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")
                
                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b:
                        del solicitudAdmi[cont]
                        aceptarORechazar()
                    else:
                        cont=cont+1


        elif diferencia>=360 and diferencia<390:
            totalDiasSoli=0
            diasVacaciones=12
            diasDisponibles=diasVacaciones-totalDiasSoli

            if  int(obtencionDiasSolicitados)<=diasDisponibles:
                totalDiasSoli=totalDiasSoli+int(obtencionDiasSolicitados)
                diasDisponibles=diasVacaciones-totalDiasSoli
                diasVacaciones=diasVacaciones-int(obtencionDiasSolicitados)
                print("employee has vacations")
                respuEnvio=input("type the answer to send: ")

                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=totalDiasSoli
                infEmpleadoDicci["Dias Disponibles"]=diasDisponibles
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")

                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b:
                        del solicitudAdmi[cont]
                        aceptarORechazar()
                    else:
                        cont=cont+1

            elif int(obtencionDiasSolicitados)>diasDisponibles:
                print("employee over vacation days")
                respuEnvio=input("type the answer to send: ")
                empleDicciSoli={}
                empleDicciSoli["FullName"]=a
                empleDicciSoli["identification"]=b
                empleDicciSoli["Dias Solicitados"]=c
                empleDicciSoli["Respuesta"]=respuEnvio
                respSolicitud.append(empleDicciSoli)

                infEmpleadoDicci={}
                infEmpleadoDicci["FullName"]=a
                infEmpleadoDicci["identification"]=b
                infEmpleadoDicci["Dias Totales Solicitados"]=0
                infEmpleadoDicci["Dias Disponibles"]=12
                infVacaEmpleados.append(infEmpleadoDicci)

                print("Answer Sent")
                
                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==b:
                        del solicitudAdmi[cont]
                        aceptarORechazar()
                    else:
                        cont=cont+1

        else:
            print("error data, type again")

    elif diferencia<30:
        print("employee haven't days")
        respuEnvio=input("type the answer to send: ")
        empleDicciSoli={}
        empleDicciSoli["FullName"]=a
        empleDicciSoli["identification"]=b
        empleDicciSoli["Dias Solicitados"]=c
        empleDicciSoli["Respuesta"]=respuEnvio
        respSolicitud.append(empleDicciSoli)

        infEmpleadoDicci={}
        infEmpleadoDicci["FullName"]=a
        infEmpleadoDicci["identification"]=b
        infEmpleadoDicci["Dias Totales Solicitados"]=0
        infEmpleadoDicci["Dias Disponibles"]=0
        infVacaEmpleados.append(infEmpleadoDicci)

        print("Answer Sent")

        cont=0
        while cont<len(solicitudAdmi):
            if solicitudAdmi[cont]["identification"]==b:
                del solicitudAdmi[cont]
                aceptarORechazar()
            else:
                cont=cont+1

def continuarEvaluacionFechaAño(obtencioDatoFechaFinal, prinCont):
#program inputs: the date income of the worker(obtencioDatoFechaFinal), a special program summation(prinCont)
#program outputs: return "0" or "1", if the validation is correct return=="0" else return=="1"
#restrictions: have a correct format,  have to be only 2015, only numbers
#Description: the program evaluates if the entered year is 2015,To accomplish this the program evaluates the positions of the user typed whith the prinCont(special program summation)
  
    if obtencioDatoFechaFinal[prinCont] == "/":
        prinCont += 1
        if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 2:
            prinCont += 1
            if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 0:
                prinCont += 1
                if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 1:
                    prinCont += 1
                    if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) == 5:
                        prinCont += 1
                        return 0
                    else:
                        return 1
                else:
                    return 1
            else:
                return 1
        else:
            return 1
    else:
        return 1

def continuarEvaluacionFechaMes(obtencioDatoFechaFinal, prinCont):
#program inputs: the date income of the worker, a special program summation(prinCont)
#program outputs:return "0" or "1", if the validation is correct return=="0" else return=="1"
#restrictions: have the correct format , only numbers, cant to be more than 12
#Description: the program evaluates if the entered date is in the correct format and cant to be more than 12,To accomplish this the program evaluates the positions of the user typed whith the prinCont(special program summation)
    
    if obtencioDatoFechaFinal[prinCont] == "/":
        prinCont += 1
        if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) < 2:
            prinCont += 1
            if obtencioDatoFechaFinal[prinCont -1] == "0" and int(obtencioDatoFechaFinal[prinCont]) > 0 and int(obtencioDatoFechaFinal[prinCont]) <= 9:
                prinCont += 1
                prueba = continuarEvaluacionFechaAño(obtencioDatoFechaFinal, prinCont)
                if prueba == 1:
                    return 1
                else:
                    return 0
            elif obtencioDatoFechaFinal[prinCont -1] == "1" and int(obtencioDatoFechaFinal[prinCont]) <= 2:
                prinCont += 1
                prueba = continuarEvaluacionFechaAño(obtencioDatoFechaFinal, prinCont)
                if prueba == 1:
                    return 1
                else:
                    return 0

            else:
                return 1
        else:
            return 1
    else:
        return 1


def evaluarRestriccionFechaIngresada(obtencioDatoFechaFinal, obtencioDatoDateincome):
    
#inputs: parameters of the variables:obtencioDatoFechaFinal, obtencioDatoDateincome(obtain in other function)
#outputs: return one or two (one: not meets restrictions), (two: meets restrictions),error message if the established restrictions are not met
#restriction:Fingered date can not be in a period of time prior to the date of commencement of work
#description: verification constraint, if meet requirements will return "0" else will return "1", (restriction: variable obtencioDatoFechaFinal not be before of obtencioDatoDateincome)

    if int(obtencioDatoFechaFinal[3]) == int(obtencioDatoDateincome[3]) and int(obtencioDatoFechaFinal[4]) == int(obtencioDatoDateincome[4]):
        if int(obtencioDatoFechaFinal[0]) == int(obtencioDatoDateincome[0]) and int(obtencioDatoFechaFinal[1]) > int(obtencioDatoDateincome[1]):
            return 0

        elif int(obtencioDatoFechaFinal[0]) > int(obtencioDatoDateincome[0]):
            return 0
        elif int(obtencioDatoFechaFinal[0]) == int(obtencioDatoDateincome[0]) and int(obtencioDatoFechaFinal[1]) == int(obtencioDatoDateincome[1]):
            return 0
        else:
            return 1

    elif int(obtencioDatoFechaFinal[3]) == int(obtencioDatoDateincome[3]) and int(obtencioDatoFechaFinal[4]) < int(obtencioDatoDateincome[4]):
        return 1

    elif int(obtencioDatoFechaFinal[3]) < int(obtencioDatoDateincome[3]):
        return 1
    else:
        return 0


def obtenerDiferencia(obtencioDatoFechaFinal, obtencioDatoDateincome):
    
#inputs: parameters of the variables:obtencioDatoFechaFinal, obtencioDatoDateincome(obtain in other function)
#outputs: return the diference between the two dates, sending the value for parameters
#restriction:
#description: the function is responsible for performing the diferences between the two dates, sending for parameters and continue the method

    from datetime import datetime,date
    formato_fecha = "%d/%m/%Y"
    fecha_inicial = datetime.strptime(obtencioDatoDateincome, formato_fecha)
    fecha_final = datetime.strptime(obtencioDatoFechaFinal, formato_fecha)
    diferencia = fecha_final - fecha_inicial
    numero=diferencia.days
    int(numero)
    return numero


def aceptarORechazar():
#inputs: decision to operate (1 or 2), ID of the employee, list of userList created according the employee for obtained the necessary data to print the information, obtainment of arrive date for the obtainment of the diference betweeen the two dates, value of variable 'prueba' and numero result of the validation of the date
#outputs: message for complete process,error message if the established restrictions are not met,obtainment of variable 'numero'==diference(send to the function to register employee in list of vacations), modification of the values inside the list of information about vacations,
#restriction: Only can type 1 or 2 for program continuity,if the list of information about vacation is empy go to the fuction register, if the list of information about vacation is diferente of emply but the employee is not found go to the function register, if the list of information about vacation is diferente and the employee is found in this only needmodificatetheinformation existing
#description: the fuction check if the person to accept or reject exist in list, if no exist: the person must be register through check of the arrive date (validation of the date{past functions})and the calculation of mathematical calculations recording all in list, if theperson exist only replace the old information andthe new, addition in each case the anwer of the request issend to the employee
    
    global SolicitudAdmi
    global lista
    global infVacaEmpleados
    deseaRyA=input("1.to accept or reject vacation requests 2.Other process: ")
    if deseaRyA == '':
        print("There was an error, please try again")
        aceptarORechazar()
    if deseaRyA=="1":
        if solicitudAdmi!=[]:
            impListaSoli=input("1.print request list 2.Other process: ")
            if impListaSoli == '':
                print("There was an error, please try again")
                aceptarORechazar()
            if impListaSoli=="1":
                print(solicitudAdmi)
                IDEmpleadoResp=input("Type the identification of the employee to respond: ")
                if IDEmpleadoResp == '':
                    print("There was an error, please try again")
                    aceptarORechazar()
                cont=0
                while cont<len(solicitudAdmi):
                    if solicitudAdmi[cont]["identification"]==IDEmpleadoResp:
                        a=solicitudAdmi[cont]["FullName"]
                        b=solicitudAdmi[cont]["identification"]
                        c=solicitudAdmi[cont]["Dias Solicitados"]

                        obtencionDiasSolicitados=int(solicitudAdmi[cont]["Dias Solicitados"])
                        break
                    else:
                        cont=cont+1

                if cont==len(solicitudAdmi):
                    print("data no found, type again")
                    aceptarORechazar()
                cont=0
                while cont<len(usersList):
                    if usersList[cont]["identification"]==IDEmpleadoResp:
                        
                        existe = "no"
                        if infVacaEmpleados == []:
                            break
                        else:

                            contAux=0
                            while contAux<len(infVacaEmpleados):
                                if infVacaEmpleados[contAux]["identification"]==IDEmpleadoResp:
                                    existe = "si"
                                    break
                                else:
                                    contAux=contAux+1

                            if existe != "si":


                                obtencioDatoDateincome=usersList[cont]["dateIncome"]
                                obtencioDatoFechaFinal=input("Type the arrive date dd/mm/aaaa : ")
                                if obtencioDatoFechaFinal == '':
                                    print("Date format error, please try again")
                                    aceptarORechazar()

                                contadorSec = 0
                                prinCont = 0
                                for element in obtencioDatoFechaFinal:
                                    contadorSec += 1

                                if contadorSec > 10:
                                    print("Date format error, please try again")
                                    aceptarORechazar()
                                else:
                                    while prinCont < contadorSec:

                                        if obtencioDatoFechaFinal[prinCont].isdigit() and int(obtencioDatoFechaFinal[prinCont]) <= 3:
                                            prinCont += 1

                                            if obtencioDatoFechaFinal[prinCont -1] == 3:

                                                if obtencioDatoFechaFinal[prinCont] > 1:
                                                    print("Date format error, please try again")
                                                    aceptarORechazar()
                                                else:
                                                    prinCont += 1
                                                    prueba = continuarEvaluacionFechaMes(obtencioDatoFechaFinal, prinCont)
                                                    if prueba == 1:
                                                        print("Date format error, please try again")
                                                        aceptarORechazar()
                                                    else:
                                                        terminarPrueba = evaluarRestriccionFechaIngresada(obtencioDatoFechaFinal, obtencioDatoDateincome)
                                                        if terminarPrueba == 1:
                                                            print("Date format error, please try again")
                                                            aceptarORechazar()
                                                        else:
                                                            try:
                                                                numero=obtenerDiferencia(obtencioDatoFechaFinal, obtencioDatoDateincome)
                                                                break
                                                            except ValueError:
                                                                print("Day is out of range for month")
                                                                numero = "no"
                                                                break


                                            else:
                                                prinCont += 1
                                                prueba = continuarEvaluacionFechaMes(obtencioDatoFechaFinal, prinCont)
                                                if prueba == 1:
                                                    print("Date format error, please try againf")
                                                    aceptarORechazar()
                                                else:
                                                    terminarPrueba = evaluarRestriccionFechaIngresada(obtencioDatoFechaFinal, obtencioDatoDateincome)
                                                    if terminarPrueba == 1:
                                                        print("Date format error, please try againg")
                                                        aceptarORechazar()
                                                    else:
                                                        try:
                                                            numero=obtenerDiferencia(obtencioDatoFechaFinal, obtencioDatoDateincome)
                                                            break
                                                        except ValueError:
                                                            print("Day is out of range for month")
                                                            numero = "no"
                                                            break
                                        else:
                                            print("Date format error, please try againh")
                                            aceptarORechazar()
                                    break
                            else:
                                break
                    else:
                        cont=cont+1



                if cont==len(usersList):
                    print("ERROR: employee not found")
                    aceptarORechazar()

                elif infVacaEmpleados!=[]:

                    if existe=="si":
                        cont=0
                        while cont<len(infVacaEmpleados):
                            if infVacaEmpleados[cont]["identification"]==IDEmpleadoResp:
                                datoDiasInforme=int(infVacaEmpleados[cont]["Dias Disponibles"])
                                datoDiasSoliInf=int(infVacaEmpleados[cont]["Dias Totales Solicitados"])
                                break
                            cont=cont+1

                        if int(obtencionDiasSolicitados)<=datoDiasInforme:
                            print("employee has vacations")
                            respuEnvio=input("type the answer to send: ")
                            empleDicciSoli={}
                            empleDicciSoli["FullName"]=a
                            empleDicciSoli["identification"]=b
                            empleDicciSoli["Dias Solicitados"]=c
                            empleDicciSoli["Respuesta"]=respuEnvio
                            respSolicitud.append(empleDicciSoli)

                            print(empleDicciSoli)

                            restaDias=datoDiasInforme-int(obtencionDiasSolicitados)
                            infVacaEmpleados[cont]["Dias Disponibles"]=restaDias
                            datoDiasSoli=datoDiasSoliInf
                            sumaDiasSoli= int(datoDiasSoli)+int(obtencionDiasSolicitados)
                            infVacaEmpleados[cont]["Dias Totales Solicitados"]= sumaDiasSoli

                            print("Answer Sent")

                            cont=0
                            while cont<len(solicitudAdmi):
                                if solicitudAdmi[cont]["identification"]==b:
                                    del solicitudAdmi[cont]
                                    aceptarORechazar()
                                else:
                                    cont=cont+1

                        else:
                            print("employee over vacation days")
                            respuEnvio=input("type the answer to send: ")
                            empleDicciSoli={}
                            empleDicciSoli["FullName"]=a
                            empleDicciSoli["identification"]=b
                            empleDicciSoli["Dias Solicitados"]=c
                            empleDicciSoli["Respuesta"]=respuEnvio
                            respSolicitud.append(empleDicciSoli)

                            print("Answer Sent")

                            cont=0
                            while cont<len(solicitudAdmi):
                                if solicitudAdmi[cont]["identification"]==b:
                                    del solicitudAdmi[cont]
                                    aceptarORechazar()
                                else:
                                    cont=cont+1

                    elif existe=="no":
                        if(numero != "no"):
                            registrarEmpleado(obtencionDiasSolicitados,a,b,c,numero)
                            
                        else:
                            aceptarORechazar()

                elif infVacaEmpleados==[]:
                    if(numero != "no"):
                        registrarEmpleado(obtencionDiasSolicitados,a,b,c,numero)
                        
                    else:
                        aceptarORechazar()

            elif impListaSoli=="2":
                m= "administrator"
                menuAdministrator(m)
                
            else:
                print("Data error")
                aceptarORechazar()
                
        elif solicitudAdmi==[]:
            print("no pending requests")
            aceptarORechazar()
            
    elif deseaRyA=="2":
        m= "administrator"
        menuAdministrator(m)

    else:
        print("ERROR: try again")
        aceptarORechazar()


def solicitarVacaciones():
#inputs: decision to operate (1 or 2),ID of the employee, FullName of the employee, desired days for holidays,list of respSolicitud or solicitudAdmi  or usersList created according the employee for obtained the necessary data to print the information
#outputs: ,Only you can type 1 or 2, error message if the established restrictions are not met, message when the process was completed successfully
#restriction: the days introduced must be greater than zero, if the employee must be request in the 'solicitudAdmi' (list of all the request)can not request again  until the request have answer
#description: the function recive values introduced by input, and analize if are correct, next introduce the data in a global list for the administrador can see and accept or reject the request
    
    conjunto={}
    global respSolicitud
    global solicitudAdmi
    global usersList
    deseaSolicitar=input("1.like to request holidays 2.Other process: ")
    if deseaSolicitar=="1":
        nombreSolicitante=input("type your FullName: ")
        IDSolicitante=input("Type your identification: ")
        cont=0
        while cont<len(usersList):
            if usersList[cont]["identification"]==IDSolicitante:
                cantidadDias=input("type the days ")
                if int(cantidadDias)>0:
                    if solicitudAdmi!=[]:
                        cont=0
                        existe="no"
                        while cont<len(solicitudAdmi):
                            if solicitudAdmi[cont]["identification"]==IDSolicitante:
                                existe="si"
                                break
                            else:
                                cont=cont+1

                        if existe=="no":
                            conjunto["FullName"]=nombreSolicitante
                            conjunto["identification"]=IDSolicitante
                            conjunto["Dias Solicitados"]=cantidadDias
                            solicitudAdmi.append(conjunto)
                            print("Request Sent Successfully")
                            print("")
                            solicitarVacaciones()

                        elif existe=="si":
                            print("ERROR: applications already exist in the system, wait for answer")
                            solicitarVacaciones()
                    else:
                        conjunto["FullName"]=nombreSolicitante
                        conjunto["identification"]=IDSolicitante
                        conjunto["Dias Solicitados"]=cantidadDias
                        solicitudAdmi.append(conjunto)
                        print("Request Sent Successfully")
                        print("")
                        solicitarVacaciones()
                else:
                    print("data error ")
                    solicitarVacaciones()
            else:
                cont=cont+1
        if cont==len(usersList):
            print("the name doesn't exist in the system, enter the data again ")
            solicitarVacaciones()

    elif deseaSolicitar=="2":
        m= "employee"
        employeeMenu(m)
    else:
        print("data error ")
        solicitarVacaciones()


def verRespuestaSolicitud():
#inputs:  decision to operate (1 or 2), ID of the employee obtained by input,list of answer request created according the employee for obtained the necessary data to print the information
#outputs: print of the answer according the employee
#restriction:Only can type 1 or 2, the employee must be in registrated in the company and registrated in "respSolicitud" (answer of the request)
#description: print of the answer of the request if this is available (exist in the list),subsequently demostrate results, the response was eliminated

    global respSolicitud
    deseaVer=input("1.want to see answer request. 2.other process: ")
    if deseaVer=="1":
        if respSolicitud==[]:
            print("No Answer")
            verRespuestaSolicitud()

        elif respSolicitud!=[]:
            IDSoli=input("type your identification: ")
            cont=0
            while cont<len(respSolicitud):
                if respSolicitud[cont]["identification"]==IDSoli:
                    print(respSolicitud[cont])
                    del respSolicitud[cont]
                    verRespuestaSolicitud()
                cont=cont+1
                
            if cont==len(respSolicitud):
                print("No Answer")
                verRespuestaSolicitud()

    if deseaVer=="2":
        m= "employee"
        employeeMenu(m)
    else:
        print("data error")
        verRespuestaSolicitud()
        
def menuAdministrator(admin):

    print("******************************************************************************************************")
    print("*                                     WELCOME                                                        *")
    print("******************************************************************************************************")
    print("The options are: ","\n","1. Employee","                                   ","5. Vacations",
                            "\n",  "2. Post","                                       ","6. Bonuses",
                            "\n",  "3. Payroll","                                    ","7. Log out",
                            "\n",  "4. Performance Evaluation","                     ","8. Exit the program")
    print("")
    option= input("Enter the number of the desired option: ")

#empleados
    if option=="1":
        print("")
        print("***************************************************************************************************************")
        print("The options are: ","\n",  "1. Add New Employee","                         ","5. Print Inactive Employees",
                                  "\n",  "2. Print History Worker","                     ","6. Amount Employees of the Company",
                                  "\n",  "3. Change Employee State","                    ","7. Log out",
                                  "\n",  "4. Print Employee State","                     ","8. Go to Main Menu")

        option= input("Enter the number of the desired option: ")
        if option == "1":
            print("***********************************************************************************************************")
            obtainUserData()
        elif option == "2":
            print("***********************************************************************************************************")
            history(admin)
        elif option == "3":
            print("***********************************************************************************************************")
            cambiarEstado()
        elif option == "4":
            print("***********************************************************************************************************")
            employeeState()
        elif option == "5":
            print("***********************************************************************************************************")
            inactiveEmployes()
        elif option == "6":
            print("***********************************************************************************************************")
            contarEmpleados()
        elif option == "7":
            print("***********************************************************************************************************")
            login()
        elif option == "8":
            print("***********************************************************************************************************")
            menuAdministrator(admin)
        else:
            print("ERROR: type in what appears on screen, please try again")
            print("")
            menuAdministrator(admin)
#puestos
    elif option=="2":
        print("")
        print("*********************************************************************************************************************")
        print("The options are: ",      "\n",  "1. Add New Job Post",
                                        "\n",  "2. change Employee Post",
                                        "\n",  "3. Delete Post",
                                        "\n",  "4. Go to Main Menu")
        option= input("Enter the number of the desired option: ")
        if option == "1":
            print("***********************************************************************************************************")
            createSince()
        elif option == "2":
            print("***********************************************************************************************************")
            changeSince()
        elif option == "3":
            print("***********************************************************************************************************")
            deletePosts()
        elif option == "4":
            print("***********************************************************************************************************")
            menuAdministrator(admin)
        else:
            print("ERROR: type in what appears on screen, please try again")
            print("")
            menuAdministrator(admin)
#planilla
    elif option=="3":
        print("")
        print("***********************************************************************************************************************")
        print("The options are: ",      "\n",  "1. calculate payroll",
                                        "\n",  "2. Print Payroll by Employee ",
                                        "\n",  "3. Total Payroll of the Company",
                                        "\n"   "4. Print Total Extra and Regular Hours"
                                        "\n"   "5. Go to Main Menu")
        option= input("Enter the number of the desired option: ")
        if option == "1":
            print("***********************************************************************************************************")
            addHoursEmployee()
        elif option == "2":
            print("***********************************************************************************************************")
            imprimirPlanilla(admin)
        elif option == "3":
            print("***********************************************************************************************************")
            imprimirPlanillaTotal()
        elif option == "4":
            print("***********************************************************************************************************")
            printAmountHours()
        elif option == "5":
            print("***********************************************************************************************************")
            menuAdministrator(admin)
        else:
            print("ERROR: type in what appears on screen, please try again")
            print("")
            menuAdministrator(admin)
#evaluaciones de desempeño
    elif option=="4":
        print("")
        print("*********************************************************************************************************************")
        print("The options are: ",      "\n",  "1. Qualify Employee Performance Evaluation",
                                        "\n",  "2. Edit or Delete Performance Evaluation",
                                        "\n",  "3. Print Performance Evaluation",
                                        "\n",  "4. Print Total Performance Evaluation Paid of the Company ",
                                        "\n",  "5. Go to Main Menu")
        option= input("Enter the number of the desired option: ")
        if option == "1":
            print("***********************************************************************************************************")
            incentive()
        elif option == "2":
            print("***********************************************************************************************************")
            editOrDellinsentive()
        elif option == "3":
            print("***********************************************************************************************************")
            seeTheCalification(admin)
        elif option == "4":
            print("***********************************************************************************************************")
            totalBonusesIncentives()
        elif option == "5":
            print("***********************************************************************************************************")
            menuAdministrator(admin)
        else:
            print("ERROR: type in what appears on screen, please try again")
            print("")
            menuAdministrator(admin)
# vacaciones
    elif option=="5":
        print("")
        print("*********************************************************************************************************************")
        print("The options are: ",      "\n",  "1.accept or reject holidays ",
                                        "\n",  "2. Print Report Vacation",
                                        "\n",  "3. Go to Main Menu")
        option= input("Enter the number of the desired option: ")
        if option == "1":
            print("***********************************************************************************************************")
            aceptarORechazar()
        elif option == "2":
            print("***********************************************************************************************************")
            imprimirInfoVacaciones(admin)
        elif option == "3":
            print("***********************************************************************************************************")
            menuAdministrator(admin)
        else:
            print("ERROR: type in what appears on screen, please try again")
            print("")
            menuAdministrator(admin)




#aguinaldo
    elif option=="6":
        print("")
        print("*********************************************************************************************************************")
        print("The options are: ",      "\n",  "1. Perform Employee Bonuses",
                                        "\n",  "2. Print Employee Bonuses",
                                        "\n",  "3. Print Total Bonuses of the Company",
                                        "\n",  "4. Go to Main Menu")
        option= input("Enter the number of the desired option: ")
        if option == "1":
            print("***********************************************************************************************************")
            performBonuses()
        elif option == "2":
            print("***********************************************************************************************************")
            printAguinaldo(admin)
        elif option == "3":
            print("***********************************************************************************************************")
            sumAguinaldo()
        elif option == "4":
            print("***********************************************************************************************************")
            menuAdministrator(admin)
        else:
            print("ERROR: type in what appears on screen, please try again")
            print("")
            menuAdministrator(admin)

#ir a login
    elif option == "7":
        print("*******************************************************************************************************************")
        login()
#sale del programa
    elif option == "8":
        print("GOOD BYE")
        quit()
    else:
        print("ERROR: type in what appears on screen, please try again")
        menuAdministrator(admin)



def employeeMenu(emplo):
    print("******************************************************************************************************")
    print("*                                     WELCOME                                                        *")
    print("******************************************************************************************************")
    print("The options are: ","\n","1. Request History","                                   ","6. Consult Bonus",
                            "\n",  "2. Print my Payroll","                                  ","7. See Answer Vacation Request",
                            "\n",  "3. Print Information About Vacation","                  ","8. Log Out",
                            "\n",  "4. Performance Evaluation","                            ","9. Exit the Program",
                            "\n",  "5. Holiday Request")
    print("")



#la 4, si es asi



    option= input("Enter the number of the desired option: ")
    if option=="1":
        print("***********************************************************************************************************")
        history(emplo)

    elif option=="2":
        print("***********************************************************************************************************")
        imprimirPlanilla(emplo)

    elif option=="3":
        print("***********************************************************************************************************")
        imprimirInfoVacaciones(emplo)

    elif option=="4":
        print("***********************************************************************************************************")
        seeTheCalification(emplo)

    elif option=="5":
        print("***********************************************************************************************************")
        solicitarVacaciones()

    elif option=="6":
        print("***********************************************************************************************************")
        printAguinaldo(emplo)

    elif option=="7":
        print("***********************************************************************************************************")
        verRespuestaSolicitud()

    elif option=="8":
        print("***********************************************************************************************************")
        login()
    elif option=="9":
        print("***********************************************************************************************************")
        print("GOOD BYE")
        quit()
    else:
        print("ERROR: type in what appears on screen, please try again")
        employeeMenu(emplo)


login()
