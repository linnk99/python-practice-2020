

def run():
    counter = 0
    with open('aleph.txt') as f:
        for line in f:
            counter += line.count('Muerte')
    
    print('Beatriz se encuentra {} en el texto'.format(counter))



if __name__ == "__main__":
    run()