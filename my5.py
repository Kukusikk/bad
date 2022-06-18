
flag_res=False

with open("input.txt", "r") as f:
    for line in f:
        if not (line.count('(')+1 == line.count(')') or line.count('(') == line.count(')')+1):
            print(-1)
        else:
            ex = line.split('=')
            current_string=''
            inx=0
            for i in ex:
                if i.count('(') == i.count(')'):
                    current_string+=i
                    continue

                if flag_res==True:
                    print(-1)
                    break

                if i.count('(') == i.count(')')+1:
                    inx=i.find('(')+ len(current_string)
                    
                elif i.count('(')+1 == i.count(')'):
                    inx=i.find(')')+ len(current_string)

                flag_res=True
            print(inx+1)

            
                
    
    
    
