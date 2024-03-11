def main():
    heros = ['spider man', 'thor', 'hulk', 'iron man', 'captain america']

    print(f"Length of the list is : {len(heros)}")

    heros.append('black panther')
    print(f"Added black panter at the end of the list: {heros}")

    heros.remove('black panther')
    heros.insert(3, 'black panther')
    print(f"Removed black panther at the end and inserted after hulk: {heros}")

    heros[1], heros[2] = 'doctor strange', 'doctor strange'
    print(f"Replaced Thor and hulk with doctor strange in one line: {heros}")

    heros.sort()
    print(f"Sorted the heros list in alphabetical order: {heros}")

if __name__ == '__main__':
    main()