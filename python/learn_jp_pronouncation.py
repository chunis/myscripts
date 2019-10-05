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


option = 1
if len(sys.argv) > 1:
    option = int(sys.argv[1])
    if option > 0 and option <= 3:
        pass
    else:
        option = 1

snd_set = set()
while allsounds:
    snd_set.add(tuple(allsounds[:3]))
    allsounds = allsounds[3:]
snd_list = shuffle_tuple_as_list(snd_set)

tmp_set = set()
while snd_list:
    print "Let's begin..."
    for x in snd_list:
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

