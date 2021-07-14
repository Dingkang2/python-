def city(city_name):
    def country(country_name):
        return city_name + ', ' + country_name
    return country

temp = city('BeiJing')
print(temp('China'))