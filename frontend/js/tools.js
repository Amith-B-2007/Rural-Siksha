/**
 * Study Tools - Calculator, Formula Sheet, Periodic Table, Unit Converter
 */

let calcDisplay = '0';
let calcHistory = [];
let calcMemory = 0;

// MATH FORMULAS by Grade
const FORMULAS = {
    'Mathematics': [
        { topic: 'Algebra', formulas: [
            '(a + b)² = a² + 2ab + b²',
            '(a - b)² = a² - 2ab + b²',
            '(a + b)(a - b) = a² - b²',
            '(a + b)³ = a³ + 3a²b + 3ab² + b³',
            '(a - b)³ = a³ - 3a²b + 3ab² - b³',
            'a³ + b³ = (a + b)(a² - ab + b²)',
            'a³ - b³ = (a - b)(a² + ab + b²)',
        ]},
        { topic: 'Geometry - Area', formulas: [
            'Square Area = side²',
            'Rectangle Area = length × breadth',
            'Triangle Area = ½ × base × height',
            'Circle Area = πr²',
            'Parallelogram Area = base × height',
            'Trapezium Area = ½ × (a + b) × h',
            'Rhombus Area = ½ × d₁ × d₂',
        ]},
        { topic: 'Geometry - Perimeter', formulas: [
            'Square Perimeter = 4 × side',
            'Rectangle Perimeter = 2(l + b)',
            'Triangle Perimeter = sum of all sides',
            'Circle Circumference = 2πr',
        ]},
        { topic: 'Geometry - Volume', formulas: [
            'Cube Volume = side³',
            'Cuboid Volume = l × b × h',
            'Cylinder Volume = πr²h',
            'Cone Volume = (1/3)πr²h',
            'Sphere Volume = (4/3)πr³',
            'Hemisphere Volume = (2/3)πr³',
        ]},
        { topic: 'Trigonometry', formulas: [
            'sin θ = Opposite / Hypotenuse',
            'cos θ = Adjacent / Hypotenuse',
            'tan θ = Opposite / Adjacent',
            'sin²θ + cos²θ = 1',
            '1 + tan²θ = sec²θ',
            '1 + cot²θ = cosec²θ',
            'sin(90°-θ) = cos θ',
            'cos(90°-θ) = sin θ',
        ]},
        { topic: 'Trigonometric Values', formulas: [
            'sin 0° = 0, sin 30° = 1/2, sin 45° = 1/√2',
            'sin 60° = √3/2, sin 90° = 1',
            'cos 0° = 1, cos 30° = √3/2, cos 45° = 1/√2',
            'cos 60° = 1/2, cos 90° = 0',
            'tan 0° = 0, tan 30° = 1/√3, tan 45° = 1',
            'tan 60° = √3, tan 90° = undefined',
        ]},
        { topic: 'Quadratic Equation', formulas: [
            'Standard form: ax² + bx + c = 0',
            'x = [-b ± √(b² - 4ac)] / 2a',
            'Discriminant D = b² - 4ac',
            'Sum of roots = -b/a',
            'Product of roots = c/a',
        ]},
        { topic: 'Coordinate Geometry', formulas: [
            'Distance = √[(x₂-x₁)² + (y₂-y₁)²]',
            'Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2)',
            'Slope m = (y₂-y₁)/(x₂-x₁)',
            'Line equation: y = mx + c',
            'Section formula: ((mx₂+nx₁)/(m+n), (my₂+ny₁)/(m+n))',
        ]},
        { topic: 'Statistics', formulas: [
            'Mean = Sum of values / Number of values',
            'Median: middle value (or avg of 2 middles)',
            'Mode: most frequent value',
            'Range = Highest - Lowest',
            'Mode = 3 × Median - 2 × Mean',
        ]},
        { topic: 'Compound Interest', formulas: [
            'Simple Interest = PRT/100',
            'Amount A = P(1 + R/100)^n',
            'CI = A - P',
            'Half-yearly: A = P(1 + R/200)^2n',
        ]},
    ],
    'Science': [
        { topic: 'Physics - Motion', formulas: [
            'Speed = Distance / Time',
            'Velocity = Displacement / Time',
            'Acceleration = (v - u) / t',
            'v = u + at',
            's = ut + ½at²',
            'v² = u² + 2as',
            'Newton\'s 2nd Law: F = ma',
        ]},
        { topic: 'Physics - Force & Energy', formulas: [
            'Force = mass × acceleration',
            'Weight = mass × g (g = 9.8 m/s²)',
            'Pressure = Force / Area',
            'Work = Force × Distance',
            'Power = Work / Time = Energy / Time',
            'Kinetic Energy = ½mv²',
            'Potential Energy = mgh',
        ]},
        { topic: 'Physics - Light', formulas: [
            'Mirror formula: 1/v + 1/u = 1/f',
            'Magnification: m = h\'/h = -v/u',
            'Lens formula: 1/v - 1/u = 1/f',
            'Power of lens: P = 1/f (in meters)',
            'Refractive index: n = sin i / sin r',
        ]},
        { topic: 'Physics - Electricity', formulas: [
            'Ohm\'s Law: V = IR',
            'Power P = VI = I²R = V²/R',
            'Energy E = P × t',
            'In Series: R = R₁ + R₂ + R₃',
            'In Parallel: 1/R = 1/R₁ + 1/R₂',
        ]},
        { topic: 'Chemistry', formulas: [
            'Water: H₂O',
            'Carbon dioxide: CO₂',
            'Methane: CH₄',
            'Ammonia: NH₃',
            'Common salt: NaCl',
            'Photosynthesis: 6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂',
            'Respiration: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O',
        ]},
        { topic: 'Biology - Body', formulas: [
            'Normal body temperature: 37°C / 98.6°F',
            'Normal heart rate: 60-100 beats/min',
            'Number of bones: 206 (adult)',
            'Number of teeth: 32 (adult)',
            'Blood pressure: 120/80 mmHg (normal)',
            'Breathing rate: 12-20 per minute',
        ]},
    ]
};

