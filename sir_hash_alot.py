import itertools
import hashlib
import sys


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
    hash_algo="sha256"
    hash =""
    file=None
    if '-gethash' in sys.argv and sys.argv.index('-gethash')+1 < len(sys.argv):
        if "-algo" in sys.argv and sys.argv.index('-algo')+1 < len(sys.argv):
            hash_algo = sys.argv[sys.argv.index('-algo') + 1]
        else:
            exit()
        if hash_algo == "sha256":
            print(get_sha256_digest(sys.argv[sys.argv.index('-gethash') + 1]))
            exit()
        elif hash_algo == "md5":
            print(get_md5_digest(sys.argv[sys.argv.index('-gethash') + 1]))
            exit()
        else:
            exit()
    if "-hash" in sys.argv and sys.argv.index('-hash')+1 < len(sys.argv):
        hash = sys.argv[sys.argv.index('-hash')+1]
    if "-algo" in sys.argv and sys.argv.index('-algo')+1 < len(sys.argv):
        hash_algo = sys.argv[sys.argv.index('-algo') + 1]
    if "-file" in sys.argv and sys.argv.index('-file')+1 < len(sys.argv):
        file = sys.argv[sys.argv.index('-file') + 1]
    if file == None:
        print("must have a file of seed data newline delimited")
    if hash == None:
        print('Must have a -hash parameter to compare to')
    if hash is not None and file is not None:
        hmmm_Hash(file,hash,hash_algo)
    return
main()
