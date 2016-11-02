#Kevin Taing

EOF, SPACE, OR, AND, TRUE, FALSE, LEFT_PARAN, RIGHT_PARAN, ARROW1, ARROW2, TAIL, NOT = 'EOF', 'SPACE', 'OR', 'AND', 'TRUE', 'FALSE', 'LEFT_PARAN', 'RIGHT_PARAN', 'ARROW1', 'ARROW2', 'TAIL', 'NOT'

class Token(object):
    def _init_(self, type, value):
        self.type = type
        self.value = value

    def _str_(self):
        return Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def _repr_(self):
        return self._str_()

class Stack(object):
    def _intit_(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        if self.items = []:
            return TRUE
        else:
            return FALSE

class Lex(object):
    def _init_(self, text):
        self.text = text
        self.pos = 0
        self.current_token = text[self.pos]

    def get_current():
        return self.current_token

    def get_next():
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

    def get_next(self):
        text = self.text
        if self.pos > len(text) - 1:
            return Token(EOF, None)

        self.pos += 1
        current_char = text[self.pos]
        return current_char

    def atom():
        if self.lex.get_current() == 'T':
            self.stack.push('T')
            self.lex.get_next()
        elif self.lex.get_current() == 'F':
            self.stack.push('F')
            self.lex.get_next()
        elif self.lex.get_current() == '('
            self.lex.get_next()
            #call another function
        else:
            raise Exception('Syntax error: error in atom')

    def literal():
        if self.lex.get_current() == '~':
            self.lex.get_next()

            if(self.lex.isEmpty()):
                raise Exception('Syntax error: trying to inverse something that is not inversible')
            else:
                
