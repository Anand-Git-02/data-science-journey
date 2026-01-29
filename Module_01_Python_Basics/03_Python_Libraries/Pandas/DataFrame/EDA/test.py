import phonenumbers

from phonenumbers import geocoder, carrier

phon_number_1 = phonenumbers.parse("+918511779261")
phon_number_2 = phonenumbers.parse("+919924118088")

print('Phone Number Location')
print(geocoder.description_for_number(phon_number_1, "en"))
print(geocoder.description_for_number(phon_number_2, "en"))
