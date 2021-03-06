import os

from app.request.get import UserGet
from app.request.city import CityGet
from app.request.group import GroupGet
from app.request.search import UserSearch
from app.request.country import CountryGet

from app.handler.get import get
from app.handler.sort import sort
from app.handler.city import city
from app.handler.group import group
from app.handler.clean import clean
from app.handler.merge import merge
from app.handler.range import range
from app.handler.exact import exact
from app.handler.count import count
from app.handler.filter import filter
from app.handler.search import search
from app.handler.country import country

app = {
	"root" : "https://api.vk.com/method/",

	"dir" : os.path.dirname(os.path.abspath(__file__)),

	"order" : [ CountryGet, CityGet, UserSearch, UserGet, GroupGet ],

	"current" : -1,

	"async" : 5,

	"execute" : 25,

	"method" : {
		CountryGet : "database.getCountries",
		CityGet : "database.getCities",
		UserSearch : "users.search",
		UserGet : "execute",
		GroupGet : "execute"
	},

	"handlers" : {
		CountryGet : [ country ],
		CityGet : [ city ],
		UserSearch : [ search, range, exact, merge, filter, clean, sort ],
		UserGet : [ get, range, exact, merge, filter, clean, sort ],
		GroupGet : [ group, range, exact, merge, filter, count, clean, sort ]
	},

	"js" : {
		"get" : os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			"js/get.js"
		),

		"group" : os.path.join(
			os.path.dirname(os.path.abspath(__file__)),
			"js/group.js"
		)
	}
}

default = {
	"q" : "",
	"country" : None,
	"city" : None,
	"sort" : "rank",
	"sex" : "any",
	"age" : None,
	"min" : 0
}

