political_divisions =[{"name": "Alabama", "abbreviation": "AL",
                          "counties": ["Dale", "Autauga", "Baldwin", "Bibb", "Bullock", "Chilton", "Coffee", "Coosa",
                                       "Etowah", "Franklin", "Lamar", "Macon", "Marion", "Morgan", "Randolph", "Sumter",
                                       "Wilcox", "Barbour", "Blount", "Butler", "Calhoun", "Chambers", "Cherokee",
                                       "Choctaw", "Clarke", "Clay", "Cleburne", "Colbert", "Conecuh", "Covington",
                                       "Crenshaw", "Cullman", "Dallas", "DeKalb", "Elmore", "Escambia", "Fayette",
                                       "Geneva", "Greene", "Hale", "Henry", "Houston", "Jefferson", "Lauderdale",
                                       "Lawrence", "Lee", "Lowndes", "Madison", "Marengo", "Marshall", "Mobile",
                                       "Monroe", "Montgomery", "Jackson", "Perry", "Pickens", "Pike", "Russell",
                                       "St. Clair", "Shelby", "Talladega", "Tallapoosa", "Tuscaloosa", "Walker",
                                       "Washington", "Winston", "Limestone"]},
                         {"name": "Alaska", "abbreviation": "AK",
                          "counties": ["Valdez-Cordova",
                                       "Wade Hampton", "Wrangell",
                                       "Yukon-Koyukuk",
                                       "Ketchikan Gateway",
                                       "Aleutians East", "Bethel",
                                       "Hoonah-Angoon", "Sitka",
                                       "Kenai Peninsula",
                                       "Kodiak Island",
                                       "Lake and Peninsula",
                                       "Nome", "Petersburg",
                                       "North Slope",
                                       "Northwest Arctic",
                                       "Southeast Fairbanks",
                                       "Yakutat",
                                       "Aleutians West",
                                       "Anchorage", "Bristol Bay",
                                       "Denali", "Dillingham",
                                       "Fairbanks North Star",
                                       "Haines", "Juneau",
                                       "Matanuska-Susitna",
                                       "Prince of Wales-Hyder",
                                       "Skagway"]},
                         {"name": "Arizona", "abbreviation": "AZ",
                          "counties": ["Mohave", "Santa Cruz", "Cochise", "Graham", "La Paz", "Pima", "Pinal",
                                       "Yavapai", "Yuma", "Apache", "Coconino", "Gila", "Greenlee", "Maricopa",
                                       "Navajo"]},
                         {"name": "Arkansas", "abbreviation": "AR",
                          "counties": ["Cleveland", "Columbia", "Baxter", "Cleburne", "Cross",
                                       "Drew", "Garland", "Hot Spring", "Jackson",
                                       "Little River", "Madison", "Montgomery", "Pike",
                                       "Poinsett", "St. Francis", "Searcy", "Sharp", "Union",
                                       "Van Buren", "Washington", "Woodruff", "Arkansas",
                                       "Ashley", "Benton", "Boone", "Bradley", "Calhoun",
                                       "Carroll", "Chicot", "Clark", "Clay", "Conway",
                                       "Craighead", "Crawford", "Crittenden", "Newton",
                                       "Ouachita", "Perry", "Phillips", "Polk", "Pope",
                                       "Prairie", "Pulaski", "Randolph", "Saline", "Scott",
                                       "Sebastian", "Sevier", "Stone", "Dallas", "Desha",
                                       "Faulkner", "Franklin", "Fulton", "Grant", "Greene",
                                       "Hempstead", "Howard", "Independence", "Izard",
                                       "Jefferson", "Johnson", "Lafayette", "Lawrence", "Lee",
                                       "Logan", "Lonoke", "Marion", "Miller", "Mississippi",
                                       "Monroe", "Nevada", "White", "Yell", "Lincoln"]},
                         {"name": "California", "abbreviation": "CA",
                          "counties": ["Colusa", "Glenn", "Kings", "Mariposa", "Modoc", "Sacramento", "San Bernardino",
                                       "Santa Barbara", "Shasta", "Tulare", "Alameda", "Alpine", "Marin", "Mendocino",
                                       "Merced", "Mono", "Monterey", "Napa", "Nevada", "Orange", "Placer", "Plumas",
                                       "Riverside", "San Benito", "San Diego", "San Francisco", "San Joaquin", "Amador",
                                       "Butte", "Calaveras", "Contra Costa", "Del Norte", "El Dorado", "Fresno",
                                       "Humboldt", "Imperial", "Inyo", "Kern", "Lake", "Lassen", "Los Angeles",
                                       "Madera", "San Luis Obispo", "San Mateo", "Santa Clara", "Santa Cruz", "Sierra",
                                       "Siskiyou", "Solano", "Sonoma", "Stanislaus", "Tehama", "Trinity", "Tuolumne",
                                       "Ventura", "Yolo", "Yuba", "Sutter"]},
                         {"name": "Colorado", "abbreviation": "CO",
                          "counties": ["Hinsdale", "Kiowa", "Lincoln", "Mineral", "Montrose", "Phillips", "Pueblo",
                                       "Rio Grande", "Sedgwick", "Washington", "Adams", "Alamosa", "Bent", "Boulder",
                                       "Broomfield", "Crowley", "Elbert", "Gilpin", "Gunnison", "Huerfano", "Jackson",
                                       "Jefferson", "Kit Carson", "Lake", "La Plata", "Larimer", "Las Animas", "Logan",
                                       "Mesa", "Moffat", "Montezuma", "Morgan", "Otero", "Ouray", "Park", "Pitkin",
                                       "Prowers", "Rio Blanco", "Routt", "Saguache", "San Juan", "San Miguel", "Summit",
                                       "Teller", "Weld", "Yuma", "Cheyenne", "Arapahoe", "Archuleta", "Baca", "Chaffee",
                                       "Clear Creek", "Conejos", "Costilla", "Custer", "Delta", "Denver", "Dolores",
                                       "Eagle", "El Paso", "Fremont", "Garfield", "Grand", "Douglas"]},
                         {"name": "Connecticut", "abbreviation": "CT",
                          "counties": ["Tolland", "Windham", "Fairfield", "Hartford", "Litchfield", "Middlesex",
                                       "New Haven", "New London"]}]

n=int(input())
while(n>=1):
    n=n-1
    s=input().split()
    save=[]
    if(s[0]=="1"):
        for part in political_divisions:
            if(part["name"]==s[1] or part["abbreviation"]==s[1] or part["abbreviation"]==str.lower(s[1])):
                for elements in part["counties"]:
                    if(elements[0]==s[2]):
                        save.append(elements)
                        save.sort()
                    
                for e in save[0:-1]:
                    print(e,end=", ")
                print(save[-1])
                   
    if(s[0]=="2"):
        for i in range(2, len(s)):
            s[1] += " " + s[i]
        for part in political_divisions:
            for elements in part["counties"]:
                if(s[1]==elements):
                    save.append(part["abbreviation"])
                    save.sort()
        for e in save[0:-1]:
            print(e,end=", ")
        print(save[-1])
             
                
