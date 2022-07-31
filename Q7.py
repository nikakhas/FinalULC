def identifier(string,tokens):
    if (string[0]=='$') and string[1]!='_':
        tokens.append([string,'variable'])
        return 1
    elif(string[0]=='$') and string[1]=='_':
        tokens.append([string,'privatevariable'])
        return 1
    elif (string[0]=='@') and string[1]!='_':
        tokens.append([string,'array'])
        return 1
    elif(string[0]=='@') and string[1]=='_':
        tokens.append([string,'privatearray'])
        return 1
    elif (string[0]=='#') and string[1]!='_':
        tokens.append([string,'hashmap'])
        return 1
    elif(string[0]=='#') and string[1]=='_':
        tokens.append([string,'privatehashmap'])
        return 1
    else:
        return 0
def typeDeclaration(string, token):
    if(string=='str'):
        token.append([string,'String'])
        return 1
    elif(string=='int'):
        token.append([string,'Int'])
        return 1
    elif(string=='char'):
        token.append([string,'Char'])
        return 1
    elif(string=='float'):
        token.append([string,'Float'])
        return 1
    else:
        return 0
   
def symbol(firststr,tokens):
    if(firststr=='=='):
        tokens.append([firststr,'Assignment'])
        return 1
    elif(firststr=='+'):
        tokens.append([firststr,'Addition'])
        return 1
    elif(firststr=='-'):
        tokens.append([firststr,'Subtract'])
        return 1
    elif(firststr=="div"):
         tokens.append([firststr,'Division'])
         return 1
    elif(firststr=='**'):
         tokens.append([firststr,'Multiply'])
         return 1
    elif(firststr=='mod'):
          tokens.append([firststr,'Modulo'])
          return 1
    elif(firststr=='&&'):
          tokens.append([firststr,'and'])  
          return 1
    elif(firststr=='||'):
           tokens.append([firststr,'or'])  
           return 1
    elif(firststr=='{'):
          tokens.append([firststr,'open_block'])
          return 1
    elif(firststr=='}'):
          tokens.append([firststr,'close_block'])  
          return 1
    elif(firststr=='('):
           tokens.append([firststr,'open_parenthesis'])  
           return 1
    elif(firststr==')'):
           tokens.append([firststr,'close_parenthesis'])  
           return 1
    elif(firststr=='['):
            tokens.append([firststr,'open_array'])
            return 1
    elif(firststr==']'):
            tokens.append([firststr,'close_array'])
            return 1
    elif(firststr==';'):
            tokens.append([firststr,'endofstatement'])
            return 1
    else:
            return 0
def literals(string,token):
    if(string[0]=="\"" and string[-1]=="\""):
        token.append([string,'string'])
        return 1
    elif (string[0]=="'" and string[0]=="'" and len(string)==3):
        token.append([string,'character'])
        return 1
    elif(digit(string)):
        if ('.' in string):
            token.append([string,'float'])
            return 1
        else:
            token.append([string,'integer'])
            return 1
    else:
        return 0
 
 
 
 
def digit(string):
     
      operator=['+','-','.']
      operator2=['e','E']
   
      digitlen=len(string)
      if(string[0].isdigit() or (string[0] in operator2) or (string[0] in operator)):
          if(digitlen<=1):
              if not string[0].isdigit():
                  flag=0
              else:
                  flag=1
          elif(digitlen>1):
             if(string[0].isdigit() or string[0]=='-' or string[0]=='+'):
                 j=1
                 while(j<digitlen):
                     if (string[j].isdigit()):
                         flag=1
                     elif(string[j]=='.'):
                         flag=1
                     elif(string[j] in operator2):
                       
                         j=j+1
                         if (string[j]=='+' or string[j]=='-'):
                             flag=1
                         else:
                             flag=0
                             break
                     else:
                        flag=0
                        break
                     j=j+1
             elif(string[0]=='.'):
                 j=1
                 while(j<digitlen):
                     if(not string[j].isdigit()):
                       flag=0
                       break
                     else:
                       flag=1
                     j=j+1
             elif(string[0] in operator2):
           
                 if(string[1]=='+' or string[1]=='-'):
                    j=2
                    while j<digitlen:
                        if (not string[j].isdigit()):
                            flag=0
                            break
                        elif(string[j].isdigit()):
                            flag=1
                        else:
                            flag=0
                            break
                        j=j+1
                 else:
                     flag=0  
             else:
                 flag=0
         
      else:
          flag=0
      return flag        
 
 
 
tokens=[]
with open("tester.txt","r") as line:
    lines=line.readlines()
for string in lines:
    for firststr in string.split():
        if(identifier(firststr, tokens)):
            a=0
        elif(typeDeclaration(firststr,tokens)):
            a=0
        elif(symbol(firststr, tokens)):
            a=0
        elif(literals(firststr, tokens)):
            a=0
        else:
            print('undefinned token ', firststr)
            exit()
 
       
print(tokens)
rules=Syntax.Syntax(tokens)
symboltable,expression=rules.declaration()
print('symboltable',symboltable)
print('expression',expression)
 
result=expression.copy()
 
for i in expression:
    j=0
    if 'mod' in i:
        ind=i.index('mod')
        a=i[ind+1]
        b=i[ind-1]
        i.pop(ind+1)
        i.pop(ind)
        i.pop(ind-1)
        i.append(int(symboltable[a][0]) % int(symboltable[b][0]))
       
    if 'div' in i :
        ind=i.index('div')
        a=i[ind+1]
        b=i[ind-1]
        i.pop(ind+1)
        i.pop(ind)
        i.pop(ind-1)
        if(symboltable[a][1]=='integer' and symboltable[b][1]=='integer'):
            i.append(int(symboltable[a][0]) / int(symboltable[b][0]))
        else:
            i.append(float(symboltable[a][0]) / float(symboltable[b][0]))
    if '***' in i :        
              ind=i.index('***')
              a=i[ind+1]
              b=i[ind-1]
              i.pop(ind+1)
              i.pop(ind)
              i.pop(ind-1)
              if (isinstance(a, str)):
                  if(symboltable[a][1]=='integer' and symboltable[b][1]=='integer'):
                      i.append(int(symboltable[a][0]) * int(symboltable[b][0]))
                  else:
                      i.append(float(symboltable[a][0]) * float(symboltable[b][0]))              
              else:
                  i.append(float(symboltable[b][0]) * float(a))  
    if '+' in i :        
        ind=i.index('+')
        a=i[ind+1]
        b=i[ind-1]
        print('i==',i)
        i.pop(ind+1)
        i.pop(ind)
        i.pop(ind-1)
       
        if (isinstance(a, str)):
            if(symboltable[a][1]=='integer' and symboltable[b][1]=='integer'):
                i.append(int(symboltable[a][0]) + int(symboltable[b][0]))
            else:
                i.append(float(symboltable[a][0]) + float(symboltable[b][0]))
        else:
            i.append(float(symboltable[b][0]) + float(a))
    if '-' in i :        
          ind=i.index('-')
          a=i[ind+1]
          b=i[ind-1]
          i.pop(ind+1)
          i.pop(ind)
          i.pop(ind-1)
          if (isinstance(a, str)):
              if(symboltable[a][1]=='integer' and symboltable[b][1]=='integer'):
                  i.append(int(symboltable[a][0]) - int(symboltable[b][0]))
              else:
                  i.append(float(symboltable[a][0]) - float(symboltable[b][0]))
          else:
              i.append(float(symboltable[b][0]) * float(a))  
 
print('Result',expression)