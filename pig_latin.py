class Rule:
    def __init__(self, condition, action):
        self.condition = condition
        self.action = action

    def evaluate(self, context):
        if self.condition(context):
            self.action(context)

class RuleEngine:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def run(self, context):
        for rule in self.rules:
            rule.evaluate(context)
            if context.get('processed', False):
                break


# Conditions and actions for Pig Latin rules

def condition1(context):
    word = context['word']
    vowels = "aeiou"
    return word[0] in vowels or word[:2] in {"xr", "yt"}


def action1(context):
    context['result'].append(context['word'] + "ay")
    context['processed'] = True

def condition3(context):
    word = context['word']
    return "qu" in word


def action3(context):
    word = context['word']
    index_qu = word.index("qu") + 2
    context['result'].append(word[index_qu:] + word[:index_qu] + "ay")
    context['processed'] = True

def condition4(context):
    word = context['word']
    vowels = "aeiou"
    return ("y" in word and word.index("y") > 0 and
            all(letter not in vowels for letter in word[:word.index("y")]))

def action4(context):
    word = context['word']
    index_y = word.index("y")
    context['result'].append(word[index_y:] + word[:index_y] + "ay")
    context['processed'] = True


def condition2(context):
    word = context['word']
    vowels = "aeiou"
    return not (word[0] in vowels or word[:2] in ["xr", "yt"])


def action2(context):
    word = context['word']
    vowels = "aeiou"
    for i, letter in enumerate(word):
        if letter in vowels:
            context['result'].append(word[i:] + word[:i] + "ay")
            context['processed'] = True
            return

# Rule Engine Initialization
engine = RuleEngine()
engine.add_rule(Rule(condition1, action1))
engine.add_rule(Rule(condition3, action3))
engine.add_rule(Rule(condition4, action4))
engine.add_rule(Rule(condition2, action2))


def translate(text):
    result = []
    for word in text.split():
        context = {'word': word, 'result': result, 'processed': False}
        engine.run(context)
    return " ".join(result)
