country = set(["china", "japan", "russia"])
countryBig = set(["china", "japan", "russia", "india", "brazil"])


print(country & countryBig)

print(countryBig.issuperset(country))
print(countryBig.issubset(country))
print(country.issubset(countryBig))
