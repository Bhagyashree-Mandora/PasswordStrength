class ExtendPasswords:

    def __init__(self):
        self.common = self.__populate()

    def __populate(self):
        common_pwd = open("../data/common_passwords","r")
        data = common_pwd.readlines()
        common_pwd.close()
        common = []
        for line in data:
            common.append(line.strip())
        return common

    def create_variations(self):
        rev = self.__reverse_technique(self.common)
        rep = self.__repeat_technique(self.common)
        cap = self.__capitalize(self.common)
        dig = self.__digitize(self.common)
        ch = self.__special_characterize(self.common)
        cap_with_dig = self.__digitize(cap)
        dig_with_ch = self.__special_characterize(dig)
        cap_with_ch = self.__special_characterize(cap)
        cap_dig_ch = self.__special_characterize(cap_with_dig)
        all_variations = self.common + rev + rep + cap + dig + ch + cap_with_dig + dig_with_ch + cap_with_ch + cap_dig_ch
        self.__write_pwds(all_variations)

    def __reverse_technique(self, words):
        rev = []
        for w in words:
            rev.append(w[::-1])
        return rev

    def __repeat_technique(self, words):
        rep = []
        for w in words:
            rep.append(w*2)
            rep.append(w*3)
        return rep

    def __capitalize(self, words):
        cap = []
        for w in words:
            cap.append(w.capitalize())
        return cap

    def __digitize(self, words):
        dig = []
        for w in words:
            for digit in range(10):
                dig.append(w + str(digit))
                dig.append(w[:-1] + str(digit) + w[-1:])
        return dig

    def __special_characterize(self, words):
        chars = ["!", "@", "#", "$", "%", "&"]
        ch = []
        for w in words:
            for c in chars:
                ch.append(w + c)
        return ch

    def __write_pwds(self, pwds):
        with open("../data/all", "w") as f:
            for p in pwds:
                f.write("%s\n" % p)
