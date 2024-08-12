# -*- coding: utf-8 -*-
"""
Earthquate data to be used for analysis.

Source: https://earthquake.usgs.gov/earthquakes/feed/v1.0/csv.php

Fields: 
    date_time - combined date / time field
    date
    time
    latitude 
    longitude
    depth 
    mag - magnitude of the earthquake
    location - approximate location of the earthquake
    place - description of the epicenter where the earthquake occurred

@author: Jonathan Hoffman
"""


#list of the fields in the data
fields = ["date_time", "date", "time", "latitude", "longitude", "depth", "mag" , "location", "place"]

#values of the earthquake data
data = [["2023-10-26T19:20:09.146Z", "2023-10-26", "19:20:09", -61.1365, 160.7281, 10, 5.6, "Balleny Islands", "Balleny Islands region"]
        , ["2023-10-26T10:27:25.062Z", "2023-10-26", "10:27:25", -17.8614 , -178.5976, 545.564, 4.6, "Fiji", "Fiji region"]
        , ["2023-10-26T07:21:24.529Z", "2023-10-26", "07:21:24", -58.8739, 148.9041, 10, 5.9, "Macquarie Island", "west of Macquarie Island"]
        , ["2023-10-25T15:25:06.159Z", "2023-10-25", "15:25:06", -56.2318, -26.9185, 62.546, 5.2, "South Sandwich Islands", "South Sandwich Islands region"]
        , ["2023-10-25T10:09:15.411Z", "2023-10-25", "10:09:15", -19.2439, -177.7058, 413.626, 4.6, "Fiji", "Fiji region"]
        , ["2023-10-24T22:19:45.618Z", "2023-10-24", "22:19:45", 64.7356, -17.9166, 10, 5.1, "Iceland", "Iceland"]
        , ["2023-10-24T22:17:26.078Z", "2023-10-24", "22:17:26", -13.1372, -76.6398, 56.027, 4.7, "Peru", "near the coast of central Peru"]
        , ["2023-10-24T18:02:45.917Z", "2023-10-24", "18:02:45", 33.5556, 87.4205, 10.018, 4.6, "China", "western Xizang"]
        , ["2023-10-24T01:44:49.310Z", "2023-10-24", "01:44:49", -40.8795, -91.7514, 10, 4.7, "Chile", "West Chile Rise"]
        , ["2023-10-24T01:43:24.708Z", "2023-10-24", "01:43:24", -41.1362, -91.6906, 10, 4.7, "Easter Island", "southeast of Easter Island"]
        , ["2023-10-23T20:35:23.379Z", "2023-10-23", "20:35:23", -23.3559, 170.6451, 10, 4.6, "Loyalty Islands", "southeast of the Loyalty Islands"]
        , ["2023-10-23T14:58:46.668Z", "2023-10-23", "14:58:46", -17.5242, -178.7113, 549.219, 4.6, "Fiji", "Fiji region"]
        , ["2023-10-23T00:17:26.539Z", "2023-10-23", "00:17:26", -23.7218, 179.0544, 542.401, 4.6, "Fiji", "south of the Fiji Islands"]
        , ["2023-10-22T19:31:42.566Z", "2023-10-22", "19:31:42", -23.6936, 179.3579, 532.016, 5.5, "Fiji", "south of the Fiji Islands"]
        , ["2023-10-22T04:45:47.618Z", "2023-10-22", "04:45:47", -25.9983, 69.9756, 10, 5.2, "Indian Ocean Triple Junction", "Indian Ocean Triple Junction"]
        , ["2023-10-22T03:03:21.345Z", "2023-10-22", "03:03:21", -58.6997, -25.2008, 29.585, 4.9, "South Sandwich Islands", "South Sandwich Islands region"]
        , ["2023-10-22T01:54:20.970Z", "2023-10-22", "01:54:20", 27.8679, 84.7191, 24.684, 5.2, "Nepal", "Nepal-India border region"]
        , ["2023-10-21T04:50:38.993Z", "2023-10-21", "04:50:38", -32.1215, -178.0621, 10, 4.7, "Kermadec Islands", "south of the Kermadec Islands"]
        , ["2023-10-21T04:26:01.564Z", "2023-10-21", "04:26:01", -49.8618, 114.1357, 10, 4.7, "Western Indain-Antarctic Range", "western Indian-Antarctic Ridge"]
        , ["2023-10-21T01:02:15.797Z", "2023-10-21", "01:02:15", -4.1557, -104.0109, 10, 4.7, "Pacific Rise", "central East Pacific Rise"]
        , ["2023-10-20T21:21:20.411Z", "2023-10-20", "21:21:20", -18.6595, -172.9717, 10, 4.7, "Tonga", "Tonga region"]
        , ["2023-10-20T03:49:48.242Z", "2023-10-20", "03:49:48", -35.5763, 179.6741, 44.97, 4.6, "New Zealand, off the east coast of the North Island of New Zealand"]
        , ["2023-10-20T16:05:08.204Z", "2023-10-20", "16:05:08", -24.3367, -67.1274, 156.414, 4.5, "Argentina", "83 km W of San Antonio de los Cobres, Argentina"]
        , ["2023-10-21T15:11:07.261Z", "2023-10-21", "15:11:07", -38.6948, 143.5136, 10, 4.8, "Australia", "15 km WNW of Apollo Bay, Australia"]
        , ["2023-10-24T05:58:20.696Z", "2023-10-24", "05:58:20", 50.5879, -130.1581, 10, 4.5, "Canada", "Vancouver Island, Canada region"]
        , ["2023-10-26T21:49:34.459Z", "2023-10-26", "21:49:34", -28.6869, -70.2711, 100.977, 5.4, "Chile", "Atacama, Chile"]
        , ["2023-10-21T02:23:16.536Z", "2023-10-21", "02:23:16", -22.4935, -68.5291, 131.94, 4.5, "Chile", "40 km E of Calama, Chile"]
        , ["2023-10-20T16:56:52.068Z", "2023-10-20", "16:56:52", -22.1277, -67.3442, 175.293, 4.6, "Chile", "123 km NE of San Pedro de Atacama, Chile"]
        , ["2023-10-20T04:43:23.364Z", "2023-10-20", "04:43:23", -28.084, -71.4926, 41.954, 4.7, "Chile", "90 km NW of Vallenar, Chile"]
        , ["2023-10-20T02:03:19.915Z", "2023-10-20", "02:03:19", -20.4037, -68.9309, 114.213, 4.5, "Chile", "76 km E of La Tirana, Chile"]
        , ["2023-10-25T18:35:39.452Z", "2023-10-25", "18:35:39", 36.6279, 83.6899, 10, 4.5, "China", "155 km E of Aqqan, China"]
        , ["2023-10-24T11:32:13.651Z", "2023-10-24", "11:32:13", 39.2796, 97.2878, 10, 5.4, "China", "Gansu, China"]
        , ["2023-10-23T08:43:37.933Z", "2023-10-23", "08:43:37", 31.5853, 88.1154, 10, 4.7, "China", "269 km NNW of Rikaze, China"]
        , ["2023-10-23T06:10:39.131Z", "2023-10-23", "06:10:39", 33.5675, 91.1525, 10, 5, "China", "246 km NNW of Nagqu, China"]
        , ["2023-10-22T19:20:22.635Z", "2023-10-22", "19:20:22", 23.3544, 117.3907, 10, 4.8, "China", "53 km SE of Huanggang, China"]
        , ["2023-10-22T15:14:12.034Z", "2023-10-22", "15:14:12", 39.3035, 97.204, 10, 5, "China", "74 km SW of Laojunmiao, China"]
        , ["2023-10-21T23:39:00.322Z", "2023-10-21", "23:39:00", 7.632, -75.043, 59.267, 4.5, "Colombia", "24 km NW of Zaragoza, Colombia"]
        , ["2023-10-21T10:45:58.982Z", "2023-10-21", "10:45:58", 9.5147, -83.6125, 10, 5.1, "Costa Rica", "18 km NNE of San Isidro, Costa Rica"]
        , ["2023-10-26T19:00:26.171Z", "2023-10-26", "19:00:26", -7.3035, 27.9327, 15.328, 5.4, "Democratic Republic of the Congo", "178 km SE of Kabalo, Democratic Republic of the Congo"]
        , ["2023-10-21T09:03:55.460Z", "2023-10-21", "09:03:55", 11.8041, -62.0956, 131.098, 4.5, "Grenada", "46 km SW of Saint George's, Grenada"]
        , ["2023-10-25T08:18:43.916Z", "2023-10-25", "08:18:43", 64.0121, -22.3656, 10, 4.6, "Iceland", "3 km NNE of Vogar, Iceland"]
        , ["2023-10-25T03:57:46.749Z", "2023-10-25", "03:57:46", -2.849, 128.1118, 23.875, 4.5, "Indonesia", "93 km N of Ambon, Indonesia"]
        , ["2023-10-23T15:30:22.272Z", "2023-10-23", "15:30:22", 1.1569, 127.9713, 10.53, 5, "Indonesia", "Halmahera, Indonesia"]
        , ["2023-10-22T14:23:05.495Z", "2023-10-22", "14:23:05", 0.41, 98.3255, 27.748, 4.7, "Indonesia", "Nias region, Indonesia"]
        , ["2023-10-21T12:04:56.360Z", "2023-10-21", "12:04:56", -8.1326, 118.0666, 10, 4.7, "Indonesia", "62 km NW of Dompu, Indonesia"]
        , ["2023-10-21T05:32:56.254Z", "2023-10-21", "05:32:56", 2.6228, 128.5856, 228.415, 4.8, "Indonesia", "117 km NNE of Tobelo, Indonesia"]
        , ["2023-10-20T19:51:55.439Z", "2023-10-20", "19:51:55", 0.7788, 125.2063, 51.393, 5.2, "Indonesia", "66 km SSE of Tondano, Indonesia"]
        , ["2023-10-20T18:01:37.181Z", "2023-10-20", "18:01:37", -0.7009, 98.4277, 21.053, 4.9, "Indonesia", "157 km SSE of Teluk Dalam, Indonesia"]
        , ["2023-10-20T13:07:02.209Z", "2023-10-20", "13:07:02", 2.1069, 127.8122, 228.264, 4.6, "Indonesia", "47 km NNW of Tobelo, Indonesia"]
        , ["2023-10-20T08:45:42.593Z", "2023-10-20", "08:45:42", 1.0831, 96.8178, 10, 4.5, "Indonesia", "91 km WSW of Gunungsitoli, Indonesia"]
        , ["2023-10-20T08:22:23.625Z", "2023-10-20", "08:22:23", -2.8867, 130.0501, 15.174, 4.6, "Indonesia", "128 km ENE of Masohi, Indonesia"]
        , ["2023-10-20T07:57:29.125Z", "2023-10-20", "07:57:29", -2.9427, 129.7818, 10, 4.9, "Indonesia", "Seram, Indonesia"]
        , ["2023-10-20T02:44:12.218Z", "2023-10-20", "02:44:12", -6.2293, 103.7772, 38.448, 4.6, "Indonesia", "186 km WSW of Bandar Lampung, Indonesia"]
        , ["2023-10-26T20:34:12.759Z", "2023-10-26", "20:34:12", 32.1051, 59.699, 10, 5.1, "Iran", "95 km SSE of Bīrjand, Iran"]
        , ["2023-10-24T21:07:26.320Z", "2023-10-24", "21:07:26", 38.5938, 136.5848, 10, 4.5, "Japan", "153 km N of Anamizu, Japan"]
        , ["2023-10-24T12:29:42.302Z", "2023-10-24", "12:29:42", 35.3545, 139.0164, 166.787, 4.5, "Japan", "7 km ENE of Gotenba, Japan"]
        , ["2023-10-24T02:54:25.952Z", "2023-10-24", "02:54:25", 24.0625, 122.5947, 31.21, 4.6, "Japan", "60 km SW of Yonakuni, Japan"]
        , ["2023-10-23T23:05:25.506Z", "2023-10-23", "23:05:25", 24.0602, 122.6461, 35.161, 5.9, "Japan", "57 km SW of Yonakuni, Japan"]
        , ["2023-10-23T11:28:05.726Z", "2023-10-23", "11:28:05", 24.6314, 125.4683, 51.086, 4.6, "Japan", "23 km SE of Miyakojima, Japan"]
        , ["2023-10-22T14:13:40.467Z", "2023-10-22", "14:13:40", 27.2115, 128.2038, 61.362, 4.6, "Japan", "31 km NE of Iheya, Japan"]
        , ["2023-10-21T15:40:21.518Z", "2023-10-21", "15:40:21", 31.8109, 142.3374, 17.904, 4.7, "Japan", "Izu Islands, Japan region"]
        , ["2023-10-21T02:42:21.165Z", "2023-10-21", "02:42:21", 31.9116, 141.8959, 10, 4.6, "Japan", "Izu Islands, Japan region"]
        , ["2023-10-20T19:16:09.952Z", "2023-10-20", "19:16:09", 30.9618, 141.4852, 35, 4.5, "Japan", "Izu Islands, Japan region"]
        , ["2023-10-20T19:01:45.866Z", "2023-10-20", "19:01:45", 30.987, 141.3473, 38.573, 5, "Japan", "Izu Islands, Japan region"]
        , ["2023-10-26T09:34:21.206Z", "2023-10-26", "09:34:21", 14.4787, -92.6281, 69.635, 4.6, "Mexico", "near the coast of Chiapas, Mexico"]
        , ["2023-10-22T02:05:15.172Z", "2023-10-22", "02:05:15", 16.3143, -99.0333, 10, 4.9, "Mexico", "33 km S of Copala, Mexico"]
        , ["2023-10-21T17:10:01.488Z", "2023-10-21", "17:10:01", 14.1917, -93.451, 10, 5.1, "Mexico", "125 km WSW of Puerto Madero, Mexico"]
        , ["2023-10-21T17:05:13.508Z", "2023-10-21", "17:05:13", 14.2136, -93.4334, 10, 4.6, "Mexico", "122 km WSW of Puerto Madero, Mexico"]
        , ["2023-10-20T23:00:21.344Z", "2023-10-20", "23:00:21", 14.3049, -93.4249, 10, 4.9, "Mexico", "117 km WSW of Puerto Madero, Mexico"]
        , ["2023-10-26T23:26:15.637Z", "2023-10-26", "23:26:15", -23.0252, 170.2122, 10, 5.2, "New Caledonia", "281 km E of Vao, New Caledonia"]
        , ["2023-10-26T02:59:00.910Z", "2023-10-26", "02:59:00", -29.9202, -177.4931, 38.66, 5.4, "New Zealand", "Kermadec Islands, New Zealand"]
        , ["2023-10-23T23:02:13.763Z", "2023-10-23", "23:02:13", -29.8963, -177.5052, 37.281, 5.2, "New Zealand", "Kermadec Islands, New Zealand"]
        , ["2023-10-23T10:10:15.384Z", "2023-10-23", "10:10:15", -29.9476, -177.5191, 23.092, 6, "New Zealand", "Kermadec Islands, New Zealand"]
        , ["2023-10-23T08:03:13.616Z", "2023-10-23", "08:03:13", -29.951, -177.415, 35, 4.9, "New Zealand", "Kermadec Islands, New Zealand"]
        , ["2023-10-21T06:00:36.882Z", "2023-10-21", "06:00:36", 22.7178, 59.8297, 10, 4.8, "Oman", "35 km ENE of Sur, Oman"]
        , ["2023-10-24T10:10:07.647Z", "2023-10-24", "10:10:07", 5.798, -82.4066, 10, 5, "Panama", "243 km SSW of Río Grande, Panama"]
        , ["2023-10-25T03:49:23.206Z", "2023-10-25", "03:49:23", -6.4611, 146.5797, 69.599, 5.2, "Papua New Guinea", "54 km WNW of Lae, Papua New Guinea"]
        , ["2023-10-23T23:24:47.826Z", "2023-10-23", "23:24:47", -7.0648, 146.909, 53.999, 5.3, "Papua New Guinea", "33 km ENE of Bulolo, Papua New Guinea"]
        , ["2023-10-23T16:47:01.204Z", "2023-10-23", "16:47:01", -5.6264, 146.1056, 89.316, 4.6, "Papua New Guinea", "57 km SE of Madang, Papua New Guinea"]
        , ["2023-10-22T22:29:56.249Z", "2023-10-22", "22:29:56", -7.0495, 155.3124, 10, 4.5, "Papua New Guinea", "83 km SSW of Panguna, Papua New Guinea"]
        , ["2023-10-21T16:22:46.371Z", "2023-10-21", "16:22:46", -4.3773, 153.4935, 107.286, 4.5, "Papua New Guinea", "136 km E of Kokopo, Papua New Guinea"]
        , ["2023-10-21T00:11:38.310Z", "2023-10-21", "00:11:38", -2.4646, 146.4255, 10, 4.8, "Papua New Guinea", "105 km WSW of Lorengau, Papua New Guinea"]
        , ["2023-10-20T19:34:02.111Z", "2023-10-20", "19:34:02", -5.4912, 150.2567, 124.504, 4.9, "Papua New Guinea", "14 km ENE of Kimbe, Papua New Guinea"]
        , ["2023-10-26T19:51:17.145Z", "2023-10-26", "19:51:17", 10.6177, 126.8705, 10, 5.1, "Philippines", "112 km NE of Santa Monica, Philippines"]
        , ["2023-10-21T15:21:43.061Z", "2023-10-21", "15:21:43", 9.1139, 126.5818, 35, 4.6, "Philippines", "37 km ENE of La Paz, Philippines"]
        , ["2023-10-21T05:32:47.538Z", "2023-10-21", "05:32:47", 9.1336, 126.5205, 59.322, 4.6, "Philippines", "32 km ENE of La Paz, Philippines"]
        , ["2023-10-23T12:58:02.440Z", "2023-10-23", "12:58:02", 17.9988, -66.8058, 10, 4.45, "Puerto Rico", "1 km ENE of Indios, Puerto Rico"]
        , ["2023-10-26T16:05:11.437Z", "2023-10-26", "16:05:11", 56.0543, 164.7466, 2.364, 5.9, "Russia", "142 km E of Ust’-Kamchatsk Staryy, Russia"]
        , ["2023-10-24T22:02:51.280Z", "2023-10-24", "22:02:51", 49.2311, 154.9157, 72.453, 4.8, "Russia", "182 km SSW of Severo-Kuril’sk, Russia"]
        , ["2023-10-24T15:34:49.155Z", "2023-10-24", "15:34:49", 54.4542, 162.3952, 10, 4.8, "Russia", "197 km S of Ust’-Kamchatsk Staryy, Russia"]
        , ["2023-10-23T16:01:31.740Z", "2023-10-23", "16:01:31", 43.8368, 147.6851, 85.835, 4.5, "Russia", "77 km E of Shikotan, Russia"]
        , ["2023-10-20T09:48:42.817Z", "2023-10-20", "09:48:42", 49.0898, 155.1177, 52.762, 4.6, "Russia", "190 km SSW of Severo-Kuril’sk, Russia"]
        , ["2023-10-25T14:37:17.118Z", "2023-10-25", "14:37:17", -9.2455, 159.213, 5.323, 5.1, "Solomon Islands", "74 km NW of Malango, Solomon Islands"]
        , ["2023-10-25T13:24:59.598Z", "2023-10-25", "13:24:59", 1.0297, 124.831, 141.838, 5.2, "Indonesia", "Minahasa, Sulawesi, Indonesia"]
        , ["2023-10-26T05:44:19.794Z", "2023-10-26", "05:44:19", -7.0984, 129.2594, 165.173, 5.5, "Timor Leste", "294 km ENE of Lospalos, Timor Leste"]
        , ["2023-10-25T09:15:12.372Z", "2023-10-25", "09:15:12", -20.5856, -177.7926, 511.94, 4.7, "Tonga", "267 km WNW of Houma, Tonga"]
        , ["2023-10-23T10:31:33.622Z", "2023-10-23", "10:31:33", -15.0307, -176.1431, 322.211, 5.2, "Wallis and Futuna", "193 km S of Mata-Utu, Wallis and Futuna"]
        ]
