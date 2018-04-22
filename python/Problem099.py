#!/usr/bin/env python3

#  Copyright (C) 2014  Alexander Gude - alex.public.account+ProjectEulerSolutions@gmail.com
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
#  The most recent version of this program is available at:
#  https://github.com/agude/Project-Euler

"""
Comparing two numbers written in index form like 211 and 37 is not difficult,
as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more
difficult, as both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a
base,exponent pair on each line, determine which line number has the greatest
numerical value.

NOTE: The first two lines in the file represent the numbers in the example
given above.
"""

from collections import namedtuple
from math import log
from time import time


INPUT_DATA = [
    (519432, 525806, 1),
    (632382, 518061, 2),
    (78864, 613712, 3),
    (466580, 530130, 4),
    (780495, 510032, 5),
    (525895, 525320, 6),
    (15991, 714883, 7),
    (960290, 502358, 8),
    (760018, 511029, 9),
    (166800, 575487, 10),
    (210884, 564478, 11),
    (555151, 523163, 12),
    (681146, 515199, 13),
    (563395, 522587, 14),
    (738250, 512126, 15),
    (923525, 503780, 16),
    (595148, 520429, 17),
    (177108, 572629, 18),
    (750923, 511482, 19),
    (440902, 532446, 20),
    (881418, 505504, 21),
    (422489, 534197, 22),
    (979858, 501616, 23),
    (685893, 514935, 24),
    (747477, 511661, 25),
    (167214, 575367, 26),
    (234140, 559696, 27),
    (940238, 503122, 28),
    (728969, 512609, 29),
    (232083, 560102, 30),
    (900971, 504694, 31),
    (688801, 514772, 32),
    (189664, 569402, 33),
    (891022, 505104, 34),
    (445689, 531996, 35),
    (119570, 591871, 36),
    (821453, 508118, 37),
    (371084, 539600, 38),
    (911745, 504251, 39),
    (623655, 518600, 40),
    (144361, 582486, 41),
    (352442, 541775, 42),
    (420726, 534367, 43),
    (295298, 549387, 44),
    (6530, 787777, 45),
    (468397, 529976, 46),
    (672336, 515696, 47),
    (431861, 533289, 48),
    (84228, 610150, 49),
    (805376, 508857, 50),
    (444409, 532117, 51),
    (33833, 663511, 52),
    (381850, 538396, 53),
    (402931, 536157, 54),
    (92901, 604930, 55),
    (304825, 548004, 56),
    (731917, 512452, 57),
    (753734, 511344, 58),
    (51894, 637373, 59),
    (151578, 580103, 60),
    (295075, 549421, 61),
    (303590, 548183, 62),
    (333594, 544123, 63),
    (683952, 515042, 64),
    (60090, 628880, 65),
    (951420, 502692, 66),
    (28335, 674991, 67),
    (714940, 513349, 68),
    (343858, 542826, 69),
    (549279, 523586, 70),
    (804571, 508887, 71),
    (260653, 554881, 72),
    (291399, 549966, 73),
    (402342, 536213, 74),
    (408889, 535550, 75),
    (40328, 652524, 76),
    (375856, 539061, 77),
    (768907, 510590, 78),
    (165993, 575715, 79),
    (976327, 501755, 80),
    (898500, 504795, 81),
    (360404, 540830, 82),
    (478714, 529095, 83),
    (694144, 514472, 84),
    (488726, 528258, 85),
    (841380, 507226, 86),
    (328012, 544839, 87),
    (22389, 690868, 88),
    (604053, 519852, 89),
    (329514, 544641, 90),
    (772965, 510390, 91),
    (492798, 527927, 92),
    (30125, 670983, 93),
    (895603, 504906, 94),
    (450785, 531539, 95),
    (840237, 507276, 96),
    (380711, 538522, 97),
    (63577, 625673, 98),
    (76801, 615157, 99),
    (502694, 527123, 100),
    (597706, 520257, 101),
    (310484, 547206, 102),
    (944468, 502959, 103),
    (121283, 591152, 104),
    (451131, 531507, 105),
    (566499, 522367, 106),
    (425373, 533918, 107),
    (40240, 652665, 108),
    (39130, 654392, 109),
    (714926, 513355, 110),
    (469219, 529903, 111),
    (806929, 508783, 112),
    (287970, 550487, 113),
    (92189, 605332, 114),
    (103841, 599094, 115),
    (671839, 515725, 116),
    (452048, 531421, 117),
    (987837, 501323, 118),
    (935192, 503321, 119),
    (88585, 607450, 120),
    (613883, 519216, 121),
    (144551, 582413, 122),
    (647359, 517155, 123),
    (213902, 563816, 124),
    (184120, 570789, 125),
    (258126, 555322, 126),
    (502546, 527130, 127),
    (407655, 535678, 128),
    (401528, 536306, 129),
    (477490, 529193, 130),
    (841085, 507237, 131),
    (732831, 512408, 132),
    (833000, 507595, 133),
    (904694, 504542, 134),
    (581435, 521348, 135),
    (455545, 531110, 136),
    (873558, 505829, 137),
    (94916, 603796, 138),
    (720176, 513068, 139),
    (545034, 523891, 140),
    (246348, 557409, 141),
    (556452, 523079, 142),
    (832015, 507634, 143),
    (173663, 573564, 144),
    (502634, 527125, 145),
    (250732, 556611, 146),
    (569786, 522139, 147),
    (216919, 563178, 148),
    (521815, 525623, 149),
    (92304, 605270, 150),
    (164446, 576167, 151),
    (753413, 511364, 152),
    (11410, 740712, 153),
    (448845, 531712, 154),
    (925072, 503725, 155),
    (564888, 522477, 156),
    (7062, 780812, 157),
    (641155, 517535, 158),
    (738878, 512100, 159),
    (636204, 517828, 160),
    (372540, 539436, 161),
    (443162, 532237, 162),
    (571192, 522042, 163),
    (655350, 516680, 164),
    (299741, 548735, 165),
    (581914, 521307, 166),
    (965471, 502156, 167),
    (513441, 526277, 168),
    (808682, 508700, 169),
    (237589, 559034, 170),
    (543300, 524025, 171),
    (804712, 508889, 172),
    (247511, 557192, 173),
    (543486, 524008, 174),
    (504383, 526992, 175),
    (326529, 545039, 176),
    (792493, 509458, 177),
    (86033, 609017, 178),
    (126554, 589005, 179),
    (579379, 521481, 180),
    (948026, 502823, 181),
    (404777, 535969, 182),
    (265767, 554022, 183),
    (266876, 553840, 184),
    (46631, 643714, 185),
    (492397, 527958, 186),
    (856106, 506581, 187),
    (795757, 509305, 188),
    (748946, 511584, 189),
    (294694, 549480, 190),
    (409781, 535463, 191),
    (775887, 510253, 192),
    (543747, 523991, 193),
    (210592, 564536, 194),
    (517119, 525990, 195),
    (520253, 525751, 196),
    (247926, 557124, 197),
    (592141, 520626, 198),
    (346580, 542492, 199),
    (544969, 523902, 200),
    (506501, 526817, 201),
    (244520, 557738, 202),
    (144745, 582349, 203),
    (69274, 620858, 204),
    (292620, 549784, 205),
    (926027, 503687, 206),
    (736320, 512225, 207),
    (515528, 526113, 208),
    (407549, 535688, 209),
    (848089, 506927, 210),
    (24141, 685711, 211),
    (9224, 757964, 212),
    (980684, 501586, 213),
    (175259, 573121, 214),
    (489160, 528216, 215),
    (878970, 505604, 216),
    (969546, 502002, 217),
    (525207, 525365, 218),
    (690461, 514675, 219),
    (156510, 578551, 220),
    (659778, 516426, 221),
    (468739, 529945, 222),
    (765252, 510770, 223),
    (76703, 615230, 224),
    (165151, 575959, 225),
    (29779, 671736, 226),
    (928865, 503569, 227),
    (577538, 521605, 228),
    (927555, 503618, 229),
    (185377, 570477, 230),
    (974756, 501809, 231),
    (800130, 509093, 232),
    (217016, 563153, 233),
    (365709, 540216, 234),
    (774508, 510320, 235),
    (588716, 520851, 236),
    (631673, 518104, 237),
    (954076, 502590, 238),
    (777828, 510161, 239),
    (990659, 501222, 240),
    (597799, 520254, 241),
    (786905, 509727, 242),
    (512547, 526348, 243),
    (756449, 511212, 244),
    (869787, 505988, 245),
    (653747, 516779, 246),
    (84623, 609900, 247),
    (839698, 507295, 248),
    (30159, 670909, 249),
    (797275, 509234, 250),
    (678136, 515373, 251),
    (897144, 504851, 252),
    (989554, 501263, 253),
    (413292, 535106, 254),
    (55297, 633667, 255),
    (788650, 509637, 256),
    (486748, 528417, 257),
    (150724, 580377, 258),
    (56434, 632490, 259),
    (77207, 614869, 260),
    (588631, 520859, 261),
    (611619, 519367, 262),
    (100006, 601055, 263),
    (528924, 525093, 264),
    (190225, 569257, 265),
    (851155, 506789, 266),
    (682593, 515114, 267),
    (613043, 519275, 268),
    (514673, 526183, 269),
    (877634, 505655, 270),
    (878905, 505602, 271),
    (1926, 914951, 272),
    (613245, 519259, 273),
    (152481, 579816, 274),
    (841774, 507203, 275),
    (71060, 619442, 276),
    (865335, 506175, 277),
    (90244, 606469, 278),
    (302156, 548388, 279),
    (399059, 536557, 280),
    (478465, 529113, 281),
    (558601, 522925, 282),
    (69132, 620966, 283),
    (267663, 553700, 284),
    (988276, 501310, 285),
    (378354, 538787, 286),
    (529909, 525014, 287),
    (161733, 576968, 288),
    (758541, 511109, 289),
    (823425, 508024, 290),
    (149821, 580667, 291),
    (269258, 553438, 292),
    (481152, 528891, 293),
    (120871, 591322, 294),
    (972322, 501901, 295),
    (981350, 501567, 296),
    (676129, 515483, 297),
    (950860, 502717, 298),
    (119000, 592114, 299),
    (392252, 537272, 300),
    (191618, 568919, 301),
    (946699, 502874, 302),
    (289555, 550247, 303),
    (799322, 509139, 304),
    (703886, 513942, 305),
    (194812, 568143, 306),
    (261823, 554685, 307),
    (203052, 566221, 308),
    (217330, 563093, 309),
    (734748, 512313, 310),
    (391759, 537328, 311),
    (807052, 508777, 312),
    (564467, 522510, 313),
    (59186, 629748, 314),
    (113447, 594545, 315),
    (518063, 525916, 316),
    (905944, 504492, 317),
    (613922, 519213, 318),
    (439093, 532607, 319),
    (445946, 531981, 320),
    (230530, 560399, 321),
    (297887, 549007, 322),
    (459029, 530797, 323),
    (403692, 536075, 324),
    (855118, 506616, 325),
    (963127, 502245, 326),
    (841711, 507208, 327),
    (407411, 535699, 328),
    (924729, 503735, 329),
    (914823, 504132, 330),
    (333725, 544101, 331),
    (176345, 572832, 332),
    (912507, 504225, 333),
    (411273, 535308, 334),
    (259774, 555036, 335),
    (632853, 518038, 336),
    (119723, 591801, 337),
    (163902, 576321, 338),
    (22691, 689944, 339),
    (402427, 536212, 340),
    (175769, 572988, 341),
    (837260, 507402, 342),
    (603432, 519893, 343),
    (313679, 546767, 344),
    (538165, 524394, 345),
    (549026, 523608, 346),
    (61083, 627945, 347),
    (898345, 504798, 348),
    (992556, 501153, 349),
    (369999, 539727, 350),
    (32847, 665404, 351),
    (891292, 505088, 352),
    (152715, 579732, 353),
    (824104, 507997, 354),
    (234057, 559711, 355),
    (730507, 512532, 356),
    (960529, 502340, 357),
    (388395, 537687, 358),
    (958170, 502437, 359),
    (57105, 631806, 360),
    (186025, 570311, 361),
    (993043, 501133, 362),
    (576770, 521664, 363),
    (215319, 563513, 364),
    (927342, 503628, 365),
    (521353, 525666, 366),
    (39563, 653705, 367),
    (752516, 511408, 368),
    (110755, 595770, 369),
    (309749, 547305, 370),
    (374379, 539224, 371),
    (919184, 503952, 372),
    (990652, 501226, 373),
    (647780, 517135, 374),
    (187177, 570017, 375),
    (168938, 574877, 376),
    (649558, 517023, 377),
    (278126, 552016, 378),
    (162039, 576868, 379),
    (658512, 516499, 380),
    (498115, 527486, 381),
    (896583, 504868, 382),
    (561170, 522740, 383),
    (747772, 511647, 384),
    (775093, 510294, 385),
    (652081, 516882, 386),
    (724905, 512824, 387),
    (499707, 527365, 388),
    (47388, 642755, 389),
    (646668, 517204, 390),
    (571700, 522007, 391),
    (180430, 571747, 392),
    (710015, 513617, 393),
    (435522, 532941, 394),
    (98137, 602041, 395),
    (759176, 511070, 396),
    (486124, 528467, 397),
    (526942, 525236, 398),
    (878921, 505604, 399),
    (408313, 535602, 400),
    (926980, 503640, 401),
    (882353, 505459, 402),
    (566887, 522345, 403),
    (3326, 853312, 404),
    (911981, 504248, 405),
    (416309, 534800, 406),
    (392991, 537199, 407),
    (622829, 518651, 408),
    (148647, 581055, 409),
    (496483, 527624, 410),
    (666314, 516044, 411),
    (48562, 641293, 412),
    (672618, 515684, 413),
    (443676, 532187, 414),
    (274065, 552661, 415),
    (265386, 554079, 416),
    (347668, 542358, 417),
    (31816, 667448, 418),
    (181575, 571446, 419),
    (961289, 502320, 420),
    (365689, 540214, 421),
    (987950, 501317, 422),
    (932299, 503440, 423),
    (27388, 677243, 424),
    (746701, 511701, 425),
    (492258, 527969, 426),
    (147823, 581323, 427),
    (57918, 630985, 428),
    (838849, 507333, 429),
    (678038, 515375, 430),
    (27852, 676130, 431),
    (850241, 506828, 432),
    (818403, 508253, 433),
    (131717, 587014, 434),
    (850216, 506834, 435),
    (904848, 504529, 436),
    (189758, 569380, 437),
    (392845, 537217, 438),
    (470876, 529761, 439),
    (925353, 503711, 440),
    (285431, 550877, 441),
    (454098, 531234, 442),
    (823910, 508003, 443),
    (318493, 546112, 444),
    (766067, 510730, 445),
    (261277, 554775, 446),
    (421530, 534289, 447),
    (694130, 514478, 448),
    (120439, 591498, 449),
    (213308, 563949, 450),
    (854063, 506662, 451),
    (365255, 540263, 452),
    (165437, 575872, 453),
    (662240, 516281, 454),
    (289970, 550181, 455),
    (847977, 506933, 456),
    (546083, 523816, 457),
    (413252, 535113, 458),
    (975829, 501767, 459),
    (361540, 540701, 460),
    (235522, 559435, 461),
    (224643, 561577, 462),
    (736350, 512229, 463),
    (328303, 544808, 464),
    (35022, 661330, 465),
    (307838, 547578, 466),
    (474366, 529458, 467),
    (873755, 505819, 468),
    (73978, 617220, 469),
    (827387, 507845, 470),
    (670830, 515791, 471),
    (326511, 545034, 472),
    (309909, 547285, 473),
    (400970, 536363, 474),
    (884827, 505352, 475),
    (718307, 513175, 476),
    (28462, 674699, 477),
    (599384, 520150, 478),
    (253565, 556111, 479),
    (284009, 551093, 480),
    (343403, 542876, 481),
    (446557, 531921, 482),
    (992372, 501160, 483),
    (961601, 502308, 484),
    (696629, 514342, 485),
    (919537, 503945, 486),
    (894709, 504944, 487),
    (892201, 505051, 488),
    (358160, 541097, 489),
    (448503, 531745, 490),
    (832156, 507636, 491),
    (920045, 503924, 492),
    (926137, 503675, 493),
    (416754, 534757, 494),
    (254422, 555966, 495),
    (92498, 605151, 496),
    (826833, 507873, 497),
    (660716, 516371, 498),
    (689335, 514746, 499),
    (160045, 577467, 500),
    (814642, 508425, 501),
    (969939, 501993, 502),
    (242856, 558047, 503),
    (76302, 615517, 504),
    (472083, 529653, 505),
    (587101, 520964, 506),
    (99066, 601543, 507),
    (498005, 527503, 508),
    (709800, 513624, 509),
    (708000, 513716, 510),
    (20171, 698134, 511),
    (285020, 550936, 512),
    (266564, 553891, 513),
    (981563, 501557, 514),
    (846502, 506991, 515),
    (334, 1190800, 516),
    (209268, 564829, 517),
    (9844, 752610, 518),
    (996519, 501007, 519),
    (410059, 535426, 520),
    (432931, 533188, 521),
    (848012, 506929, 522),
    (966803, 502110, 523),
    (983434, 501486, 524),
    (160700, 577267, 525),
    (504374, 526989, 526),
    (832061, 507640, 527),
    (392825, 537214, 528),
    (443842, 532165, 529),
    (440352, 532492, 530),
    (745125, 511776, 531),
    (13718, 726392, 532),
    (661753, 516312, 533),
    (70500, 619875, 534),
    (436952, 532814, 535),
    (424724, 533973, 536),
    (21954, 692224, 537),
    (262490, 554567, 538),
    (716622, 513264, 539),
    (907584, 504425, 540),
    (60086, 628882, 541),
    (837123, 507412, 542),
    (971345, 501940, 543),
    (947162, 502855, 544),
    (139920, 584021, 545),
    (68330, 621624, 546),
    (666452, 516038, 547),
    (731446, 512481, 548),
    (953350, 502619, 549),
    (183157, 571042, 550),
    (845400, 507045, 551),
    (651548, 516910, 552),
    (20399, 697344, 553),
    (861779, 506331, 554),
    (629771, 518229, 555),
    (801706, 509026, 556),
    (189207, 569512, 557),
    (737501, 512168, 558),
    (719272, 513115, 559),
    (479285, 529045, 560),
    (136046, 585401, 561),
    (896746, 504860, 562),
    (891735, 505067, 563),
    (684771, 514999, 564),
    (865309, 506184, 565),
    (379066, 538702, 566),
    (503117, 527090, 567),
    (621780, 518717, 568),
    (209518, 564775, 569),
    (677135, 515423, 570),
    (987500, 501340, 571),
    (197049, 567613, 572),
    (329315, 544673, 573),
    (236756, 559196, 574),
    (357092, 541226, 575),
    (520440, 525733, 576),
    (213471, 563911, 577),
    (956852, 502490, 578),
    (702223, 514032, 579),
    (404943, 535955, 580),
    (178880, 572152, 581),
    (689477, 514734, 582),
    (691351, 514630, 583),
    (866669, 506128, 584),
    (370561, 539656, 585),
    (739805, 512051, 586),
    (71060, 619441, 587),
    (624861, 518534, 588),
    (261660, 554714, 589),
    (366137, 540160, 590),
    (166054, 575698, 591),
    (601878, 519990, 592),
    (153445, 579501, 593),
    (279899, 551729, 594),
    (379166, 538691, 595),
    (423209, 534125, 596),
    (675310, 515526, 597),
    (145641, 582050, 598),
    (691353, 514627, 599),
    (917468, 504026, 600),
    (284778, 550976, 601),
    (81040, 612235, 602),
    (161699, 576978, 603),
    (616394, 519057, 604),
    (767490, 510661, 605),
    (156896, 578431, 606),
    (427408, 533714, 607),
    (254849, 555884, 608),
    (737217, 512182, 609),
    (897133, 504851, 610),
    (203815, 566051, 611),
    (270822, 553189, 612),
    (135854, 585475, 613),
    (778805, 510111, 614),
    (784373, 509847, 615),
    (305426, 547921, 616),
    (733418, 512375, 617),
    (732087, 512448, 618),
    (540668, 524215, 619),
    (702898, 513996, 620),
    (628057, 518328, 621),
    (640280, 517587, 622),
    (422405, 534204, 623),
    (10604, 746569, 624),
    (746038, 511733, 625),
    (839808, 507293, 626),
    (457417, 530938, 627),
    (479030, 529064, 628),
    (341758, 543090, 629),
    (620223, 518824, 630),
    (251661, 556451, 631),
    (561790, 522696, 632),
    (497733, 527521, 633),
    (724201, 512863, 634),
    (489217, 528217, 635),
    (415623, 534867, 636),
    (624610, 518548, 637),
    (847541, 506953, 638),
    (432295, 533249, 639),
    (400391, 536421, 640),
    (961158, 502319, 641),
    (139173, 584284, 642),
    (421225, 534315, 643),
    (579083, 521501, 644),
    (74274, 617000, 645),
    (701142, 514087, 646),
    (374465, 539219, 647),
    (217814, 562985, 648),
    (358972, 540995, 649),
    (88629, 607424, 650),
    (288597, 550389, 651),
    (285819, 550812, 652),
    (538400, 524385, 653),
    (809930, 508645, 654),
    (738326, 512126, 655),
    (955461, 502535, 656),
    (163829, 576343, 657),
    (826475, 507891, 658),
    (376488, 538987, 659),
    (102234, 599905, 660),
    (114650, 594002, 661),
    (52815, 636341, 662),
    (434037, 533082, 663),
    (804744, 508880, 664),
    (98385, 601905, 665),
    (856620, 506559, 666),
    (220057, 562517, 667),
    (844734, 507078, 668),
    (150677, 580387, 669),
    (558697, 522917, 670),
    (621751, 518719, 671),
    (207067, 565321, 672),
    (135297, 585677, 673),
    (932968, 503404, 674),
    (604456, 519822, 675),
    (579728, 521462, 676),
    (244138, 557813, 677),
    (706487, 513800, 678),
    (711627, 513523, 679),
    (853833, 506674, 680),
    (497220, 527562, 681),
    (59428, 629511, 682),
    (564845, 522486, 683),
    (623621, 518603, 684),
    (242689, 558077, 685),
    (125091, 589591, 686),
    (363819, 540432, 687),
    (686453, 514901, 688),
    (656813, 516594, 689),
    (489901, 528155, 690),
    (386380, 537905, 691),
    (542819, 524052, 692),
    (243987, 557841, 693),
    (693412, 514514, 694),
    (488484, 528271, 695),
    (896331, 504881, 696),
    (336730, 543721, 697),
    (728298, 512647, 698),
    (604215, 519840, 699),
    (153729, 579413, 700),
    (595687, 520398, 701),
    (540360, 524240, 702),
    (245779, 557511, 703),
    (924873, 503730, 704),
    (509628, 526577, 705),
    (528523, 525122, 706),
    (3509, 847707, 707),
    (522756, 525555, 708),
    (895447, 504922, 709),
    (44840, 646067, 710),
    (45860, 644715, 711),
    (463487, 530404, 712),
    (398164, 536654, 713),
    (894483, 504959, 714),
    (619415, 518874, 715),
    (966306, 502129, 716),
    (990922, 501212, 717),
    (835756, 507474, 718),
    (548881, 523618, 719),
    (453578, 531282, 720),
    (474993, 529410, 721),
    (80085, 612879, 722),
    (737091, 512193, 723),
    (50789, 638638, 724),
    (979768, 501620, 725),
    (792018, 509483, 726),
    (665001, 516122, 727),
    (86552, 608694, 728),
    (462772, 530469, 729),
    (589233, 520821, 730),
    (891694, 505072, 731),
    (592605, 520594, 732),
    (209645, 564741, 733),
    (42531, 649269, 734),
    (554376, 523226, 735),
    (803814, 508929, 736),
    (334157, 544042, 737),
    (175836, 572970, 738),
    (868379, 506051, 739),
    (658166, 516520, 740),
    (278203, 551995, 741),
    (966198, 502126, 742),
    (627162, 518387, 743),
    (296774, 549165, 744),
    (311803, 547027, 745),
    (843797, 507118, 746),
    (702304, 514032, 747),
    (563875, 522553, 748),
    (33103, 664910, 749),
    (191932, 568841, 750),
    (543514, 524006, 751),
    (506835, 526794, 752),
    (868368, 506052, 753),
    (847025, 506971, 754),
    (678623, 515342, 755),
    (876139, 505726, 756),
    (571997, 521984, 757),
    (598632, 520198, 758),
    (213590, 563892, 759),
    (625404, 518497, 760),
    (726508, 512738, 761),
    (689426, 514738, 762),
    (332495, 544264, 763),
    (411366, 535302, 764),
    (242546, 558110, 765),
    (315209, 546555, 766),
    (797544, 509219, 767),
    (93889, 604371, 768),
    (858879, 506454, 769),
    (124906, 589666, 770),
    (449072, 531693, 771),
    (235960, 559345, 772),
    (642403, 517454, 773),
    (720567, 513047, 774),
    (705534, 513858, 775),
    (603692, 519870, 776),
    (488137, 528302, 777),
    (157370, 578285, 778),
    (63515, 625730, 779),
    (666326, 516041, 780),
    (619226, 518883, 781),
    (443613, 532186, 782),
    (597717, 520257, 783),
    (96225, 603069, 784),
    (86940, 608450, 785),
    (40725, 651929, 786),
    (460976, 530625, 787),
    (268875, 553508, 788),
    (270671, 553214, 789),
    (363254, 540500, 790),
    (384248, 538137, 791),
    (762889, 510892, 792),
    (377941, 538833, 793),
    (278878, 551890, 794),
    (176615, 572755, 795),
    (860008, 506412, 796),
    (944392, 502967, 797),
    (608395, 519571, 798),
    (225283, 561450, 799),
    (45095, 645728, 800),
    (333798, 544090, 801),
    (625733, 518476, 802),
    (995584, 501037, 803),
    (506135, 526853, 804),
    (238050, 558952, 805),
    (557943, 522972, 806),
    (530978, 524938, 807),
    (634244, 517949, 808),
    (177168, 572616, 809),
    (85200, 609541, 810),
    (953043, 502630, 811),
    (523661, 525484, 812),
    (999295, 500902, 813),
    (840803, 507246, 814),
    (961490, 502312, 815),
    (471747, 529685, 816),
    (380705, 538523, 817),
    (911180, 504275, 818),
    (334149, 544046, 819),
    (478992, 529065, 820),
    (325789, 545133, 821),
    (335884, 543826, 822),
    (426976, 533760, 823),
    (749007, 511582, 824),
    (667067, 516000, 825),
    (607586, 519623, 826),
    (674054, 515599, 827),
    (188534, 569675, 828),
    (565185, 522464, 829),
    (172090, 573988, 830),
    (87592, 608052, 831),
    (907432, 504424, 832),
    (8912, 760841, 833),
    (928318, 503590, 834),
    (757917, 511138, 835),
    (718693, 513153, 836),
    (315141, 546566, 837),
    (728326, 512645, 838),
    (353492, 541647, 839),
    (638429, 517695, 840),
    (628892, 518280, 841),
    (877286, 505672, 842),
    (620895, 518778, 843),
    (385878, 537959, 844),
    (423311, 534113, 845),
    (633501, 517997, 846),
    (884833, 505360, 847),
    (883402, 505416, 848),
    (999665, 500894, 849),
    (708395, 513697, 850),
    (548142, 523667, 851),
    (756491, 511205, 852),
    (987352, 501340, 853),
    (766520, 510705, 854),
    (591775, 520647, 855),
    (833758, 507563, 856),
    (843890, 507108, 857),
    (925551, 503698, 858),
    (74816, 616598, 859),
    (646942, 517187, 860),
    (354923, 541481, 861),
    (256291, 555638, 862),
    (634470, 517942, 863),
    (930904, 503494, 864),
    (134221, 586071, 865),
    (282663, 551304, 866),
    (986070, 501394, 867),
    (123636, 590176, 868),
    (123678, 590164, 869),
    (481717, 528841, 870),
    (423076, 534137, 871),
    (866246, 506145, 872),
    (93313, 604697, 873),
    (783632, 509880, 874),
    (317066, 546304, 875),
    (502977, 527103, 876),
    (141272, 583545, 877),
    (71708, 618938, 878),
    (617748, 518975, 879),
    (581190, 521362, 880),
    (193824, 568382, 881),
    (682368, 515131, 882),
    (352956, 541712, 883),
    (351375, 541905, 884),
    (505362, 526909, 885),
    (905165, 504518, 886),
    (128645, 588188, 887),
    (267143, 553787, 888),
    (158409, 577965, 889),
    (482776, 528754, 890),
    (628896, 518282, 891),
    (485233, 528547, 892),
    (563606, 522574, 893),
    (111001, 595655, 894),
    (115920, 593445, 895),
    (365510, 540237, 896),
    (959724, 502374, 897),
    (938763, 503184, 898),
    (930044, 503520, 899),
    (970959, 501956, 900),
    (913658, 504176, 901),
    (68117, 621790, 902),
    (989729, 501253, 903),
    (567697, 522288, 904),
    (820427, 508163, 905),
    (54236, 634794, 906),
    (291557, 549938, 907),
    (124961, 589646, 908),
    (403177, 536130, 909),
    (405421, 535899, 910),
    (410233, 535417, 911),
    (815111, 508403, 912),
    (213176, 563974, 913),
    (83099, 610879, 914),
    (998588, 500934, 915),
    (513640, 526263, 916),
    (129817, 587733, 917),
    (1820, 921851, 918),
    (287584, 550539, 919),
    (299160, 548820, 920),
    (860621, 506386, 921),
    (529258, 525059, 922),
    (586297, 521017, 923),
    (953406, 502616, 924),
    (441234, 532410, 925),
    (986217, 501386, 926),
    (781938, 509957, 927),
    (461247, 530595, 928),
    (735424, 512277, 929),
    (146623, 581722, 930),
    (839838, 507288, 931),
    (510667, 526494, 932),
    (935085, 503327, 933),
    (737523, 512167, 934),
    (303455, 548204, 935),
    (992779, 501145, 936),
    (60240, 628739, 937),
    (939095, 503174, 938),
    (794368, 509370, 939),
    (501825, 527189, 940),
    (459028, 530798, 941),
    (884641, 505363, 942),
    (512287, 526364, 943),
    (835165, 507499, 944),
    (307723, 547590, 945),
    (160587, 577304, 946),
    (735043, 512300, 947),
    (493289, 527887, 948),
    (110717, 595785, 949),
    (306480, 547772, 950),
    (318593, 546089, 951),
    (179810, 571911, 952),
    (200531, 566799, 953),
    (314999, 546580, 954),
    (197020, 567622, 955),
    (301465, 548487, 956),
    (237808, 559000, 957),
    (131944, 586923, 958),
    (882527, 505449, 959),
    (468117, 530003, 960),
    (711319, 513541, 961),
    (156240, 578628, 962),
    (965452, 502162, 963),
    (992756, 501148, 964),
    (437959, 532715, 965),
    (739938, 512046, 966),
    (614249, 519196, 967),
    (391496, 537356, 968),
    (62746, 626418, 969),
    (688215, 514806, 970),
    (75501, 616091, 971),
    (883573, 505412, 972),
    (558824, 522910, 973),
    (759371, 511061, 974),
    (173913, 573489, 975),
    (891351, 505089, 976),
    (727464, 512693, 977),
    (164833, 576051, 978),
    (812317, 508529, 979),
    (540320, 524243, 980),
    (698061, 514257, 981),
    (69149, 620952, 982),
    (471673, 529694, 983),
    (159092, 577753, 984),
    (428134, 533653, 985),
    (89997, 606608, 986),
    (711061, 513557, 987),
    (779403, 510081, 988),
    (203327, 566155, 989),
    (798176, 509187, 990),
    (667688, 515963, 991),
    (636120, 517833, 992),
    (137410, 584913, 993),
    (217615, 563034, 994),
    (556887, 523038, 995),
    (667229, 515991, 996),
    (672276, 515708, 997),
    (325361, 545187, 998),
    (172115, 573985, 999),
    (13846, 725685, 1000),
]


# A named tuples to store the computed number and the line it came from
NumberAndLine = namedtuple("NumberAndLine", ["number", "line_number"])


def problem_099(input_data=INPUT_DATA):
    start_time = time()

    # We observe that log(base^power) = power * log(base), and that since log
    # is monotonically increasing if a > b then log(a) > log(b). Then we
    # compute power * log(base) and find the largest.
    biggest = NumberAndLine(0, None)
    for base, power, line_number in input_data:
        large_number = power * log(base)
        new_number = NumberAndLine(large_number, line_number)

        biggest = max(biggest, new_number)

    end_time = time() - start_time

    answer = biggest.line_number

    print(answer, 'in', end_time, 'secs')
    return answer

# Only runs if executed directly
if __name__ == '__main__':

    problem_099(INPUT_DATA)
