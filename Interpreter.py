# Kevin Taing
# python 2.7, python interpreter
#
#~My code does not read from a file. Just type into the console

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

class Lex(object):
    def __init__(self, text):
        self.text = text
        self.pos = 0
        self.current_token = text[self.pos]

    def get_current(self):
        return self.current_token

    #This will advance the pointer and it will return the token
    def get_next(self):
        if self.pos > len(self.text) - 1:
            self.current_token = '.'
            return self.current_token

        self.pos += 1
        while self.text[self.pos] == ' ':
            self.pos += 1

        if self.text[self.pos] == '-':
            if self.text[self.pos + 1] == '>':
                self.pos += 1
                self.current_token = '->'
                #return self.current_token
            else:
                raise Exception('Syntax error: arrow typo')

        self.current_token = self.text[self.pos]
        #return self.current_token

class Interpreter(object):
    def __init__(self, text):
        self.text = text
        self.lex = Lex(text)
        self.stack = Stack()

    def atom(self):
        if self.lex.get_current() == 'T':
            self.stack.push('T')
            self.lex.get_next()
            return True
        elif self.lex.get_current() == 'F':
            self.stack.push('F')
            self.lex.get_next()
            return True
        elif self.lex.get_current() == '(':
            self.lex.get_next()
            if self.Bool_Stmt():
                return True
        else:
            raise Exception('Syntax error: expected an atom')
            return False

    def literal(self):
        if self.lex.get_current() == '~':
            self.lex.get_next()

            if self.lex.isEmpty():
                raise Exception('Syntax error: trying to inverse something that is not inversible')
                return False
            elif self.literal():
                temp = self.stack.pop()

                if temp == 'T':
                    self.stack.push('F')
                    return True
                elif temp == 'F':
                    self.stack.push('T')
                    return True
            elif self.atom():
                temp = self.stack.pop()

                if temp == 'T':
                    self.stack.push('F')
                    return True
                elif temp == 'F':
                    self.stack.push('T')
                    return True
        elif self.atom():
            return True

        else:
            raise Exception('Syntax error: expected a literal')
            return False

    def And_Tail(self):
        if self.lex.get_current() == '^':
            self.lex.get_next()

            if self.literal():
                temp = self.stack.pop()
                temp2 = self.stack.pop()

                if temp == 'F' or temp2 == 'F':
                    self.stack.push('F')
                    return True
                else:
                    self.lex.push('T')
                    return True

        else:
            return True


    def And_Term(self):
        if self.literal():
            if self.And_Tail():
                return True
            else:
                raise Exception('And term expected And_Tail')
                return False
        else:
            raise Exception('And term error')
            return False

    def Or_Tail(self):
        if self.lex.get_current() == 'v':
            self.lex.get_next()

            if self.And_Term():
                temp = self.stack.pop()
                temp2 = self.stack.pop()

                if temp == 'T' or temp2 == 'T':
                    self.stack.push('T')
                    return True
                else:
                    self.stack.push('F')
                    return True
        else:
            return True

    def Or_Term(self):
        if self.And_Term():
            if self.Or_Tail():
                return True
            else:
                raise Exception('Syntax error: Or term expected an Or_Tail')
                return False
        else:
            raise Exception('Syntax error: Or term error')
            return False

    def Imply_Tail(self):
        if self.lex.get_current() == '->':
            self.lex.get_next()

            if self.Or_Term():
                temp = self.stack.pop()
                temp2 = self.stack.pop()

                if temp == temp2:
                    self.stack.push('T')
                    return True
                else:
                    self.stack.push('F')
                    return True
            else:
                raise Exception('Syntax error: expected Bool_Stmt')
                return False
        else:
            return True

    def Imply_Term(self):
        if self.Or_Term():
            if self.Imply_Tail():
                return True
            else:
                raise Exception('Syntax error: Imply term expected an Imply_Tail')
                return False
        else:
            raise Exception('Syntax error: Imply term error')
            return False

    def Bool_Stmt(self):
        if self.Imply_Term():
            return True
        elif self.lex.get_current() == '.':
            return True
        else:
            raise Exception('Syntax error: Not a boolean statement')
            return False

    def Final_Value(self):
        return self.stack.pop()


def main():
    text = raw_input('Enter text: ')

    interpreter = Interpreter(text)
    interpreter.Bool_Stmt()
    print(interpreter.Final_Value())


if __name__ == "__main__":
    main()
