import itertools
import hashlib
import sys
import argparse


def hmmm_Hash(file, target, hash_algo):
    data = ""
    try:
        with open(file,'r') as f:
            data = f.read()
    except:
        print("The file was not able to be opened")
    data = data.split('\n')
    for nlen in range(1,len(data)):
        combos = itertools.permutations(data,r = nlen)
        for x in combos:
            temp=""
            for y in x:
                temp+=y
            if hash_algo == 'sha256':
                hash_result = get_sha256_digest(temp)
                if hash_result == target:
                    print("MATCH:\n"+str(temp))
                    exit()
            elif hash_algo == 'md5':
                hash_result = get_md5_digest(temp)
                if hash_result == target:
                    print("MATCH:\n" + str(temp))
                    exit()
    print("NO match found")

def get_sha256_digest(string):
    m = hashlib.sha256()
    m.update(string.encode("utf8"))
    return m.hexdigest()

def get_md5_digest(string):
    m = hashlib.md5()
    m.update(string.encode("utf8"))
    return m.hexdigest()

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--gethash', action='store')
    parser.add_argument('--algo', action='store', default="sha256")
    parser.add_argument('--file', action='store', help='seed data file (newline delimited)')
    parser.add_argument('--hash', action='store')
    args = parser.parse_args();

    if args.gethash:
        # This used to exit if there was no algo arg. Defaults to "sha256" now
        if args.algo == "sha256":
            print(get_sha256_digest(args.gethash))
        elif args.algo == "md5":
            print(get_md5_digest(args.gethash))
        else: 
            print("Invalid algorithm")
        exit()
    if args.file == None:
        print('must have a file of seed data newline delimited')
    if args.hash == None:
        print("Must have a -hash parameter to compare to")
    if args.hash is not None and args.file is not None:
        hmmm_Hash(args.file,args.hash,args.algo)
    return
main()
