import lang
import sys

def repl():
    print('dumb lang repl 😊💕')
    counter = 1
    while True:
        code = input(f'{counter} >> ')
        counter += 1
        virgin_code = code.strip().lower()
        if virgin_code == 'break':
            break
        lang.run(code)
            

if __name__ == '__main__':
    # running repl by default because why not
    try:
        if len(sys.argv) == 1:
            repl()
        elif len(sys.argv) > 1:
            with open(sys.argv[1], 'r') as f:
                lang.run(f.read())
    except KeyboardInterrupt:
        pass
else:
    raise RuntimeError('not really meant to be used as a module sry diva')