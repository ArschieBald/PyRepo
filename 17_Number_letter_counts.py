# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

dic1 = {"1":"one","2":"two","3":"three","4":"four","5":"five","6":"six","7":"seven","8":"eight","9":"nine"}
dic2 = {"2":"twenty","3":"thirty","4":"forty","5":"fifty","6":"sixty","7":"seventy","8":"eighty","9":"ninety"}
dic3 = {"1":"onehundredand","2":"twohundredand","3":"threehundredand","4":"fourhundredand","5":"fivehundredand","6":"sixhundredand","7":"sevenhundredand","8":"eighthundredand","9":"ninehundredand"}
exceptions = {"10":"ten","11":"eleven","12":"twelve","13":"thirteen","14":"fourteen","15":"fifteen","16":"sixteen","17":"seventeen","18":"eighteen","19":"nineteen"}
exceptions1 = {"10":"ten","20":"twenty","30":"thirty","40":"forty","50":"fifty","60":"sixty","70":"seventy","80":"eighty","90":"ninety"}
exceptions2 = {"100":"onehundredand","200":"twohundredand","300":"threehundredand","400":"fourhundredand","500":"fivehundredand","600":"sixhundredand","700":"sevenhundredand","800":"eighthundredand","900":"ninehundredand"}

string = ""
for i in range(1,1000):
    i = str(i)
    if len(i) == 3:  # 3 basamaklı sayılar için
        if i[1] == "0" and i[2] == "0":  # 100-200-300... gibi durumlar
            string += exceptions2[i]
            string = string[:-3]
        elif i[1] == "0":  # 2. basamağının 0 olduğu durumlar için(106-605...)
            string += dic3[i[0]] + dic1[i[2]]
        elif i[1] == "1":  # 2. basamağının 1 olduğu durumlar için(210-919...)
            string += dic3[i[0]] + exceptions[i[1:]]
        elif i[2] == "0":  # 1. basamağının 0 olduğu durumlar için(390-450...)
            string += dic3[i[0]] + dic2[i[1]]
        else:
            string += dic3[i[0]] + dic2[i[1]] + dic1[i[2]]
    elif len(i) == 2:  # 2 basamaklı sayılar için
        if i[1] == "0":  # 1. basamağının 0 olduğu durumlar için(70-80...)
            string += exceptions1[i]
        elif i[0] == "1":  # 2. basamağının 1 olduğu durumlar için(11-16...)
            string += exceptions[i]
        else:
            string += dic2[i[0]] + dic1[i[1]]
    else:
        string += dic1[i[0]]
string += "onethousand"
print(len(string))
