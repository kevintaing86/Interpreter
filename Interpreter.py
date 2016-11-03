#Kevin Taing


class Stack(object):
    def _intit_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if self.items == []:
            return TRUE
        else:
            return FALSE

class Lex(object):
    def _init_(self, text):
        self.text = text
        self.pos = 0
        self.current_token = text[self.pos]

    def get_current(self):
        return self.current_token
    
    #This will advance the pointer and it will return the token
    def get_next(self):
        if self.pos > len(self.text) - 1:
            self.current_token = 'EOF'

        self.pos += 1
        while text[self.pos == ' ']:
            self.pos += 1

        if text[self.pos] == '-':
            if text[self.pos + 1] == '>':
                self.pos += 1
                self.current_token = '->'
                #return self.current_token
            else:
                raise Exception('Syntax error: arrow typo')

        self.current_token = text[self.pos]
        #return self.current_token

class Interpreter(object):
    def _init_(self, text):
        self.text = text
        self.lex = Lex(text)
        self.stack = Stack()

    def atom(self):
        if self.lex.get_current() == 'T':
            self.stack.push('T')
            self.lex.get_next()
            return TRUE
        elif self.lex.get_current() == 'F':
            self.stack.push('F')
            self.lex.get_next()
            return TRUE
        elif self.lex.get_current() == '(':
            self.lex.get_next()
            #call another function
            #return TRUE 
        else:
            raise Exception('Syntax error: error in atom')
            return FALSE

    def literal(self):
        if self.lex.get_current() == '~':
            self.lex.get_next()

            if self.lex.isEmpty():
                raise Exception('Syntax error: trying to inverse something that is not inversible')
                return FALSE
            elif literal():
                temp = self.stack.pop()

                if temp == 'T':
                    self.stack.push('F')
                    return TRUE
                elif temp == 'F':
                    self.stack.push('T')
                    return TRUE
            elif atom():
                temp = self.stack.pop()

                if temp == 'T':
                    self.stack.push('F')
                    return TRUE
                elif temp == 'F':
                    self.stack.push('T')
                    return TRUE
        elif atom():
            return TRUE

        else:
            raise Exception('Syntax error: expected a literal')
            return FALSE

    def And_Tail(self):
        if self.lex.get_current() == '^':
            self.lex.get_next()

            if literal():
                temp = self.lex.pop()
                temp2 = self.lex.pop()

                if temp == 'F' or temp2 == 'F':
                    self.lex.push('F')
                    return TRUE
                else:
                    self.lex.push('T')
                    return TRUE

        else:
            return TRUE


    def And_Term(self):
        if literal():
            if And_Tail():
                return TRUE
            else:
                raise Exception('And term expected And_Tail')
                return FALSE
        else:
            raise Exception('And term error')
            return FALSE

    def Or_Tail(self):
        if self.lex.get_current() == 'v':
            self.lex.get_next()

            if And_Term():
                temp = self.lex.pop()
                temp2 = self.lex.pop()

                if temp == 'T' or temp2 == 'T':
                    self.lex.push('T')
                    return TRUE
                else:
                    self.lex.push('F')
                    return TRUE
        else:
            return TRUE

    def Or_Term(self):
        if And_Term():
            if Or_Tail():
                return TRUE
            else:
                raise Exception('Syntax error: Or term expected an Or_Tail')
                return FALSE
        else:
            raise Exception('Syntax error: Or term error')
            return FALSE

    def Imply_Tail(self):
        if self.lex.get_current() == '->':
            self.lex.get_next()

            if Or_Term():
                temp = self.lex.pop()
                temp2 = self.lexl.pop()

                if temp == temp2:
                    self.lex.push('T')
                    return TRUE
                else:
                    self.lex.push('F')
                    return TRUE
            else:
                raise Exception('Syntax error: expected Bool_Stmt')
                return FALSE
        else:
            return TRUE

    def Imply_Term(self):
        if Or_Term():
            if Imply_Tail():
                return TRUE
            else:
                raise Exception('Syntax error: Imply term expected an Imply_Tail')
                return FALSE
        else:
            raise Exception('Syntax error: Imply term error')
            return FALSE
    
    def Bool_Stmt(self):
        if Imply_Term():
            return TRUE
        elif self.lex.get_current() == '.':
            return TRUE
        else:
            raise Exception('Syntax error: Not a boolean statement')
            return FALSE
                
    def Final_Value(self):
        return self.stack.pop()

class main(object):
    def main():
        text = input('Enter Text> ')

        interpreter = Interpreter(text)

        print(interpreter.Final_Value())





                