// COMPLETE PERIODIC TABLE - All 118 Elements
const PERIODIC_TABLE = [
    {num: 1, sym: 'H', name: 'Hydrogen', mass: 1.008, group: 1, period: 1, type: 'nonmetal'},
    {num: 2, sym: 'He', name: 'Helium', mass: 4.003, group: 18, period: 1, type: 'noble'},
    {num: 3, sym: 'Li', name: 'Lithium', mass: 6.94, group: 1, period: 2, type: 'alkali'},
    {num: 4, sym: 'Be', name: 'Beryllium', mass: 9.012, group: 2, period: 2, type: 'alkaline'},
    {num: 5, sym: 'B', name: 'Boron', mass: 10.81, group: 13, period: 2, type: 'metalloid'},
    {num: 6, sym: 'C', name: 'Carbon', mass: 12.01, group: 14, period: 2, type: 'nonmetal'},
    {num: 7, sym: 'N', name: 'Nitrogen', mass: 14.01, group: 15, period: 2, type: 'nonmetal'},
    {num: 8, sym: 'O', name: 'Oxygen', mass: 16.00, group: 16, period: 2, type: 'nonmetal'},
    {num: 9, sym: 'F', name: 'Fluorine', mass: 19.00, group: 17, period: 2, type: 'halogen'},
    {num: 10, sym: 'Ne', name: 'Neon', mass: 20.18, group: 18, period: 2, type: 'noble'},
    {num: 11, sym: 'Na', name: 'Sodium', mass: 22.99, group: 1, period: 3, type: 'alkali'},
    {num: 12, sym: 'Mg', name: 'Magnesium', mass: 24.31, group: 2, period: 3, type: 'alkaline'},
    {num: 13, sym: 'Al', name: 'Aluminum', mass: 26.98, group: 13, period: 3, type: 'metal'},
    {num: 14, sym: 'Si', name: 'Silicon', mass: 28.09, group: 14, period: 3, type: 'metalloid'},
    {num: 15, sym: 'P', name: 'Phosphorus', mass: 30.97, group: 15, period: 3, type: 'nonmetal'},
    {num: 16, sym: 'S', name: 'Sulfur', mass: 32.07, group: 16, period: 3, type: 'nonmetal'},
    {num: 17, sym: 'Cl', name: 'Chlorine', mass: 35.45, group: 17, period: 3, type: 'halogen'},
    {num: 18, sym: 'Ar', name: 'Argon', mass: 39.95, group: 18, period: 3, type: 'noble'},
    {num: 19, sym: 'K', name: 'Potassium', mass: 39.10, group: 1, period: 4, type: 'alkali'},
    {num: 20, sym: 'Ca', name: 'Calcium', mass: 40.08, group: 2, period: 4, type: 'alkaline'},
    {num: 21, sym: 'Sc', name: 'Scandium', mass: 44.96, group: 3, period: 4, type: 'transition'},
    {num: 22, sym: 'Ti', name: 'Titanium', mass: 47.87, group: 4, period: 4, type: 'transition'},
    {num: 23, sym: 'V', name: 'Vanadium', mass: 50.94, group: 5, period: 4, type: 'transition'},
    {num: 24, sym: 'Cr', name: 'Chromium', mass: 52.00, group: 6, period: 4, type: 'transition'},
    {num: 25, sym: 'Mn', name: 'Manganese', mass: 54.94, group: 7, period: 4, type: 'transition'},
    {num: 26, sym: 'Fe', name: 'Iron', mass: 55.85, group: 8, period: 4, type: 'transition'},
    {num: 27, sym: 'Co', name: 'Cobalt', mass: 58.93, group: 9, period: 4, type: 'transition'},
    {num: 28, sym: 'Ni', name: 'Nickel', mass: 58.69, group: 10, period: 4, type: 'transition'},
    {num: 29, sym: 'Cu', name: 'Copper', mass: 63.55, group: 11, period: 4, type: 'transition'},
    {num: 30, sym: 'Zn', name: 'Zinc', mass: 65.38, group: 12, period: 4, type: 'transition'},
    {num: 31, sym: 'Ga', name: 'Gallium', mass: 69.72, group: 13, period: 4, type: 'metal'},
    {num: 32, sym: 'Ge', name: 'Germanium', mass: 72.63, group: 14, period: 4, type: 'metalloid'},
    {num: 33, sym: 'As', name: 'Arsenic', mass: 74.92, group: 15, period: 4, type: 'metalloid'},
    {num: 34, sym: 'Se', name: 'Selenium', mass: 78.97, group: 16, period: 4, type: 'nonmetal'},
    {num: 35, sym: 'Br', name: 'Bromine', mass: 79.90, group: 17, period: 4, type: 'halogen'},
    {num: 36, sym: 'Kr', name: 'Krypton', mass: 83.80, group: 18, period: 4, type: 'noble'},
    {num: 37, sym: 'Rb', name: 'Rubidium', mass: 85.47, group: 1, period: 5, type: 'alkali'},
    {num: 38, sym: 'Sr', name: 'Strontium', mass: 87.62, group: 2, period: 5, type: 'alkaline'},
    {num: 39, sym: 'Y', name: 'Yttrium', mass: 88.91, group: 3, period: 5, type: 'transition'},
    {num: 40, sym: 'Zr', name: 'Zirconium', mass: 91.22, group: 4, period: 5, type: 'transition'},
    {num: 41, sym: 'Nb', name: 'Niobium', mass: 92.91, group: 5, period: 5, type: 'transition'},
    {num: 42, sym: 'Mo', name: 'Molybdenum', mass: 95.95, group: 6, period: 5, type: 'transition'},
    {num: 43, sym: 'Tc', name: 'Technetium', mass: 98, group: 7, period: 5, type: 'transition'},
    {num: 44, sym: 'Ru', name: 'Ruthenium', mass: 101.07, group: 8, period: 5, type: 'transition'},
    {num: 45, sym: 'Rh', name: 'Rhodium', mass: 102.91, group: 9, period: 5, type: 'transition'},
    {num: 46, sym: 'Pd', name: 'Palladium', mass: 106.42, group: 10, period: 5, type: 'transition'},
    {num: 47, sym: 'Ag', name: 'Silver', mass: 107.87, group: 11, period: 5, type: 'transition'},
    {num: 48, sym: 'Cd', name: 'Cadmium', mass: 112.41, group: 12, period: 5, type: 'transition'},
    {num: 49, sym: 'In', name: 'Indium', mass: 114.82, group: 13, period: 5, type: 'metal'},
    {num: 50, sym: 'Sn', name: 'Tin', mass: 118.71, group: 14, period: 5, type: 'metal'},
    {num: 51, sym: 'Sb', name: 'Antimony', mass: 121.76, group: 15, period: 5, type: 'metalloid'},
    {num: 52, sym: 'Te', name: 'Tellurium', mass: 127.60, group: 16, period: 5, type: 'metalloid'},
    {num: 53, sym: 'I', name: 'Iodine', mass: 126.90, group: 17, period: 5, type: 'halogen'},
    {num: 54, sym: 'Xe', name: 'Xenon', mass: 131.29, group: 18, period: 5, type: 'noble'},
    {num: 55, sym: 'Cs', name: 'Cesium', mass: 132.91, group: 1, period: 6, type: 'alkali'},
    {num: 56, sym: 'Ba', name: 'Barium', mass: 137.33, group: 2, period: 6, type: 'alkaline'},
    {num: 57, sym: 'La', name: 'Lanthanum', mass: 138.91, group: 3, period: 6, type: 'lanthanide'},
    {num: 58, sym: 'Ce', name: 'Cerium', mass: 140.12, group: 3, period: 6, type: 'lanthanide'},
    {num: 59, sym: 'Pr', name: 'Praseodymium', mass: 140.91, group: 3, period: 6, type: 'lanthanide'},
    {num: 60, sym: 'Nd', name: 'Neodymium', mass: 144.24, group: 3, period: 6, type: 'lanthanide'},
    {num: 61, sym: 'Pm', name: 'Promethium', mass: 145, group: 3, period: 6, type: 'lanthanide'},
    {num: 62, sym: 'Sm', name: 'Samarium', mass: 150.36, group: 3, period: 6, type: 'lanthanide'},
    {num: 63, sym: 'Eu', name: 'Europium', mass: 151.96, group: 3, period: 6, type: 'lanthanide'},
    {num: 64, sym: 'Gd', name: 'Gadolinium', mass: 157.25, group: 3, period: 6, type: 'lanthanide'},
    {num: 65, sym: 'Tb', name: 'Terbium', mass: 158.93, group: 3, period: 6, type: 'lanthanide'},
    {num: 66, sym: 'Dy', name: 'Dysprosium', mass: 162.50, group: 3, period: 6, type: 'lanthanide'},
    {num: 67, sym: 'Ho', name: 'Holmium', mass: 164.93, group: 3, period: 6, type: 'lanthanide'},
    {num: 68, sym: 'Er', name: 'Erbium', mass: 167.26, group: 3, period: 6, type: 'lanthanide'},
    {num: 69, sym: 'Tm', name: 'Thulium', mass: 168.93, group: 3, period: 6, type: 'lanthanide'},
    {num: 70, sym: 'Yb', name: 'Ytterbium', mass: 173.04, group: 3, period: 6, type: 'lanthanide'},
    {num: 71, sym: 'Lu', name: 'Lutetium', mass: 174.97, group: 3, period: 6, type: 'lanthanide'},
    {num: 72, sym: 'Hf', name: 'Hafnium', mass: 178.49, group: 4, period: 6, type: 'transition'},
    {num: 73, sym: 'Ta', name: 'Tantalum', mass: 180.95, group: 5, period: 6, type: 'transition'},
    {num: 74, sym: 'W', name: 'Tungsten', mass: 183.84, group: 6, period: 6, type: 'transition'},
    {num: 75, sym: 'Re', name: 'Rhenium', mass: 186.21, group: 7, period: 6, type: 'transition'},
    {num: 76, sym: 'Os', name: 'Osmium', mass: 190.23, group: 8, period: 6, type: 'transition'},
    {num: 77, sym: 'Ir', name: 'Iridium', mass: 192.22, group: 9, period: 6, type: 'transition'},
    {num: 78, sym: 'Pt', name: 'Platinum', mass: 195.08, group: 10, period: 6, type: 'transition'},
    {num: 79, sym: 'Au', name: 'Gold', mass: 196.97, group: 11, period: 6, type: 'transition'},
    {num: 80, sym: 'Hg', name: 'Mercury', mass: 200.59, group: 12, period: 6, type: 'transition'},
    {num: 81, sym: 'Tl', name: 'Thallium', mass: 204.38, group: 13, period: 6, type: 'metal'},
    {num: 82, sym: 'Pb', name: 'Lead', mass: 207.2, group: 14, period: 6, type: 'metal'},
    {num: 83, sym: 'Bi', name: 'Bismuth', mass: 208.98, group: 15, period: 6, type: 'metal'},
    {num: 84, sym: 'Po', name: 'Polonium', mass: 209, group: 16, period: 6, type: 'metalloid'},
    {num: 85, sym: 'At', name: 'Astatine', mass: 210, group: 17, period: 6, type: 'halogen'},
    {num: 86, sym: 'Rn', name: 'Radon', mass: 222, group: 18, period: 6, type: 'noble'},
    {num: 87, sym: 'Fr', name: 'Francium', mass: 223, group: 1, period: 7, type: 'alkali'},
    {num: 88, sym: 'Ra', name: 'Radium', mass: 226, group: 2, period: 7, type: 'alkaline'},
    {num: 89, sym: 'Ac', name: 'Actinium', mass: 227, group: 3, period: 7, type: 'actinide'},
    {num: 90, sym: 'Th', name: 'Thorium', mass: 232.04, group: 3, period: 7, type: 'actinide'},
    {num: 91, sym: 'Pa', name: 'Protactinium', mass: 231.04, group: 3, period: 7, type: 'actinide'},
    {num: 92, sym: 'U', name: 'Uranium', mass: 238.03, group: 3, period: 7, type: 'actinide'},
    {num: 93, sym: 'Np', name: 'Neptunium', mass: 237, group: 3, period: 7, type: 'actinide'},
    {num: 94, sym: 'Pu', name: 'Plutonium', mass: 244, group: 3, period: 7, type: 'actinide'},
    {num: 95, sym: 'Am', name: 'Americium', mass: 243, group: 3, period: 7, type: 'actinide'},
    {num: 96, sym: 'Cm', name: 'Curium', mass: 247, group: 3, period: 7, type: 'actinide'},
    {num: 97, sym: 'Bk', name: 'Berkelium', mass: 247, group: 3, period: 7, type: 'actinide'},
    {num: 98, sym: 'Cf', name: 'Californium', mass: 251, group: 3, period: 7, type: 'actinide'},
    {num: 99, sym: 'Es', name: 'Einsteinium', mass: 252, group: 3, period: 7, type: 'actinide'},
    {num: 100, sym: 'Fm', name: 'Fermium', mass: 257, group: 3, period: 7, type: 'actinide'},
    {num: 101, sym: 'Md', name: 'Mendelevium', mass: 258, group: 3, period: 7, type: 'actinide'},
    {num: 102, sym: 'No', name: 'Nobelium', mass: 259, group: 3, period: 7, type: 'actinide'},
    {num: 103, sym: 'Lr', name: 'Lawrencium', mass: 266, group: 3, period: 7, type: 'actinide'},
    {num: 104, sym: 'Rf', name: 'Rutherfordium', mass: 267, group: 4, period: 7, type: 'transition'},
    {num: 105, sym: 'Db', name: 'Dubnium', mass: 268, group: 5, period: 7, type: 'transition'},
    {num: 106, sym: 'Sg', name: 'Seaborgium', mass: 269, group: 6, period: 7, type: 'transition'},
    {num: 107, sym: 'Bh', name: 'Bohrium', mass: 270, group: 7, period: 7, type: 'transition'},
    {num: 108, sym: 'Hs', name: 'Hassium', mass: 277, group: 8, period: 7, type: 'transition'},
    {num: 109, sym: 'Mt', name: 'Meitnerium', mass: 278, group: 9, period: 7, type: 'transition'},
    {num: 110, sym: 'Ds', name: 'Darmstadtium', mass: 281, group: 10, period: 7, type: 'transition'},
    {num: 111, sym: 'Rg', name: 'Roentgenium', mass: 282, group: 11, period: 7, type: 'transition'},
    {num: 112, sym: 'Cn', name: 'Copernicium', mass: 285, group: 12, period: 7, type: 'transition'},
    {num: 113, sym: 'Nh', name: 'Nihonium', mass: 286, group: 13, period: 7, type: 'metal'},
    {num: 114, sym: 'Fl', name: 'Flerovium', mass: 289, group: 14, period: 7, type: 'metal'},
    {num: 115, sym: 'Mc', name: 'Moscovium', mass: 290, group: 15, period: 7, type: 'metal'},
    {num: 116, sym: 'Lv', name: 'Livermorium', mass: 293, group: 16, period: 7, type: 'metal'},
    {num: 117, sym: 'Ts', name: 'Tennessine', mass: 294, group: 17, period: 7, type: 'halogen'},
    {num: 118, sym: 'Og', name: 'Oganesson', mass: 294, group: 18, period: 7, type: 'noble'}
];

