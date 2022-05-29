const routes = {
    1: ["Clermistion", "Seafield"],
    2: ["The Jewel", "Gyle Centre"],
    3: ["Clovenstone", "Mayfield", "Dalkeith"],
    4: ["Hillend", "The Jewel"],
    5: ["Hunter's Tryst", "The Jewel"],
    7: ["Newhaven", "Royal Infirmary"],
    8: ["Muirhouse", "Royal Infirmary"],
    10: ["Western Harbour", "Torphin", "Bonaly"],
    11: ["Ocean Terminal", "Hyvots Bank"],
    12: ["Gyle Centre"],
    14: ["Muirhouse", "Greendykes"],
    15: ["Easter Bush"],
    16: ["Silverknowes", "Colinton"],
    19: ["Granton", "King's Road"],
    22: ["Gyle Centre", "Ocean Terminal"],
    23: ["Trinity", "Greenbank"],
    24: ["Muirhouse", "Royal Infirmary"],
    25: ["Heriot Watt University", "Restalrig"],
    26: ["Clerwood", "Seton Sands", "Tranent"],
    27: ["Sliverknowes", "Hunter's Tryst"],
    29: ["Silverknowes", "Gorebridge"],
    3: ["Clovenstone", "Musselburgh"],
    31: ["East Craigs", "Bonnyrig", "Polton Mill"],
    33: ["Wester Hailes", "Millerhill"],
    34: ["Heriot Watt University", "Ocean Terminal"],
    36: ["Gyle Centre", "Ocean Terminal"],
    37: ["Silverknowes", "Penicuik", "Easter Bush"],
    41: ["Cramond", "King's Buildings"],
    42: ["Craigleith", "King's Road"],
    44: ["Balerno", "Wallyford"],
    45: ["Heroit Watt University", "Queen Margaret University"],
    47: ["Granton", "Penicuik"],
    49: ["Fort Kinnaird", "Rosewell"],
    X18: ["Whitburn"],
    X27: ["Whitburn"],
    X28: ["Bathgate"],
    43: ["Queensferry"],
    104: ["Haddington"],
    X7: ["Dunbar"],
    113: ["Pentcaitland", "West Granton"],
    124: ["North Berwick"],
    Tram: ["Edinburgh Airport"]
}
const routeKeys = Object.keys(routes);

function getRandomItem(array) {
    return array[array.length * Math.random() | 0];
}

function showRandomRoute() {
    const route = getRandomItem(routeKeys);
    const destination = getRandomItem(routes[route]);

    console.log(route, destination);
}
