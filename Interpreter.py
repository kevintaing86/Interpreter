#Kevin Taing

EOF, SPACE, OR, AND, TRUE, FALSE, LEFT_PARAN, RIGHT_PARAN, ARROW1, ARROW2, TAIL = 'EOF', 'SPACE', 'OR', 'AND', 'TRUE', 'FALSE', 'LEFT_PARAN', 'RIGHT_PARAN', 'ARROW1', 'ARROW2', 'TAIL'

class Token(object):
    def _init_(self, type, value):
        self.type = type
        self.value = value

    def _str_(self):
        return 'Token({type}, {value})'.format(type=self.type, value=repr(self.value))

    def _repr_(self):
        return self._str_()


class Interpreter(object):
    def _init(self, text):
        self.text = text
        self.pos = 0
        self.current_token = None

    def error(self):
        raise Exception('There was an error')

    def get_next(self):
        text = self.text

        if self.pos > len(text) - 1:
            return Token(EOF, None)

        current_char = text[self.pos]

        if current_char == '.':
            token = Token(EOF, current_char)
            self.pos += 1
            return token

        if current_char == ' ':
            token = Token(SPACE, current_char)
            self.pos += 1
            return token

        if current_char == 'v':
            token = Token(OR, current_char)
            self.pos += 1
            return token

        if current_char == '^':
            token = Token(AND, current_char)
            self.pos += 1
            return token

        if current_char == 'T':
            token = Token(TRUE, current_char)
            self.pos += 1
            return token

        if current_char == 'F':
            token = Token(FALSE, current_char)
            self.pos += 1
            return token

        if current_char == '(':
            token = Token(LEFT_PARAN, current_char)
            self.pos += 1
            return token

        if current_char == ')':
            token = Token(RIGHT_PARAN, current_char)
            self.pos += 1
            return token

        if current_char == '-':
            token = Token(ARROW1, current_char)
            self.pos += 1
            return token

        if current_char == '>':
            token = Token(ARROW2, current_char)
            self.pos += 1
            return token

        if current_char == '~':
            token = Token(TAIL, current_char)
            self.pos += 1
            return token

        self.error()


def eat(self, token_type):
    if self.current_token.type == token_type:
        self.current_token = self.get_next()

    else:
        self.error()