// UNIT CONVERSIONS
const UNIT_CONVERSIONS = {
    'length': {
        units: ['mm', 'cm', 'm', 'km', 'inch', 'feet', 'mile'],
        toMeters: {
            'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000,
            'inch': 0.0254, 'feet': 0.3048, 'mile': 1609.34
        }
    },
    'weight': {
        units: ['g', 'kg', 'tonne', 'pound', 'ounce'],
        toGrams: {
            'g': 1, 'kg': 1000, 'tonne': 1000000,
            'pound': 453.592, 'ounce': 28.3495
        }
    },
    'volume': {
        units: ['ml', 'l', 'cm³', 'm³'],
        toMl: {
            'ml': 1, 'l': 1000, 'cm³': 1, 'm³': 1000000
        }
    },
    'temperature': {
        units: ['celsius', 'fahrenheit', 'kelvin'],
        special: true
    }
};

/**
 * CALCULATOR FUNCTIONS
 */
function calcPress(value) {
    const display = document.getElementById('calcDisplay');
    if (!display) return;

    if (calcDisplay === '0' && !['.', '+', '-', '×', '÷'].includes(value)) {
        calcDisplay = value;
    } else {
        calcDisplay += value;
    }
    display.value = calcDisplay;
}

function calcClear() {
    calcDisplay = '0';
    const display = document.getElementById('calcDisplay');
    if (display) display.value = '0';
}

