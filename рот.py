name = ("my_dict")
pnone_book = {"Arseni": 986543057, "Ivan": 907633057}
print(name,pnone_book["Ivan"])
pnone_book.update({"Vasilisa": 999861105,
                   "Antoshka": 876943010})
print(pnone_book)
a = pnone_book.pop("Vasilisa")
print(pnone_book)
print(a)

my_set = set_ = {"cat",6794,5.5,"cat",6794}
print(set_)

my_set.update({"milk","oil"})
print(my_set)