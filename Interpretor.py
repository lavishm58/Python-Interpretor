import sys

# from pythonds.basic.stack import Stack

dic = {}


class program(object):
    def __init__(self, lines):
        self.lines = lines


    def eval(self):
        i=0
        while i < len(self.lines):
            cif = 0
            cfi = 0
            if (self.lines[i].find('print') != -1):
                pos = self.lines[i].find('t')
                disp_inst = display(self.lines[i][pos + 1:])
                disp_inst.eval()
                i += 1
                continue

            elif ('while' in self.lines[i]):
                #print('i=',i)
                pos = self.lines[i].find('e')
                while_inst = condition()

                if (while_inst.eval(self.lines[i][pos + 1:])):
                    cwhile = 0
                    cdone = 0
                    for j in range(i, len(self.lines)):
                        if 'while' in self.lines[j]:
                            cwhile += 1
                        if 'done' in self.lines[j]:
                            cdone += 1
                        if cwhile == cdone:
                            break
                    p = program(self.lines[i + 1:j])
                    p.eval()
                    #print(i)
                    continue

                else:
                    cwhile = 0
                    cdone = 0
                    for j in range(i, len(self.lines)):
                        if 'while' in self.lines[j]:
                            cwhile += 1
                        if 'done' in self.lines[j]:
                            cdone += 1
                        if cwhile == cdone:
                            break
                    i = j + 1
                    continue

            elif 'if' in self.lines[i]:
                pos = self.lines[i].find('f')
                if_inst = condition()
                if (if_inst.eval(self.lines[i][pos + 1:])):
                    # print("if true!!")
                    cif = 0
                    cfi = 0
                    for j in range(i, len(self.lines)):
                        if 'if' in self.lines[j]:
                            cif += 1
                        if 'fi' == self.lines[j]:
                            cfi += 1
                        if cif == cfi:
                            break
                    cif = 0
                    celse = 0
                    flag = 0
                    for k in range(i, len(self.lines)):
                        if 'if' in self.lines[k]:
                            cif += 1
                        if 'else' == self.lines[k]:
                            celse += 1
                        if cif == celse:
                            flag = 1
                            break
                    if flag == 1:
                        p = program(self.lines[i + 1:k])
                        p.eval()
                    else:
                        p = program(self.lines[i + 1:j])
                        p.eval()
                    i = j + 1
                else:
                    # print("else true!!")
                    cif = 0
                    cfi = 0
                    for j in range(i, len(self.lines)):
                        if 'if' in self.lines[j]:
                            cif += 1
                        if 'fi' == self.lines[j]:
                            cfi += 1
                        if cif == cfi:
                            break
                    cif = 0
                    celse = 0
                    flag = 0
                    for k in range(i, len(self.lines)):
                        if 'if' in self.lines[k]:
                            cif += 1
                        if 'else' == self.lines[k]:
                            celse += 1
                        if cif == celse:
                            flag = 1
                            break
                    if flag == 1:
                        i = k + 1
                    else:
                        i = j + 1
                continue

            elif 'fi' == self.lines[i]:
                i += 1
                continue
            elif (self.lines[i].find(':=') != -1 and self.lines[i].find("if") == -1):
                a1 = assignment(self.lines[i], self.lines[i].find(':='))
                a1.eval()
                i+=1
class assignment(object):
    def __init__(self, word, pos):
        self.leftexp = word[:pos]
        self.rightexp = word[pos + 2:]

    def eval(self):
        self.exp = expression()
        #print(self.rightexp)
        dic[self.leftexp] = self.exp.eval(self.rightexp)


class display(object):
    def __init__(self, toprint):
        self.toprint = toprint

    def eval(self):
        if self.toprint[0] == '"':
            print(self.toprint[1:(len(self.toprint) - 1)], end=' ')
            return

        elif self.toprint == r'\n':
            print('\n', end=' ')
            return

        else:
            exp_inst = expression()
            print(exp_inst.eval(self.toprint), end=' ')