function calcDelete() {
    calcDisplay = calcDisplay.slice(0, -1) || '0';
    const display = document.getElementById('calcDisplay');
    if (display) display.value = calcDisplay;
}

function calcEvaluate() {
    try {
        let expr = calcDisplay.replace(/×/g, '*').replace(/÷/g, '/');
        // Replace common math functions
        expr = expr.replace(/sqrt\(/g, 'Math.sqrt(');
        expr = expr.replace(/sin\(/g, 'Math.sin(');
        expr = expr.replace(/cos\(/g, 'Math.cos(');
        expr = expr.replace(/tan\(/g, 'Math.tan(');
        expr = expr.replace(/log\(/g, 'Math.log10(');
        expr = expr.replace(/ln\(/g, 'Math.log(');
        expr = expr.replace(/π/g, 'Math.PI');
        expr = expr.replace(/\^/g, '**');

        const result = eval(expr);
        const formatted = Number.isInteger(result) ? result : parseFloat(result.toFixed(8));
        calcHistory.push(`${calcDisplay} = ${formatted}`);
        calcDisplay = formatted.toString();

        const display = document.getElementById('calcDisplay');
        if (display) display.value = calcDisplay;

        updateCalcHistory();
    } catch (e) {
        calcDisplay = 'Error';
        const display = document.getElementById('calcDisplay');
        if (display) display.value = 'Error';
    }
}

function calcFunction(func) {
    try {
        const value = parseFloat(calcDisplay);
        let result;
        switch (func) {
            case 'sqrt': result = Math.sqrt(value); break;
            case 'square': result = value * value; break;
            case 'cube': result = value * value * value; break;
            case 'reciprocal': result = 1 / value; break;
            case 'sin': result = Math.sin(value * Math.PI / 180); break;
            case 'cos': result = Math.cos(value * Math.PI / 180); break;
            case 'tan': result = Math.tan(value * Math.PI / 180); break;
            case 'log': result = Math.log10(value); break;
            case 'ln': result = Math.log(value); break;
            case 'percent': result = value / 100; break;
            case 'negate': result = -value; break;
            case 'pi': result = Math.PI; break;
            default: return;
        }
        calcHistory.push(`${func}(${value}) = ${result}`);
        calcDisplay = parseFloat(result.toFixed(8)).toString();
        const display = document.getElementById('calcDisplay');
        if (display) display.value = calcDisplay;
        updateCalcHistory();
    } catch (e) {
        calcDisplay = 'Error';
    }
}

function updateCalcHistory() {
    const histDiv = document.getElementById('calcHistory');
    if (histDiv) {
        histDiv.innerHTML = calcHistory.slice(-5).reverse().map(h => `<div>${h}</div>`).join('');
    }
}

/**
 * FORMULAS DISPLAY
 */
function showFormulas() {
    const container = document.getElementById('toolContent');
    let html = '<div class="formulas-container">';

    for (const [subject, topics] of Object.entries(FORMULAS)) {
        const icon = subject === 'Mathematics' ? '📐' : '🔬';
        html += `<h2 class="section-title">${icon} ${subject} Formulas</h2>`;

        for (const topic of topics) {
            html += `
                <div class="formula-topic">
                    <h3>${topic.topic}</h3>
                    <ul class="formula-list">
                        ${topic.formulas.map(f => `<li>${f}</li>`).join('')}
                    </ul>
                </div>
            `;
        }
    }

    html += '</div>';
    container.innerHTML = html;
}

/**
 * CALCULATOR DISPLAY
 */
function showCalculator() {
    const container = document.getElementById('toolContent');
    container.innerHTML = `
        <div class="calculator">
            <h2 class="section-title">🧮 Scientific Calculator</h2>
            <input type="text" id="calcDisplay" class="calc-display" value="0" readonly>
            <div class="calc-history" id="calcHistory"></div>
            <div class="calc-buttons">
                <button onclick="calcFunction('sin')" class="calc-btn calc-fn">sin</button>
                <button onclick="calcFunction('cos')" class="calc-btn calc-fn">cos</button>
                <button onclick="calcFunction('tan')" class="calc-btn calc-fn">tan</button>
                <button onclick="calcFunction('log')" class="calc-btn calc-fn">log</button>
                <button onclick="calcFunction('ln')" class="calc-btn calc-fn">ln</button>

                <button onclick="calcFunction('sqrt')" class="calc-btn calc-fn">√</button>
                <button onclick="calcFunction('square')" class="calc-btn calc-fn">x²</button>
                <button onclick="calcFunction('cube')" class="calc-btn calc-fn">x³</button>
                <button onclick="calcFunction('reciprocal')" class="calc-btn calc-fn">1/x</button>
                <button onclick="calcFunction('pi')" class="calc-btn calc-fn">π</button>

                <button onclick="calcClear()" class="calc-btn calc-clear">AC</button>
                <button onclick="calcDelete()" class="calc-btn calc-clear">DEL</button>
                <button onclick="calcFunction('percent')" class="calc-btn calc-op">%</button>
                <button onclick="calcPress('(')" class="calc-btn calc-op">(</button>
                <button onclick="calcPress(')')" class="calc-btn calc-op">)</button>

                <button onclick="calcPress('7')" class="calc-btn calc-num">7</button>
                <button onclick="calcPress('8')" class="calc-btn calc-num">8</button>
                <button onclick="calcPress('9')" class="calc-btn calc-num">9</button>
                <button onclick="calcPress('÷')" class="calc-btn calc-op">÷</button>
                <button onclick="calcFunction('negate')" class="calc-btn calc-op">±</button>

                <button onclick="calcPress('4')" class="calc-btn calc-num">4</button>
                <button onclick="calcPress('5')" class="calc-btn calc-num">5</button>
                <button onclick="calcPress('6')" class="calc-btn calc-num">6</button>
                <button onclick="calcPress('×')" class="calc-btn calc-op">×</button>
                <button onclick="calcPress('^')" class="calc-btn calc-op">x^y</button>

                <button onclick="calcPress('1')" class="calc-btn calc-num">1</button>
                <button onclick="calcPress('2')" class="calc-btn calc-num">2</button>
                <button onclick="calcPress('3')" class="calc-btn calc-num">3</button>
                <button onclick="calcPress('-')" class="calc-btn calc-op">-</button>
                <button onclick="calcEvaluate()" class="calc-btn calc-equals" style="grid-row: span 2;">=</button>

                <button onclick="calcPress('0')" class="calc-btn calc-num" style="grid-column: span 2;">0</button>
                <button onclick="calcPress('.')" class="calc-btn calc-num">.</button>
                <button onclick="calcPress('+')" class="calc-btn calc-op">+</button>
            </div>
        </div>
    `;
}

/**
 * PERIODIC TABLE DISPLAY
 */
function showPeriodicTable() {
    const container = document.getElementById('toolContent');
    let html = '<h2 class="section-title">⚛️ Periodic Table</h2>';
    html += '<p class="section-info">Click any element to see details</p>';
    html += '<div class="periodic-table">';

    // Sort by atomic number
    const sorted = [...PERIODIC_TABLE].sort((a, b) => a.num - b.num);

    for (const elem of sorted) {
        html += `
            <div class="element ${elem.type}" onclick="showElement(${elem.num})">
                <div class="elem-num">${elem.num}</div>
                <div class="elem-sym">${elem.sym}</div>
                <div class="elem-name">${elem.name}</div>
                <div class="elem-mass">${elem.mass}</div>
            </div>
        `;
    }

    html += '</div>';
    html += `<div class="periodic-legend">
        <span class="legend nonmetal">Non-metal</span>
        <span class="legend metal">Post-Transition Metal</span>
        <span class="legend metalloid">Metalloid</span>
        <span class="legend alkali">Alkali Metal</span>
        <span class="legend alkaline">Alkaline Earth</span>
        <span class="legend transition">Transition Metal</span>
        <span class="legend lanthanide">Lanthanide</span>
        <span class="legend actinide">Actinide</span>
        <span class="legend halogen">Halogen</span>
        <span class="legend noble">Noble Gas</span>
    </div>
    <p style="text-align:center; margin-top:15px; color:var(--text-secondary); font-size:13px;">
        📚 All 118 known elements organized by atomic number, group, and period.
    </p>`;

    container.innerHTML = html;
}

function showElement(num) {
    const elem = PERIODIC_TABLE.find(e => e.num === num);
    if (!elem) return;

    openModal(`
        <div class="element-detail">
            <div class="elem-big ${elem.type}">
                <div class="elem-num-big">${elem.num}</div>
                <div class="elem-sym-big">${elem.sym}</div>
                <div class="elem-mass-big">${elem.mass}</div>
            </div>
            <h2>${elem.name}</h2>
            <div class="elem-info">
                <p><strong>Atomic Number:</strong> ${elem.num}</p>
                <p><strong>Symbol:</strong> ${elem.sym}</p>
                <p><strong>Atomic Mass:</strong> ${elem.mass} u</p>
                <p><strong>Group:</strong> ${elem.group}</p>
                <p><strong>Period:</strong> ${elem.period}</p>
                <p><strong>Type:</strong> ${elem.type}</p>
            </div>
            <button onclick="closeModal()" class="btn btn-primary">Close</button>
        </div>
    `);
}

/**
 * UNIT CONVERTER
 */
function showUnitConverter() {
    const container = document.getElementById('toolContent');
    container.innerHTML = `
        <h2 class="section-title">📏 Unit Converter</h2>
        <div class="converter-container">
            <div class="form-group">
                <label>Category:</label>
                <select id="convCategory" onchange="updateConverter()">
                    <option value="length">Length</option>
                    <option value="weight">Weight</option>
                    <option value="volume">Volume</option>
                    <option value="temperature">Temperature</option>
                </select>
            </div>

            <div class="converter-row">
                <div class="form-group">
                    <label>From:</label>
                    <input type="number" id="convFrom" value="1" oninput="performConversion()">
                    <select id="convFromUnit" onchange="performConversion()"></select>
                </div>

                <div class="converter-equals">=</div>

                <div class="form-group">
                    <label>To:</label>
                    <input type="number" id="convTo" value="0" readonly>
                    <select id="convToUnit" onchange="performConversion()"></select>
                </div>
            </div>

            <div id="convResult" class="conv-result"></div>
        </div>
    `;
    updateConverter();
}

function updateConverter() {
    const cat = document.getElementById('convCategory').value;
    const fromSel = document.getElementById('convFromUnit');
    const toSel = document.getElementById('convToUnit');

    fromSel.innerHTML = '';
    toSel.innerHTML = '';

    let units = [];
    if (cat === 'temperature') {
        units = ['celsius', 'fahrenheit', 'kelvin'];
    } else {
        units = UNIT_CONVERSIONS[cat].units;
    }

    units.forEach((u, i) => {
        const opt1 = new Option(u, u);
        const opt2 = new Option(u, u);
        fromSel.add(opt1);
        toSel.add(opt2);
    });

    toSel.selectedIndex = 1;
    performConversion();
}

function performConversion() {
    const cat = document.getElementById('convCategory').value;
    const from = parseFloat(document.getElementById('convFrom').value) || 0;
    const fromUnit = document.getElementById('convFromUnit').value;
    const toUnit = document.getElementById('convToUnit').value;
    let result = 0;

    if (cat === 'temperature') {
        // Convert to Celsius first
        let celsius;
        if (fromUnit === 'celsius') celsius = from;
        else if (fromUnit === 'fahrenheit') celsius = (from - 32) * 5 / 9;
        else if (fromUnit === 'kelvin') celsius = from - 273.15;

        if (toUnit === 'celsius') result = celsius;
        else if (toUnit === 'fahrenheit') result = celsius * 9 / 5 + 32;
        else if (toUnit === 'kelvin') result = celsius + 273.15;
    } else {
        const conv = UNIT_CONVERSIONS[cat];
        const key = cat === 'length' ? 'toMeters' : cat === 'weight' ? 'toGrams' : 'toMl';
        const baseValue = from * conv[key][fromUnit];
        result = baseValue / conv[key][toUnit];
    }

    document.getElementById('convTo').value = parseFloat(result.toFixed(6));
    const resDiv = document.getElementById('convResult');
    if (resDiv) {
        resDiv.innerHTML = `<strong>${from} ${fromUnit}</strong> = <strong>${result.toFixed(6)} ${toUnit}</strong>`;
    }
}

/**
 * Tool switcher
 */
function switchTool(tool) {
    document.querySelectorAll('.tool-tab-btn').forEach(b => b.classList.remove('active'));
    document.getElementById(`tool-${tool}-btn`).classList.add('active');

    switch (tool) {
        case 'calculator': showCalculator(); break;
        case 'formulas': showFormulas(); break;
        case 'periodic': showPeriodicTable(); break;
        case 'converter': showUnitConverter(); break;
    }
}

document.addEventListener('DOMContentLoaded', () => {
    const toolsBtn = document.getElementById('toolsBtn');
    if (toolsBtn) {
        toolsBtn.addEventListener('click', () => {
            switchPanel('toolsPanel', toolsBtn);
            showCalculator();
        });
    }
});
