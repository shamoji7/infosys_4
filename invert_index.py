#モジュールのインポートと変数・辞書の準備
import sys
argv = sys.argv
argc = len(argv)
words = {}

#索引辞書を作成
for i in range(argc - 1):
    f = open(argv[i+1], 'r')
    for line in f:
        line = line.rstrip()
        split_line = line.split()
        for word in split_line:
            if word not in words:
                words[word] = {}
                words[word][argv[i+1]] = 1
            else:
                words[word][argv[i+1]] = 1

#ソートして表示
for tmp in sorted(words):
    dup = []
    for tmp2 in sorted(words[tmp]):
        dup.append(tmp2)
    print(tmp, ' '.join(dup))
        

f.close()