class condition(object):
    def eval(self, cond):

        if '<=' in cond:
            pos = cond.find('<')
            left_exp = expression()
            left = left_exp.eval(cond[:pos])
            right_exp = expression()
            right = right_exp.eval(cond[pos + 2:])
            # print('left=',left)
            # print('right=',right)
            if float(left) <= float(right):
                return True
            else:
                return False

        elif '>=' in cond:
            pos = cond.find('>')
            left_exp = expression()
            left = left_exp.eval(cond[:pos])
            right_exp = expression()
            right = right_exp.eval(cond[pos + 2:])
            # print('left=',left)
            # print('right=',right)
            if float(left) >= float(right):
                return True
            else:
                return False

        elif '<' in cond:
            pos = cond.find('<')
            left_exp = expression()
            left = left_exp.eval(cond[:pos])
            right_exp = expression()
            right = right_exp.eval(cond[pos + 1:])
            # print('left=',left)
            # print('right=',right)
            if float(left) < float(right):
                return True
            else:
                return False

        elif '>' in cond:
            pos = cond.find('>')
            left_exp = expression()
            left = left_exp.eval(cond[:pos])
            right_exp = expression()
            right = right_exp.eval(cond[pos + 1:])
            # print('left=',left)
            # print('right=',right)
            if float(left) > float(right):
                return True
            else:
                return False

        elif '==' in cond:
            pos = cond.find('=')
            left_exp = expression()
            left = left_exp.eval(cond[:pos])
            right_exp = expression()
            right = right_exp.eval(cond[pos + 2:])
            # print('left=',left)
            # print('right=',right)
            if float(left) == float(right):
                return True
            else:
                return False

        elif '!=' in cond:
            pos = cond.find('!')
            left_exp = expression()
            left = left_exp.eval(cond[:pos])
            right_exp = expression()
            right = right_exp.eval(cond[pos + 2:])
            # print('left=',left)
            # print('right=',right)
            if float(left) != float(right):
                return True
            else:
                return False

class expression(object):
    def eval(self, ex):
        flag=0
        c1=0
        i=0
        st=[]
        stp=[]
        while i!=len(ex):
            if ex[i]=='(':
                c1+=1
                st.append(i)

            if ex[i]==')':
                c1-=1
                stp.append(i)
                self.exp1=cal()
                a=st.pop()
                #print(c1)
                b=stp.pop()
                ans=self.exp1.eval(ex[a+1:b])
                ex=ex[:a]+str(ans)+ex[b+1:]
                #print(ex)
                i=a
            i+=1
        if c1!=0:
            raise Exception('not valid')
        self.exp1=cal()
        ans=self.exp1.eval(ex)
        return ans

class match(object):
    def error(self):
        raise Exception('Error parsing input')
    def float(self,op):
        if is_number(op) is True:
            return float(op)
        if op in dic:
            return dic[op]
        else:
            self.error()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