val = {
	"sex" : {
		"female" : 1,
		"male" : 2,
		"any" : 0
	},

	"relation" : {
		"not indicated" : 0,
		"single" : 1,
		"in a relationship" : 2,
		"engaged" : 3,
		"married" : 4,
		"it's complicated" : 5,
		"actively searching" : 6,
		"in love" : 7
	},

	"political" : {
		"communist" : 1,
		"socialist" : 2,
		"moderate" : 3,
		"liberal" : 4,
		"conservative" : 5,
		"monarchist" : 6,
		"ultraconservative" : 7,
		"apathetic" : 8,
		"libertian" : 9
	},

	"people" : {
		"intellect and creativity" : 1,
		"kindness and honesty" : 2,
		"health and beauty" : 3,
		"wealth and power" : 4,
		"courage and persistance" : 5,
		"humor and love for life" : 6
	},

	"life" : {
		"family and children" : 1,
		"career and money" : 2,
		"entertainment and leisure" : 3,
		"science and research" : 4,
		"improving the world" : 5,
		"personal development" : 6,
		"beauty and art" : 7,
		"fame and influence" : 8
	},

	"smoking" : {
		"very negative" : 1,
		"negative" : 2,
		"neutral" : 3,
		"compromisable" : 4,
		"positive" : 5
	},

	"alcohol" : {
		"very negative" : 1,
		"negative" : 2,
		"neutral" : 3,
		"compromisable" : 4,
		"positive" : 5
	},

	"platform" : {
		"mobile" : 1,
		"iPhone app" : 2,
		"iPad app" : 3,
		"Android app" : 4,
		"Windows Phone app" : 5,
		"Windows app" : 6,
		"web" : 7
	},

	"country" : {
		"Australia" : "AU",
		"Austria" : "AT",
		"Azerbaijan" : "AZ",
		"Aland Islands" : "AX",
		"Albania" : "AL",
		"Algeria" : "DZ",
		"Minor Outlying Islands (U.S.)" : "UM",
		"U.S. Virgin Islands" : "VI",
		"American Samoa" : "AS",
		"Anguilla" : "AI",
		"Angola" : "AO",
		"Andorra" : "AD",
		"Antarctica" : "AQ",
		"Antigua and Barbuda" : "AG",
		"Argentina" : "AR",
		"Armenia" : "AM",
		"Aruba" : "AW",
		"Afghanistan" : "AF",
		"Bahamas" : "BS",
		"Bangladesh" : "BD",
		"Barbados" : "BB",
		"Bahrain" : "BH",
		"Belize" : "BZ",
		"Belarus" : "BY",
		"Belgium" : "BE",
		"Benin" : "BJ",
		"Bermuda" : "BM",
		"Bulgaria" : "BG",
		"Bolivia" : "BO",
		"Bosnia and Herzegovina" : "BA",
		"Botswana" : "BW",
		"Brazil" : "BR",
		"British Indian Ocean Territory" : "IO",
		"British Virgin Islands" : "VG",
		"Brunei" : "BN",
		"Burkina Faso" : "BF",
		"Burundi" : "BI",
		"Bhutan" : "BT",
		"Vanuatu" : "VU",
		"Vatican" : "VA",
		"United Kingdom" : "GB",
		"Hungary" : "HU",
		"Venezuela" : "VE",
		"East Timor" : "TL",
		"Vietnam" : "VN",
		"Gabon" : "GA",
		"Haiti" : "HT",
		"Guyana" : "GY",
		"Gambia" : "GM",
		"Ghana" : "GH",
		"Guadeloupe" : "GP",
		"Guatemala" : "GT",
		"Guinea" : "GN",
		"Guinea-Bissau" : "GW",
		"Germany" : "DE",
		"Gibraltar" : "GI",
		"Honduras" : "HN",
		"Hong Kong" : "HK",
		"Grenada" : "GD",
		"Greenland" : "GL",
		"Greece" : "GR",
		"Georgia" : "GE",
		"Guam" : "GU",
		"Denmark" : "DK",
		"DR Congo" : "CD",
		"Djibouti" : "DJ",
		"Dominica" : "DM",
		"Dominican Republic" : "DO",
		"European Union" : "EU",
		"Egypt" : "EG",
		"Zambia" : "ZM",
		"Western Sahara" : "EH",
		"Zimbabwe" : "ZW",
		"Israel" : "IL",
		"India" : "IN",
		"Indonesia" : "ID",
		"Jordan" : "JO",
		"Iraq" : "IQ",
		"Iran" : "IR",
		"Ireland" : "IE",
		"Iceland" : "IS",
		"Spain" : "ES",
		"Italy" : "IT",
		"Yemen" : "YE",
		"North Korea" : "KP",
		"Cape Verde" : "CV",
		"Kazakhstan" : "KZ",
		"Cayman Islands" : "KY",
		"Cambodia" : "KH",
		"Cameroon" : "CM",
		"Canada" : "CA",
		"Qatar" : "QA",
		"Kenya" : "KE",
		"Cyprus" : "CY",
		"Kyrgyzstan" : "KG",
		"Kiribati" : "KI",
		"China" : "CN",
		"Cocos Islands" : "CC",
		"Colombia" : "CO",
		"Comoros" : "KM",
		"Costa Rica" : "CR",
		"Ivory Coast" : "CI",
		"Cuba" : "CU",
		"Kuwait" : "KW",
		"Laos" : "LA",
		"Latvia" : "LV",
		"Lesotho" : "LS",
		"Liberia" : "LR",
		"Lebanon" : "LB",
		"Libya" : "LY",
		"Lithuania" : "LT",
		"Liechtenstein" : "LI",
		"Luxembourg" : "LU",
		"Mauritius" : "MU",
		"Mauritania" : "MR",
		"Madagascar" : "MG",
		"Mayotte" : "YT",
		"Macau" : "MO",
		"Republic of Macedonia" : "MK",
		"Malawi" : "MW",
		"Malaysia" : "MY",
		"Mali" : "ML",
		"Maldives" : "MV",
		"Malta" : "MT",
		"Morocco" : "MA",
		"Martinique" : "MQ",
		"Marshall Islands" : "MH",
		"Mexico" : "MX",
		"Mozambique" : "MZ",
		"Moldova" : "MD",
		"Monaco" : "MC",
		"Mongolia" : "MN",
		"Montserrat" : "MS",
		"Myanmar" : "MM",
		"Namibia" : "NA",
		"Nauru" : "NR",
		"Nepal" : "NP",
		"Niger" : "NE",
		"Nigeria" : "NG",
		"Netherlands Antilles" : "AN",
		"The Netherlands" : "NL",
		"Nicaragua" : "NI",
		"Niue" : "NU",
		"New Caledonia" : "NC",
		"New Zealand" : "NZ",
		"Norway" : "NO",
		"UAE" : "AE",
		"Oman" : "OM",
		"Christmas Island" : "CX",
		"Cook Islands" : "CK",
		"Heard Island and McDonald Islands" : "HM",
		"Pakistan" : "PK",
		"Palau" : "PW",
		"Palestine" : "PS",
		"Panama" : "PA",
		"Papua - New Guinea" : "PG",
		"Paraguay" : "PY",
		"Peru" : "PE",
		"Pitcairn Islands" : "PN",
		"Poland" : "PL",
		"Portugal" : "PT",
		"Puerto Rico" : "PR",
		"Republic of the Congo" : "CG",
		"Reunion" : "RE",
		"Russia" : "RU",
		"Rwanda" : "RW",
		"Romania" : "RO",
		"USA" : "US",
		"El Salvador" : "SV",
		"Samoa" : "WS",
		"San Marino" : "SM",
		"Sao Tome and Principe" : "ST",
		"Saudi Arabia" : "SA",
		"Swaziland" : "SZ",
		"Svalbard and Jan Mayen" : "SJ",
		"Northern Mariana Islands" : "MP",
		"Seychelles" : "SC",
		"Senegal" : "SN",
		"St. Vincent and the Grenadines" : "VC",
		"Saint Kitts and Nevis" : "KN",
		"Saint Lucia" : "LC",
		"Saint Pierre and Miquelon" : "PM",
		"Serbia" : "RS",
		"Serbia and Montenegro (valid until September 2006)" : "CS",
		"Singapore" : "SG",
		"Syria" : "SY",
		"Slovakia" : "SK",
		"Slovenia" : "SI",
		"Solomon Islands" : "SB",
		"Somalia" : "SO",
		"Sudan" : "SD",
		"Suriname" : "SR",
		"Sierra Leone" : "SL",
		"USSR (valid until September 1992)" : "SU",
		"Tajikistan" : "TJ",
		"Thailand" : "TH",
		"Republic of China" : "TW",
		"Tanzania" : "TZ",
		"Togo" : "TG",
		"Tokelau" : "TK",
		"Tonga" : "TO",
		"Trinidad and Tobago" : "TT",
		"Tuvalu" : "TV",
		"Tunisia" : "TN",
		"Turkmenistan" : "TM",
		"Turkey" : "TR",
		"Uganda" : "UG",
		"Uzbekistan" : "UZ",
		"Ukraine" : "UA",
		"Uruguay" : "UY",
		"Faroe Islands" : "FO",
		"Micronesia" : "FM",
		"Fiji" : "FJ",
		"Philippines" : "PH",
		"Finland" : "FI",
		"Falkland Islands" : "FK",
		"France" : "FR",
		"French Guiana" : "GF",
		"French Polynesia" : "PF",
		"French Southern and Antarctic Lands" : "TF",
		"Croatia" : "HR",
		"CAR" : "CF",
		"Chad" : "TD",
		"Montenegro" : "ME",
		"Czech Republic" : "CZ",
		"Chile" : "CL",
		"Switzerland" : "CH",
		"Sweden" : "SE",
		"Sri Lanka" : "LK",
		"Ecuador" : "EC",
		"Equatorial Guinea" : "GQ",
		"Eritrea" : "ER",
		"Estonia" : "EE",
		"Ethiopia" : "ET",
		"South Africa" : "ZA",
		"Republic of Korea" : "KR",
		"South Georgia and the South Sandwich Islands" : "GS",
		"Jamaica" : "JM",
		"Japan" : "JP",
		"Bouvet Island" : "BV",
		"Norfolk" : "NF",
		"Saint Helena" : "SH",
		"Turks and Caicos Islands" : "TC",
		"Wallis and Futuna" : "WF"
	}
}

tmp = {}
