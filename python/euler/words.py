from typing import FrozenSet


def is_basic_word(word: str) -> bool:
    """Returns true if the word is in the basic word list.

    This function compares a lowercased version of the input word to the
    Wikipedia Basic English Combined Word List as found here:
    http://simple.wikipedia.org/wiki/Wikipedia:Basic_English_combined_wordlist

    Args:
        word (str): The word to check. It will be lowercased for the
            comparison.

    Returns:
        bool: True if the word is in the basic word list, False otherwise.
    """
    lower_word: str = str(word).lower()
    return lower_word in BASIC_WORDS

# This wordlist comes from Wikipedia:
# http://simple.wikipedia.org/wiki/Wikipedia:Basic_English_combined_wordlist
BASIC_WORDS: FrozenSet[str] = frozenset(
    (
        "a",
        "able",
        "about",
        "absence",
        "absorption",
        "acceleration",
        "acceptance",
        "accessory",
        "accident",
        "account",
        "acid",
        "across",
        "act",
        "acting",
        "active",
        "actor",
        "addition",
        "address",
        "adjacent",
        "adjustment",
        "adventure",
        "advertisement",
        "advice",
        "after",
        "afterthought",
        "again",
        "against",
        "age",
        "agency",
        "agent",
        "ago",
        "agreement",
        "air",
        "airplane",
        "alcohol",
        "algebra",
        "all",
        "allowance",
        "almost",
        "along",
        "also",
        "alternative",
        "aluminium",
        "always",
        "ambition",
        "ammonia",
        "among",
        "amount",
        "amplitude",
        "amusement",
        "anchor",
        "and",
        "anesthetic",
        "angle",
        "angry",
        "animal",
        "ankle",
        "another",
        "answer",
        "ant",
        "any",
        "anybody",
        "anyhow",
        "anyone",
        "anything",
        "anywhere",
        "apparatus",
        "appendage",
        "apple",
        "application",
        "approval",
        "approximation",
        "april",
        "arbitrary",
        "arbitration",
        "arc",
        "arch",
        "area",
        "argument",
        "arithmetic",
        "arm",
        "army",
        "arrangement",
        "art",
        "as",
        "asbestos",
        "ash",
        "asset",
        "assistant",
        "at",
        "attack",
        "attempt",
        "attention",
        "attraction",
        "august",
        "authority",
        "autobus",
        "automatic",
        "automobile",
        "average",
        "awake",
        "awkward",
        "axis",
        "baby",
        "back",
        "backbone",
        "backwoods",
        "bad",
        "bag",
        "balance",
        "balcony",
        "bale",
        "ball",
        "ballet",
        "band",
        "bang",
        "bank",
        "bankrupt",
        "bar",
        "bark",
        "barrel",
        "base",
        "based",
        "basin",
        "basing",
        "basket",
        "bath",
        "be",
        "beak",
        "beaker",
        "beard",
        "beat",
        "beautiful",
        "because",
        "become",
        "bed",
        "bedroom",
        "bee",
        "beef",
        "beer",
        "beeswax",
        "before",
        "behavior",
        "behind",
        "belief",
        "bell",
        "belt",
        "bent",
        "berry",
        "bet",
        "between",
        "bill",
        "biology",
        "bird",
        "birefringence",
        "birth",
        "birthday",
        "birthright",
        "bit",
        "bite",
        "bitter",
        "black",
        "blackberry",
        "blackbird",
        "blackboard",
        "blade",
        "blame",
        "blanket",
        "blood",
        "bloodvessel",
        "blow",
        "blue",
        "bluebell",
        "board",
        "boat",
        "body",
        "boiling",
        "bomb",
        "bone",
        "book",
        "bookkeeper",
        "boot",
        "both",
        "bottle",
        "bottom",
        "box",
        "boy",
        "brain",
        "brake",
        "branch",
        "brass",
        "brave",
        "bread",
        "break",
        "breakfast",
        "breast",
        "breath",
        "brick",
        "bridge",
        "bright",
        "broken",
        "broker",
        "brother",
        "brown",
        "brush",
        "brushwood",
        "bubble",
        "bucket",
        "bud",
        "budget",
        "builder",
        "building",
        "bulb",
        "bunch",
        "buoyancy",
        "burial",
        "burn",
        "burned",
        "burner",
        "burning",
        "burst",
        "business",
        "busy",
        "but",
        "butter",
        "buttercup",
        "button",
        "by",
        "cafe",
        "cake",
        "calculation",
        "calendar",
        "call",
        "camera",
        "canvas",
        "capacity",
        "capital",
        "card",
        "cardboard",
        "care",
        "carefree",
        "caretaker",
        "carpet",
        "carriage",
        "cart",
        "carter",
        "cartilage",
        "case",
        "cast",
        "cat",
        "catarrh",
        "cause",
        "cave",
        "cavity",
        "cell",
        "centi-",
        "ceremony",
        "certain",
        "certificate",
        "chain",
        "chair",
        "chalk",
        "champagne",
        "chance",
        "change",
        "character",
        "charge",
        "chauffeur",
        "cheap",
        "check",
        "cheese",
        "chemical",
        "chemist",
        "chemistry",
        "chest",
        "chief",
        "child",
        "chimney",
        "chin",
        "china",
        "chocolate",
        "choice",
        "chorus",
        "church",
        "cigarette",
        "circle",
        "circuit",
        "circulation",
        "circumference",
        "circus",
        "citron",
        "civilization",
        "claim",
        "claw",
        "clay",
        "clean",
        "clear",
        "cleavage",
        "clever",
        "client",
        "climber",
        "clip",
        "clock",
        "clockwork",
        "cloth",
        "clothier",
        "clothing",
        "cloud",
        "club",
        "coal",
        "coat",
        "cocktail",
        "code",
        "coffee",
        "cognac",
        "coil",
        "cold",
        "collar",
        "collection",
        "college",
        "collision",
        "colony",
        "color",
        "column",
        "comb",
        "combination",
        "combine",
        "come",
        "comfort",
        "committee",
        "common",
        "commonsense",
        "communications",
        "company",
        "comparison",
        "competition",
        "complaint",
        "complete",
        "complex",
        "component",
        "compound",
        "concept",
        "concrete",
        "condition",
        "conductor",
        "congruent",
        "connection",
        "conscious",
        "conservation",
        "consignment",
        "constant",
        "consumer",
        "continuous",
        "contour",
        "control",
        "convenient",
        "conversion",
        "cook",
        "cooked",
        "cooker",
        "cooking",
        "cool",
        "copper",
        "copy",
        "copyright",
        "cord",
        "cork",
        "corner",
        "correlation",
        "corrosion",
        "cost",
        "cotton",
        "cough",
        "country",
        "court",
        "cover",
        "cow",
        "crack",
        "credit",
        "creeper",
        "crime",
        "crop",
        "cross",
        "cruel",
        "crush",
        "cry",
        "crying",
        "cunning",
        "cup",
        "cupboard",
        "current",
        "curtain",
        "curve",
        "cushion",
        "cusp",
        "customs",
        "cut",
        "damage",
        "damping",
        "dance",
        "dancer",
        "dancing",
        "danger",
        "dark",
        "date",
        "daughter",
        "day",
        "daylight",
        "dead",
        "dear",
        "death",
        "debit",
        "debt",
        "december",
        "deci-",
        "decision",
        "deck",
        "decrease",
        "deep",
        "defect",
        "deficiency",
        "deflation",
        "degenerate",
        "degree",
        "delicate",
        "delivery",
        "demand",
        "denominator",
        "density",
        "department",
        "dependent",
        "deposit",
        "desert",
        "design",
        "designer",
        "desire",
        "destruction",
        "detail",
        "determining",
        "development",
        "dew",
        "diameter",
        "difference",
        "different",
        "difficulty",
        "digestion",
        "dike",
        "dilution",
        "dinner",
        "dip",
        "direct",
        "direction",
        "dirty",
        "disappearance",
        "discharge",
        "discount",
        "discovery",
        "discussion",
        "disease",
        "disgrace",
        "disgust",
        "dislike",
        "dissipation",
        "distance",
        "distribution",
        "disturbance",
        "ditch",
        "dive",
        "division",
        "divisor",
        "divorce",
        "do",
        "dog",
        "doll",
        "domesticating",
        "dominion",
        "door",
        "doubt",
        "down",
        "downfall",
        "drain",
        "drawer",
        "dreadful",
        "dream",
        "dress",
        "dressing",
        "drift",
        "drink",
        "driver",
        "driving",
        "drop",
        "dropped",
        "dropper",
        "dry",
        "duct",
        "dull",
        "dust",
        "duster",
        "duty",
        "dynamite",
        "each",
        "ear",
        "early",
        "earring",
        "earth",
        "earthwork",
        "east",
        "easy",
        "economy",
        "edge",
        "education",
        "effect",
        "efficiency",
        "effort",
        "egg",
        "eight",
        "either",
        "elastic",
        "electric",
        "electricity",
        "eleven",
        "elimination",
        "embassy",
        "empire",
        "employer",
        "empty",
        "encyclopedia",
        "end",
        "enemy",
        "engine",
        "engineer",
        "enough",
        "envelope",
        "environment",
        "envy",
        "equal",
        "equation",
        "erosion",
        "error",
        "eruption",
        "evaporation",
        "even",
        "evening",
        "event",
        "ever",
        "evergreen",
        "every",
        "everybody",
        "everyday",
        "everyone",
        "everything",
        "everywhere",
        "exact",
        "example",
        "exchange",
        "excitement",
        "exercise",
        "existence",
        "expansion",
        "experience",
        "experiment",
        "expert",
        "explanation",
        "explosion",
        "export",
        "expression",
        "extinction",
        "eye",
        "eyeball",
        "eyebrow",
        "eyelash",
        "face",
        "fact",
        "factor",
        "failure",
        "fair",
        "fall",
        "false",
        "family",
        "famous",
        "fan",
        "far",
        "farm",
        "farmer",
        "fastening",
        "fat",
        "father",
        "fatherland",
        "fault",
        "fear",
        "feather",
        "february",
        "feeble",
        "feeling",
        "female",
        "ferment",
        "fertile",
        "fertilizing",
        "fever",
        "fiber",
        "fiction",
        "field",
        "fifteen",
        "fifth",
        "fifty",
        "fight",
        "figure",
        "fin",
        "financial",
        "finger",
        "fingerprint",
        "fire",
        "fire-engine",
        "firearm",
        "fired",
        "firefly",
        "fireman",
        "fireplace",
        "firework",
        "firing",
        "first",
        "first-rate",
        "fish",
        "fisher/fisherman",
        "five",
        "fixed",
        "flag",
        "flame",
        "flash",
        "flask",
        "flat",
        "flesh",
        "flight",
        "flint",
        "flood",
        "floor",
        "flour",
        "flow",
        "flower",
        "fly",
        "focus",
        "fold",
        "folder",
        "foliation",
        "food",
        "foolish",
        "foot",
        "football",
        "footlights",
        "footman",
        "footnote",
        "footprint",
        "footstep",
        "for",
        "force",
        "forecast",
        "forehead",
        "foreign",
        "forgiveness",
        "fork",
        "form",
        "forty",
        "forward",
        "four",
        "fourteen",
        "fourth",
        "fowl",
        "fraction",
        "fracture",
        "frame",
        "free",
        "frequent",
        "fresh",
        "friction",
        "friday",
        "friend",
        "from",
        "front",
        "frost",
        "frozen",
        "fruit",
        "full",
        "fume",
        "funnel",
        "funny",
        "fur",
        "furnace",
        "furniture",
        "fusion",
        "future",
        "garden",
        "gardener",
        "gas",
        "gasworks",
        "gate",
        "general",
        "generation",
        "geography",
        "geology",
        "geometry",
        "germ",
        "germinating",
        "get",
        "gill",
        "girl",
        "give",
        "glacier",
        "gland",
        "glass",
        "glove",
        "glycerin",
        "go",
        "goat",
        "god",
        "gold",
        "goldfish",
        "good",
        "good-morning",
        "goodlooking",
        "goodnight",
        "government",
        "grain",
        "gram",
        "grand",
        "grass",
        "grateful",
        "grating",
        "gravel",
        "grease",
        "great",
        "green",
        "grey/gray",
        "grief",
        "grip",
        "grocery",
        "groove",
        "gross",
        "ground",
        "group",
        "growth",
        "guarantee",
        "guard",
        "guess",
        "guide",
        "gum",
        "gun",
        "gun-carriage",
        "gunboat",
        "gunmetal",
        "gunpowder",
        "habit",
        "hair",
        "half",
        "hammer",
        "hand",
        "handbook",
        "handkerchief",
        "handle",
        "handwriting",
        "hanger",
        "hanging",
        "happy",
        "harbor",
        "hard",
        "harmony",
        "hat",
        "hate",
        "have",
        "he",
        "head",
        "headdress",
        "headland",
        "headstone",
        "headway",
        "healthy",
        "hearing",
        "heart",
        "heat",
        "heated",
        "heater",
        "heating",
        "heavy",
        "hedge",
        "help",
        "here",
        "hereafter",
        "herewith",
        "high",
        "highlands",
        "highway",
        "hill",
        "himself",
        "hinge",
        "hire",
        "hiss",
        "history",
        "hold",
        "hole",
        "holiday",
        "hollow",
        "home",
        "honest",
        "honey",
        "hoof",
        "hook",
        "hope",
        "horn",
        "horse",
        "horseplay",
        "horsepower",
        "hospital",
        "host",
        "hotel",
        "hour",
        "hourglass",
        "house",
        "houseboat",
        "housekeeper",
        "how",
        "however",
        "human",
        "humor",
        "hundred",
        "hunt",
        "hurry",
        "hurt",
        "husband",
        "hyena",
        "hygiene",
        "hysteria",
        "i",
        "ice",
        "idea",
        "if",
        "igneous",
        "ill",
        "image",
        "imagination",
        "imperial",
        "import",
        "important",
        "impulse",
        "impurity",
        "in",
        "inasmuch",
        "inclusion",
        "income",
        "increase",
        "index",
        "individual",
        "indoors",
        "industry",
        "inferno",
        "infinity",
        "inflation",
        "influenza",
        "inheritance",
        "ink",
        "inland",
        "inlet",
        "inner",
        "innocent",
        "input",
        "insect",
        "inside",
        "instep",
        "institution",
        "instrument",
        "insulator",
        "insurance",
        "integer",
        "intelligent",
        "intercept",
        "interest",
        "international",
        "interpretation",
        "intersection",
        "into",
        "intrusion",
        "invention",
        "inverse",
        "investigation",
        "investment",
        "invitation",
        "iron",
        "island",
        "itself",
        "jam",
        "january",
        "jaw",
        "jazz",
        "jealous",
        "jelly",
        "jerk",
        "jewel",
        "jeweler",
        "join",
        "joiner",
        "joint",
        "journey",
        "judge",
        "jug",
        "juice",
        "july",
        "jump",
        "june",
        "jury",
        "justice",
        "keep",
        "keeper",
        "kennel",
        "kettle",
        "key",
        "kick",
        "kidney",
        "kilo-",
        "kind",
        "king",
        "kiss",
        "kitchen",
        "knee",
        "knife",
        "knock",
        "knot",
        "knowledge",
        "lace",
        "lag",
        "lake",
        "lame",
        "lamp",
        "land",
        "landmark",
        "landslip",
        "language",
        "large",
        "last",
        "late",
        "latitude",
        "laugh",
        "laughing",
        "lava",
        "law",
        "lawyer",
        "layer",
        "lazy",
        "lead",
        "leaf",
        "learner",
        "learning",
        "least",
        "leather",
        "lecture",
        "left",
        "leg",
        "legal",
        "length",
        "lens",
        "less",
        "lesson",
        "let",
        "letter",
        "level",
        "lever",
        "liability",
        "library",
        "license",
        "lid",
        "life",
        "lift",
        "light",
        "lighthouse",
        "like",
        "lime",
        "limestone",
        "limit",
        "line",
        "linen",
        "link",
        "lip",
        "liqueur",
        "liquid",
        "list",
        "liter",
        "little",
        "liver",
        "living",
        "load",
        "loan",
        "local",
        "lock",
        "locker",
        "locking",
        "locus",
        "long",
        "longitude",
        "look",
        "looking-glass",
        "loose",
        "loss",
        "loud",
        "love",
        "low",
        "luck",
        "lump",
        "lunch",
        "lung",
        "macaroni",
        "machine",
        "madam",
        "magic",
        "magnetic",
        "magnitude",
        "make",
        "malaria",
        "male",
        "man",
        "manager",
        "manhole",
        "mania",
        "manner",
        "many",
        "map",
        "marble",
        "march",
        "margin",
        "mark",
        "marked",
        "market",
        "marriage",
        "married",
        "mass",
        "mast",
        "match",
        "material",
        "mathematics",
        "mattress",
        "mature",
        "may",
        "meal",
        "mean",
        "meaning",
        "measure",
        "meat",
        "medical",
        "medicine",
        "medium",
        "meeting",
        "melt",
        "member",
        "memory",
        "meow",
        "mess",
        "message",
        "metabolism",
        "metal",
        "meter",
        "micro-",
        "microscope",
        "middle",
        "military",
        "milk",
        "mill",
        "milli-",
        "million",
        "mind",
        "mine",
        "miner",
        "mineral",
        "minute",
        "mist",
        "mixed",
        "mixture",
        "model",
        "modern",
        "modest",
        "momentum",
        "monday",
        "money",
        "monkey",
        "monopoly",
        "month",
        "mood",
        "moon",
        "moral",
        "more",
        "morning",
        "most",
        "mother",
        "motion",
        "mountain",
        "moustache",
        "mouth",
        "move",
        "much",
        "mud",
        "multiple",
        "multiplication",
        "murder",
        "muscle",
        "museum",
        "music",
        "myself",
        "nail",
        "name",
        "narrow",
        "nasty",
        "nation",
        "natural",
        "nature",
        "navy",
        "near",
        "nearer",
        "neat",
        "necessary",
        "neck",
        "need",
        "needle",
        "neglect",
        "neighbor",
        "nerve",
        "nest",
        "net",
        "network",
        "neutron",
        "new",
        "news",
        "newspaper",
        "next",
        "nice",
        "nickel",
        "nicotine",
        "night",
        "nine",
        "no",
        "nobody",
        "node",
        "noise",
        "normal",
        "north",
        "nose",
        "nostril",
        "not",
        "note",
        "noted",
        "nothing",
        "november",
        "now",
        "nowhere",
        "nucleus",
        "number",
        "numerator",
        "nurse",
        "nut",
        "obedient",
        "observation",
        "october",
        "of",
        "off",
        "offer",
        "office",
        "officer",
        "offspring",
        "oil",
        "old",
        "olive",
        "omelet",
        "on",
        "once",
        "oncoming",
        "one",
        "oneself",
        "onlooker",
        "only",
        "onto",
        "open",
        "opera",
        "operation",
        "opinion",
        "opium",
        "opposite",
        "or",
        "orange",
        "orchestra",
        "order",
        "ore",
        "organ",
        "organism",
        "organization",
        "origin",
        "ornament",
        "other",
        "out",
        "outburst",
        "outcome",
        "outcrop",
        "outcry",
        "outdoor",
        "outer",
        "outgoing",
        "outhouse",
        "outlaw",
        "outlet",
        "outlier",
        "outline",
        "outlook",
        "output",
        "outside",
        "outskirts",
        "outstretched",
        "oval",
        "oven",
        "over",
        "overacting",
        "overall",
        "overbalancing",
        "overbearing",
        "overcoat",
        "overcome",
        "overdo",
        "overdressed",
        "overfull",
        "overhanging",
        "overhead",
        "overland",
        "overlap",
        "overleaf",
        "overloud",
        "overseas",
        "overseer",
        "overshoe",
        "overstatement",
        "overtake",
        "overtaxed",
        "overtime",
        "overturned",
        "overuse",
        "overvalued",
        "overweight",
        "overworking",
        "own",
        "owner",
        "oxidation",
        "packing",
        "pad",
        "page",
        "pain",
        "paint",
        "painter",
        "painting",
        "pair",
        "pajamas",
        "pan",
        "paper",
        "paradise",
        "paraffin",
        "paragraph",
        "parallel",
        "parcel",
        "parent",
        "park",
        "part",
        "particle",
        "parting",
        "partner",
        "party",
        "passage",
        "passport",
        "past",
        "paste",
        "patent",
        "path",
        "patience",
        "payment",
        "peace",
        "pedal",
        "pen",
        "pencil",
        "pendulum",
        "penguin",
        "pension",
        "people",
        "perfect",
        "person",
        "petal",
        "petroleum",
        "phonograph",
        "physical",
        "physics",
        "physiology",
        "piano",
        "picture",
        "pig",
        "pin",
        "pincushion",
        "pipe",
        "piston",
        "place",
        "plain",
        "plan",
        "plane",
        "plant",
        "plaster",
        "plate",
        "platinum",
        "play",
        "played",
        "playing",
        "plaything",
        "please",
        "pleased",
        "pleasure",
        "plough/plow",
        "plug",
        "pocket",
        "poetry",
        "point",
        "pointer",
        "pointing",
        "poison",
        "police",
        "policeman",
        "polish",
        "political",
        "pollen",
        "pool",
        "poor",
        "population",
        "porcelain",
        "porter",
        "position",
        "possible",
        "post",
        "postman",
        "postmark",
        "postmaster",
        "postoffice",
        "pot",
        "potash",
        "potato",
        "potter",
        "powder",
        "power",
        "practice",
        "praise",
        "prayer",
        "present",
        "president",
        "pressure",
        "price",
        "prick",
        "priest",
        "prime",
        "prince",
        "princess",
        "print",
        "printer",
        "prison",
        "prisoner",
        "private",
        "probability",
        "probable",
        "process",
        "produce",
        "producer",
        "product",
        "profit",
        "program",
        "progress",
        "projectile",
        "projection",
        "promise",
        "proof",
        "propaganda",
        "property",
        "prose",
        "protest",
        "proud",
        "psychology",
        "public",
        "pull",
        "pulley",
        "pump",
        "punishment",
        "pupil",
        "purchase",
        "pure",
        "purpose",
        "purr",
        "push",
        "put",
        "pyramid",
        "quack",
        "quality",
        "quantity",
        "quarter",
        "queen",
        "question",
        "quick",
        "quiet",
        "quinine",
        "quite",
        "quotient",
        "race",
        "radiation",
        "radio",
        "radium",
        "rail",
        "rain",
        "raining",
        "range",
        "rat",
        "rate",
        "ratio",
        "ray",
        "reaction",
        "reader",
        "reading",
        "ready",
        "reagent",
        "real",
        "reason",
        "receipt",
        "receiver",
        "reciprocal",
        "record",
        "rectangle",
        "recurring",
        "red",
        "reference",
        "referendum",
        "reflux",
        "regret",
        "regular",
        "reinforcement",
        "relation",
        "relative",
        "religion",
        "remark",
        "remedy",
        "rent",
        "repair",
        "representative",
        "reproduction",
        "repulsion",
        "request",
        "residue",
        "resistance",
        "resolution",
        "respect",
        "responsible",
        "rest",
        "restaurant",
        "result",
        "retail",
        "revenge",
        "reversible",
        "reward",
        "rheumatism",
        "rhythm",
        "rice",
        "rich",
        "right",
        "rigidity",
        "ring",
        "rise",
        "rival",
        "river",
        "road",
        "rock",
        "rod",
        "roll",
        "roller",
        "roof",
        "room",
        "root",
        "rot",
        "rotation",
        "rough",
        "round",
        "royal",
        "rub",
        "rubber",
        "rude",
        "rule",
        "ruler",
        "rum",
        "run",
        "runaway",
        "rust",
        "sac",
        "sad",
        "safe",
        "sail",
        "sailor",
        "salad",
        "sale",
        "salt",
        "same",
        "sample",
        "sand",
        "sardine",
        "satisfaction",
        "saturated",
        "saturday",
        "saucer",
        "saving",
        "say",
        "scale",
        "scarp",
        "schist",
        "school",
        "science",
        "scissors",
        "scratch",
        "screen",
        "screw",
        "sea",
        "seal",
        "seaman",
        "search",
        "seat",
        "second",
        "secondhand",
        "secret",
        "secretary",
        "secretion",
        "section",
        "security",
        "sedimentary",
        "see",
        "seed",
        "seem",
        "selection",
        "self",
        "selfish",
        "send",
        "sense",
        "sensitivity",
        "sentence",
        "sepal",
        "separate",
        "september",
        "serious",
        "serum",
        "servant",
        "service",
        "set",
        "seven",
        "sex",
        "shade",
        "shadow",
        "shake",
        "shale",
        "shame",
        "share",
        "sharp",
        "shave",
        "shear",
        "sheep",
        "sheet",
        "shelf",
        "shell",
        "ship",
        "shirt",
        "shock",
        "shocked",
        "shocking",
        "shoe",
        "shore",
        "short",
        "shorthand",
        "shoulder",
        "show",
        "shut",
        "side",
        "sideboard",
        "sidewalk",
        "sight",
        "sign",
        "silk",
        "sill",
        "silver",
        "similarity",
        "simple",
        "since",
        "sir",
        "sister",
        "six",
        "sixteen",
        "size",
        "skin",
        "skirt",
        "skull",
        "sky",
        "slate",
        "sleep",
        "sleeve",
        "slide",
        "slip",
        "slope",
        "slow",
        "small",
        "smash",
        "smell",
        "smile",
        "smoke",
        "smooth",
        "snake",
        "sneeze",
        "snow",
        "snowing",
        "so",
        "soap",
        "social",
        "society",
        "sock",
        "soft",
        "soil",
        "soldier",
        "solid",
        "solution",
        "solvent",
        "some",
        "somebody",
        "someday",
        "somehow",
        "someone",
        "something",
        "sometime",
        "somewhat",
        "somewhere",
        "son",
        "song",
        "sorry",
        "sort",
        "sound",
        "soup",
        "south",
        "space",
        "spade",
        "spark",
        "special",
        "specialization",
        "specimen",
        "speculation",
        "spirit",
        "spit",
        "splash",
        "sponge",
        "spoon",
        "sport",
        "spot",
        "spring",
        "square",
        "stable",
        "stage",
        "stain",
        "stair",
        "stalk",
        "stamen",
        "stamp",
        "star",
        "start",
        "statement",
        "station",
        "statistics",
        "steady",
        "steam",
        "steamer",
        "steel",
        "stem",
        "step",
        "stick",
        "sticky",
        "stiff",
        "still",
        "stimulus",
        "stitch",
        "stocking",
        "stomach",
        "stone",
        "stop",
        "stopper",
        "stopping",
        "stopping up",
        "store",
        "storm",
        "story",
        "straight",
        "strain",
        "strange",
        "straw",
        "stream",
        "street",
        "strength",
        "stress",
        "stretch",
        "stretcher",
        "strike",
        "string",
        "strong",
        "structure",
        "study",
        "subject",
        "substance",
        "substitution",
        "subtraction",
        "success",
        "successive",
        "such",
        "suchlike",
        "sucker",
        "sudden",
        "sugar",
        "suggestion",
        "sum",
        "summer",
        "sun",
        "sunburn",
        "sunday",
        "sunlight",
        "sunshade",
        "supply",
        "support",
        "surface",
        "surgeon",
        "surprise",
        "suspension",
        "suspicious",
        "sweet",
        "sweetheart",
        "swelling",
        "swim",
        "swing",
        "switch",
        "sympathetic",
        "system",
        "table",
        "tail",
        "tailor",
        "take",
        "talk",
        "talking",
        "tall",
        "tame",
        "tap",
        "tapioca",
        "taste",
        "tax",
        "taxi",
        "tea",
        "teacher",
        "teaching",
        "tear",
        "telegram",
        "telephone",
        "ten",
        "tendency",
        "tent",
        "term",
        "terrace",
        "test",
        "texture",
        "than",
        "that",
        "the",
        "theater",
        "then",
        "theory",
        "there",
        "thermometer",
        "thick",
        "thickness",
        "thief",
        "thimble",
        "thin",
        "thing",
        "third",
        "thirteen",
        "thirty",
        "this",
        "thorax",
        "though",
        "thought",
        "thousand",
        "thread",
        "threat",
        "three",
        "throat",
        "through",
        "thrust",
        "thumb",
        "thunder",
        "thursday",
        "ticket",
        "tide",
        "tie",
        "tight",
        "till",
        "time",
        "tin",
        "tired",
        "tissue",
        "to",
        "toast",
        "tobacco",
        "today",
        "toe",
        "together",
        "tomorrow",
        "tongs",
        "tongue",
        "tonight",
        "too",
        "tooth",
        "top",
        "torpedo",
        "total",
        "touch",
        "touching",
        "towel",
        "tower",
        "town",
        "trade",
        "trader",
        "tradesman",
        "traffic",
        "tragedy",
        "train",
        "trainer",
        "training",
        "transmission",
        "transparent",
        "transport",
        "trap",
        "travel",
        "tray",
        "treatment",
        "tree",
        "triangle",
        "trick",
        "trouble",
        "troubled",
        "troubling",
        "trousers",
        "truck",
        "true",
        "tube",
        "tuesday",
        "tune",
        "tunnel",
        "turbine",
        "turn",
        "turning",
        "twelve",
        "twenty",
        "twenty-one",
        "twice",
        "twin",
        "twist",
        "two",
        "typist",
        "ugly",
        "umbrella",
        "unconformity",
        "under",
        "underclothing",
        "undercooked",
        "undergo",
        "undergrowth",
        "undermined",
        "undersigned",
        "undersized",
        "understanding",
        "understatement",
        "undertake",
        "undervalued",
        "undo",
        "unit",
        "universe",
        "university",
        "unknown",
        "up",
        "upkeep",
        "uplift",
        "upon",
        "upright",
        "uptake",
        "use",
        "used",
        "valency",
        "valley",
        "value",
        "valve",
        "vanilla",
        "vapor",
        "variable",
        "vascular",
        "vegetable",
        "velocity",
        "verse",
        "very",
        "vessel",
        "vestigial",
        "victim",
        "victory",
        "view",
        "viewpoint",
        "violent",
        "violin",
        "visa",
        "vitamin",
        "vodka",
        "voice",
        "volt",
        "volume",
        "vortex",
        "vote",
        "waiter",
        "waiting",
        "walk",
        "wall",
        "war",
        "warm",
        "wash",
        "waste",
        "wasted",
        "watch",
        "water",
        "waterfall",
        "wave",
        "wax",
        "way",
        "weak",
        "weather",
        "wedge",
        "wednesday",
        "week",
        "weekend",
        "weight",
        "welcome",
        "well",
        "well-being",
        "well-off",
        "west",
        "wet",
        "what",
        "whatever",
        "wheel",
        "when",
        "whenever",
        "where",
        "whereas",
        "whereby",
        "wherever",
        "whether",
        "which",
        "whichever",
        "while",
        "whip",
        "whisky",
        "whistle",
        "white",
        "whitewash",
        "who",
        "whoever",
        "wholesale",
        "why",
        "wide",
        "widow",
        "wife",
        "wild",
        "will",
        "wind",
        "window",
        "windpipe",
        "wine",
        "wing",
        "winter",
        "wire",
        "wise",
        "with",
        "within",
        "without",
        "woman",
        "wood",
        "woodwork",
        "wool",
        "word",
        "work",
        "worker",
        "workhouse",
        "working",
        "world",
        "worm",
        "wound",
        "wreck",
        "wrist",
        "writer",
        "writing",
        "wrong",
        "x-ray",
        "yawn",
        "year",
        "yearbook",
        "yellow",
        "yes",
        "yesterday",
        "you",
        "young",
        "yourself",
        "zebra",
        "zinc",
        "zookeeper",
        "zoology",
    )
)
