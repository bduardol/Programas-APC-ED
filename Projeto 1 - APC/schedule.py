schedules = []

all_commands = []

monday = []
tuesday = []
wednesday = []
thurday = []
friday = []
saturday = []
semana = [monday,tuesday,wednesday,thurday,friday,saturday]
auxoperand = []

erro = []
errofinal = []
ind = []
x = ''
o = 1
#+ CIC0004B 235M12
def errou(printerro):
    """reogarnizar os erros para mostra na tela"""
    for i in range(len(erro)):
        x = erro[i]
        if x[0] in errou:
            for i in range(len(erro)):
                if x[0] == erro[i]:
                    ind.append(index(erro))
            
            
  
def validate_command(command):
    """Verifica se o comando é válido. Retorna True ou False"""

    parts = command.split(' ')
    operand, code, times = parts[0], parts[1], parts[2:]
    if operand == '+':
        auxoperand = 1
    else:
        auxoperand = 0
    if len(code) != 8:
        return False
    if not code[:3].isalpha():
        return False
    if not code[3:7].isalnum():
        return False
    if not code[-1].isalpha():
        return False

    for time in times:
        if ('M' not in time) and ('N' not in time) and ('T' not in time):
            return False
    
    return True

def insert_command(command):
    """Guarda o código e os horários de acordo com a estrutura do comando"""
    o = 1
    all_commands.append(command)
    parts = command.split(' ')
    operand, code, times = parts[0], parts[1], parts[2:]

    for time in times:
        if 'M' in time:
            x = 'M'
            weekdays, hours = time.split('M')
        elif 'N' in time:
            x = 'N'
            weekdays, hours = time.split('N')
        elif 'T' in time:
            x = 'T'
            weekdays, hours = time.split('T')

        for day in weekdays:
            if day == '2':
                for c in range(len(hours)):
                    for i in range(len(monday)):
                        if x+hours[c] in monday[i]:
                            o = 0
                            break
                    monday.append(code+' '+x+hours[c]) if o else erro.append(['+ '+code+' '+day+x+hours[c]])
                    if o==0:
                        if command not in errofinal:
                            errofinal.append(command)
                    o = 1
                        
            elif day == '3':
                for c in range(len(hours)):
                    for i in range(len(tuesday)):
                        if x+hours[c] in tuesday[i]:
                            o = 0
                            break
                    tuesday.append(code+' '+x+hours[c]) if o else erro.append(['+ '+code+' '+day+x+hours[c]])
                    o = 1
                    
            elif day == '4':
                for c in range(len(hours)):
                    for i in range(len(wednesday)):
                        if x+hours[c] in wednesday[i]:
                            o = 0
                            break
                    wednesday.append(code+' '+x+hours[c]) if o else erro.append(['+ '+code+' '+day+x+hours[c]])
                    o = 1
                    
            elif day == '5':
                for c in range(len(hours)):
                    for i in range(len(thurday)):
                        if x+hours[c] in thurday[i]:
                            o = 0
                            break
                    thurday.append(code+' '+x+hours[c]) if o else erro.append(['+ '+code+' '+day+x+hours[c]])
                    o = 1
                    
            elif day == '6':
                for c in range(len(hours)):
                    for i in range(len(friday)):
                        if x+hours[c] in friday[i]:
                            o = 0
                            break
                    friday.append(code+' '+x+hours[c]) if o else erro.append(['+ '+code+' '+day+x+hours[c]])
                    o = 1
                                           
            elif day == '7':
                for c in range(len(hours)):
                    for i in range(len(saturday)):
                        if x+hours[c] in saturday[i]:
                            o = 0
                            break
                    saturday.append(code+' '+x+hours[c]) if o else erro.append(['+ '+code+' '+day+x+hours[c]])
                    o = 1
                
def remove_command(command):
    """Remove um comando da lista"""
    all_commands.append(command)
    parts = command.split(' ')
    operand, code, times = parts[0], parts[1], parts[2:]

    for time in times:
        if 'M' in time:
            x = 'M'
            weekdays, hours = time.split('M')
        elif 'N' in time:
            x = 'N'
            weekdays, hours = time.split('N')
            totalhour = weekdays * hours
        elif 'T' in time:
            x = 'T'
            weekdays, hours = time.split('T')

        for day in weekdays:
            o = 1
            if day == '2':
                for c in range(len(hours)):
                    for i in range(len(monday)):
                        if code+' '+x+hours[c] in monday[i]:
                            o = 0
                            break
                    erro.append(['- '+code+' '+day+x+hours[c]]) if o else monday.remove(code+' '+x+hours[c])
                    o = 1
                    
                #for i in range(len(hours)):
                   # if [code, hours[i]] in monday:
                      #  monday.remove([code, hours])
                    #else:
                        #erro.append([code, hours[i]])
                      
            elif day == '3':
                for c in range(len(hours)):
                    for i in range(len(tuesday)):
                        if code+' '+x+hours[c] in tuesday[i]:
                            o = 0
                            break
                    erro.append(['- '+code+' '+day+x+hours[c]]) if o else tuesday.remove(code+' '+x+hours[c])
                    o = 1
                        
            elif day == '4':
                for c in range(len(hours)):
                    for i in range(len(wednesday)):
                        if code+' '+x+hours[c] in wednesday[i]:
                            o = 0
                            break
                    erro.append(['- '+code+' '+day+x+hours[c]]) if o else wednesday.remove(code+' '+x+hours[c])
                    o = 1

            elif day == '5':
                for c in range(len(hours)):
                    for i in range(len(thurday)):
                        if code+' '+x+hours[c] in thurday[i]:
                            o = 0
                            break
                    erro.append(['- '+code+' '+day+x+hours[c]]) if o else thurday.remove(code+' '+x+hours[c])
                    o = 1

            elif day == '6':
                for c in range(len(hours)):
                    for i in range(len(friday)):
                        if code+' '+x+hours[c] in friday[i]:
                            o = 0
                            break
                    erro.append(['- '+code+' '+day+x+hours[c]]) if o else friday.remove(code+' '+x+hours[c])
                    o = 1
                    
            elif day == '7':
                for c in range(len(hours)):
                    for i in range(len(saturday)):
                        if code+' '+x+hours[c] in saturday[i]:
                            o = 0
                            break
                    erro.append(['- '+code+' '+day+x+hours[c]]) if o else saturday.remove(code+' '+x+hours[c])
                    o = 1
            

    pass

def display_schedule():
    """Mostra a tabela com os horários"""
    for i in range(len(errofinal)):
        print(f'!({errofinal[i]})')
    erro = []
    errofinal = []
    n = 0
    print('+---------------+----------+----------+----------+----------+----------+----------+')
    print('|               | Seg      | Ter      | Qua      | Qui      | Sex      | Sab      |')
    print('+---------------+----------+----------+----------+----------+----------+----------+')
    while True:
        for i in range(len(semana)):
            for i in range(len(semana[i])):
                x = semana[i]
            
    
    
    
    pass

stop_command = 'Hasta la vista, beibe!'

input_command = input("Digite o comando...\n\n")

while input_command != stop_command:
    if input_command == "?":
        display_schedule()
    else:
        is_valid = validate_command(input_command)
        auxoperand = 1 if input_command[0] == '+' else 0  
        
        if is_valid and auxoperand:
            insert_command(input_command)
        elif is_valid == 1 and auxoperand == False:
            remove_command(input_command)
        else:
            print(f'!({input_command})')
            
    print(erro)
    print(errofinal)
    print(all_commands)
    input_command = input("Digite o comando...\n\n")
        
