from random import choice

def biogenerate( name, age):

	birthrank = ['youngest', 'first-born', 'eldest', 'middle', 'sole']
	parent1 = ['Lord Sherry']
	parent2 = ['Lady Bourbon']
	hobby = ['running with horses']
	placetype = ['her family estate', 'her summer cottage']
	location = ['Northumberland', 'West Yorkshire', 'East Riding of Yorkshire', 'Merseyside', 'Shropshire', 'East Devon', 'Somerset', 'Isle of Wight', 'East Sussex', 'Cumbria', 'Lancashire', 'South Oxfordshire', 'Essex', 'Maidenhead', 'East Hertfordshire', 'Surrey Heath', 'Winchester']
	school = ['Wimbledon College of Art Theatre', 'South-East Essex Technical College', 'Stoke-on-Trent College of Art', 'East Anglican School of Painting and Drawing', 'Birmingham Guild of Handicraft', 'Lower Dorchester Municipal College of Fashion Technology', 'Bournemouth Municipal College of Art', 'London South Bank University', 'University of West London', 'University of Greenwich', ]
	degree = ['Horticulture', 'Hospitality and Tourism', 'Dance/Movement Therapy' ]
	business = ['interior design']
	grabbag = ['swimming with turtles']

	return name + ', ' + age + ', the ' + choice(birthrank) + ' daughter of ' + choice(parent1) + ' and ' + choice(parent2) + ', is depicted ' + choice(hobby) + ' near her ' + choice(placetype) + ' in ' + choice(location) + '. ' + name + ' is finishing her degree in ' + choice(degree) + ' at the ' + choice(school) + '. She enjoys ' + choice(hobby) + ' when she is not busy running her ' + choice(business) + ' business, and in her spare time she has a pechant for ' + choice(grabbag) + '.'

 
