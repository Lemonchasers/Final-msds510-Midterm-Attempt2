import sys
input1 = sys.argv[1]
output2 = sys.argv[2]


def main(input1, output2):
    with open(input1, 'rb') as a:
        avengers = a.read()
    avengers_decoded = avengers.decode('iso-8859-1')
    avengers_encoded = avengers_decoded.encode('utf8')
    with open(output2, 'wb') as b:
        b.write(avengers_encoded)
    print(output2)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
