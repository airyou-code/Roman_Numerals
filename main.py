class RomanNumerals:

    def to_roman(val):
        ans=""
        ara_rom = [["M",1000], ["CM",900], ["D",500], ["CD",400], ["C",100], ["XC",90], ["X",10], ["V",5], ["IV",4], ["I",1]]
        for i in range(len(ara_rom)):
            ans += val//ara_rom[i][1] * ara_rom[i][0]
            val %= ara_rom[i][1]  
        return ans

    def from_roman(roman_num):
        roman_dict = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "V":5, "IV":4, "I":1}
        ans = 0
        i=0
        while i < len(roman_num):
            if i+1 != len(roman_num):
                if roman_dict[roman_num[i]] < roman_dict[roman_num[i+1]]:
                    ans += roman_dict[roman_num[i]+roman_num[i+1]]
                    i+=1
                    if i+1 == len(roman_num): break
            ans+=roman_dict[roman_num[i]]
            i+=1
        return ans
