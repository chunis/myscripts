#!/usr/bin/python
# -*- encoding: utf-8 -*-

# Chunis Deng (chunchengfh@gmail.com)


# あア a  いイ i   うウ u   えエ e  おオ o
# かカ ka きキ ki  くク ku  けケ ke こコ ko
# さサ sa しシ shi すス su  せセ se そソ so
# たタ ta ちチ chi つツ tsu てテ te とト to
# なナ na にニ ni  ぬヌ nu  ねネ ne のノ no
# はハ ha ひヒ hi  ふフ fu  へヘ he ほホ ho
# まマ ma みミ mi  むム mu  めメ me もモ mo
# やヤ ya いイ i   ゆユ yu  えエ e  よヨ yo
# らラ ra りリ ri  るル ru  れレ re ろロ ro
# わワ wa いイ i   うウ u   えエ e  をヲ o 

import sys
import random
import time


allsounds = [
    'あ', 'ア', 'a ', 'い', 'イ', 'i  ', 'う', 'ウ', 'u  ', 'え', 'エ', 'e ', 'お', 'オ', 'o ',
    'か', 'カ', 'ka', 'き', 'キ', 'ki ', 'く', 'ク', 'ku ', 'け', 'ケ', 'ke', 'こ', 'コ', 'ko',
    'さ', 'サ', 'sa', 'し', 'シ', 'shi', 'す', 'ス', 'su ', 'せ', 'セ', 'se', 'そ', 'ソ', 'so',
    'た', 'タ', 'ta', 'ち', 'チ', 'chi', 'つ', 'ツ', 'tsu', 'て', 'テ', 'te', 'と', 'ト', 'to',
    'な', 'ナ', 'na', 'に', 'ニ', 'ni ', 'ぬ', 'ヌ', 'nu ', 'ね', 'ネ', 'ne', 'の', 'ノ', 'no',
    'は', 'ハ', 'ha', 'ひ', 'ヒ', 'hi ', 'ふ', 'フ', 'fu ', 'へ', 'ヘ', 'he', 'ほ', 'ホ', 'ho',
    'ま', 'マ', 'ma', 'み', 'ミ', 'mi ', 'む', 'ム', 'mu ', 'め', 'メ', 'me', 'も', 'モ', 'mo',
    'や', 'ヤ', 'ya', 'い', 'イ', 'i  ', 'ゆ', 'ユ', 'yu ', 'え', 'エ', 'e ', 'よ', 'ヨ', 'yo',
    'ら', 'ラ', 'ra', 'り', 'リ', 'ri ', 'る', 'ル', 'ru ', 'れ', 'レ', 're', 'ろ', 'ロ', 'ro',
    'わ', 'ワ', 'wa', 'い', 'イ', 'i  ', 'う', 'ウ', 'u  ', 'え', 'エ', 'e ', 'を', 'ヲ', 'o ',
]

def usage(name):
    print '''Usage:
    %s          : use 1st ('あ') as hint
    %s 1        : use 1st ('あ') as hint
    %s 2        : use 2nd ('ア') as hint
    %s 3        : use 3rd ('a') as hint
    %s 4 type n : 'n' number of 'type' words''' %(name, name, name, name, name)

def shuffle_tuple_as_list(tpl):
    lst = list(tpl)
    random.shuffle(lst)
    return lst

def check_a_sound(tpl, index, newset):
    print tpl[index - 1]
    while True:
        feedback = raw_input()
        feedback = feedback.strip().lower()
        if feedback == 'q':
            print "Exit... Bye"
            sys.exit()
        elif feedback == 'l':
            print tpl[0], tpl[1], tpl[2]
        elif feedback == 'y':
            print 'removed'
            break
        elif feedback == 'n':
            newset.add(tpl)
            print 'try later'
            break


def test_single(snd_list, option):
    tmp_set = set()
    while snd_list:
        print "Let's begin..."
        for i, x in enumerate(snd_list):
            print "(%d/%d): " %(i+1, len(snd_list)),
            check_a_sound(x, option, tmp_set)

        # Finish one loop. Show what's left
        print "Totally %d items left" %len(tmp_set)
        _more = raw_input("Show all? [y]")
        more = _more.strip().lower()
        if more == "n":
            pass
        else:
            for x in tmp_set:
                print x[0], x[1], x[2]
            print

        snd_list = shuffle_tuple_as_list(tmp_set)
        tmp_set = set()

def test_multi(sound_list, index, num):
    loop = 25  # one test with 25 words
    indexlist = range(len(sound_list))
    i = 0
    while i < loop:
        random.shuffle(indexlist)
        print "(%d/%d) " %(i+1, loop),
        tmplist = [sound_list[si] for si in indexlist[:num]]
        for ix in tmplist:
            print ix[index-1],
        print

        while True:
            feedback = raw_input()
            feedback = feedback.strip().lower()
            if feedback == 'q':
                print "Exit... Bye"
                sys.exit()
            elif feedback == 'l':
                for n in range(3):
                    for ix in tmplist:
                        print "%s" %ix[n],
                    print
            elif feedback == 'y':
                i += 1
                break
            elif feedback == 'n':
                break


snd_set = set()
while allsounds:
    snd_set.add(tuple(allsounds[:3]))
    allsounds = allsounds[3:]
sound_list = shuffle_tuple_as_list(snd_set)


option = 1
index = 1
num = 3

if len(sys.argv) > 1:
    if sys.argv[1] == '-h' or sys.argv[1] == '--help':
        usage(sys.argv[0])
        sys.exit()

    option = int(sys.argv[1])
    if option > 0 and option <= 3:
        pass
    elif option == 4:
        index = int(sys.argv[2])
        num = int(sys.argv[3])
    else:
        option = 1


start = time.ctime()
print "\nStart at: %s\n" %start
if option < 3:
    test_single(sound_list, option)
elif option == 4:
    test_multi(sound_list, index, num)

print "Start  at:", start
print "Finish at:", time.ctime(), "\n"