class cal(object):

    def eval(self,exp):
        while is_number(exp) is False:
            if exp.find('--')!=-1:
                i=exp.find('--')
                exp=exp[:i]+'+'+exp[i+2:]
            if exp.find('+-')!=-1:
                i=exp.find('+-')
                exp = exp[:i] + '-' + exp[i + 2:]
            if exp.find('-+')!=-1:
                i=exp.find('-+')
                exp = exp[:i] + '-' + exp[i + 2:]
            if exp.find('/+')!=-1:
                i=exp.find('/+')!=-1
                exp=exp[:i+1]+exp[i+2:]

            if exp.find('/-')!=-1:
                i=exp.find('/-')!=-1
                exp=exp[:i+1]+exp[i+2:]
            if exp.find('*+')!=-1:
                i=exp.find('*+')!=-1
                exp=exp[:i+1]+exp[i+2:]
            if exp.find('*-')!=-1:
                i=exp.find('*-')!=-1
                exp=exp[:i+1]+exp[i+2:]
            if exp.find('+')!=-1 and exp.find('+')==0:
                exp=exp[1:]
            if exp.find('*')!=-1:
                i=exp.find('*')
                self.a = match()
                j=i+1
                st=j
                minus_pre=0
                if exp[i+1]=='-':
                    j=i+2
                    st=j
                    minus_pre=1
                while j<len(exp) and (is_number(exp[j]) or exp[j]=='.'or exp[j].isalpha()):
                    j += 1
                    m=j
                r = self.a.float(exp[st:m])
                k = i - 1
                while k >= 0 and (is_number(exp[k]) or exp[k] == '.'or exp[k].isalpha()):
                    k -= 1
                l = self.a.float(exp[k+1:i])
                if k==0 and exp[k]=='-':
                    minus_pre=2
                    k-=1
                if minus_pre==0:
                    ans=l*r
                    exp=exp[:k+1]+str(ans)+exp[m:]
                if minus_pre==1:
                    ans=-l*r
                    exp=exp[:k+1]+str(ans)+exp[m:]
                if minus_pre==2:
                    ans=l*r
                    exp=exp[:k+1]+str(ans)+exp[m:]

            if exp.find('/')!=-1:
                i=exp.find('/')
                self.a = match()
                j=i+1
                st=j
                minus_pre=0
                if exp[i+1]=='-':
                    j=i+2
                    st=j
                    minus_pre=1
                while j<len(exp) and (is_number(exp[j]) or exp[j]=='.'or exp[j].isalpha()):
                    j += 1
                    m=j
                r = self.a.float(exp[st:m])
                k = i - 1
                while k >= 0 and (is_number(exp[k]) or exp[k] == '.'or exp[k].isalpha()):
                    k -= 1
                l = self.a.float(exp[k+1:i])
                if k==0 and exp[k]=='-':
                    minus_pre=2
                    k-=1
                if minus_pre==0:
                    ans=l/r
                    exp=exp[:k+1]+str(ans)+exp[m:]
                if minus_pre==1:
                    ans=-l/r
                    exp=exp[:k+1]+str(ans)+exp[m:]
                if minus_pre==2:
                    ans=l/r
                    exp=exp[:k+1]+str(ans)+exp[m:]

            if exp.find('+')!=-1:
                i = exp.find('+')
                self.a = match()
                j = i + 1
                while j<len(exp) and (is_number(exp[j]) or exp[j]=='.'or exp[j].isalpha()) :
                    j += 1
                r = self.a.float(exp[i + 1:j])
                k = i - 1
                while k>=0 and (is_number(exp[k]) or exp[k]=='.'or exp[k].isalpha()):
                    k -= 1
                l = self.a.float(exp[k+1:i])
                if k>=0 and exp[k]=='-':
                    l=-l
                    k-=1
                exp = exp[:k+1] + str(l + r) + exp[j:]


            if exp.find('-')!=-1:
                i = exp.find('-')
                self.a = match()
                j = i + 1

                while j<len(exp) and (is_number(exp[j]) or exp[j]=='.'or exp[j].isalpha()):
                    j += 1
                r = self.a.float(exp[i + 1:j])
                if i == 0 and j>=len(exp):
                    break
                k = i - 1
                while k >= 0 and (is_number(exp[k]) or exp[k] == '.'or exp[k].isalpha()):
                    k -= 1
                l = self.a.float(exp[k+1:i])
                if k==0 and exp[k]=='-':
                    l=-l
                    k-=1
                exp = exp[:k+1] + str(l - r) + exp[j:]
            if exp.isalpha():
                self.a=match()
                exp=self.a.float(exp)

        #print(exp)
        return float(exp)



class operator(object):
    def eval(self, op, x, y):
        if (op == '>'):
            if (x > y):
                return True
            else:
                return False
        if (op == '<'):
            if (x < y):
                return True
            else:
                return False
        if (op == "="):
            if (x == y):
                return True
            else:
                return False


filename = "d.txt"
lines = [line.rstrip('\n') for line in open(filename)]
lines = ([s.rstrip(';') for s in lines])
lines = ([s.replace(' ', '') for s in lines])

a = program(lines)
a.eval()
print(dic)

'''final=[]
for word in lines:
    temp=[]
   if(word[0]=='i' and word[1]=='f'):
       temp.append(word)
       for end in lines(word+1,len(lines)):
           if(end[0]=='f' and end[1]=='i')





   else:
       final.append(word)'''



# def assignment():


# def condition():
