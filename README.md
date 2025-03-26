# 🌶️ Hot Sauce Scoville Calculator

Calculate the heat level of your homemade hot sauces based on pepper types and quantities, with accurate SHU (Scoville Heat Units) estimation for superhot peppers.

## Features

- **50+ Pepper Varieties**: From mild bell peppers to extreme Pepper X
- **Bottle Size Support**: Common hot sauce bottle sizes (1oz to 64oz)
- **Accurate SHU Calculations**: Special non-linear scaling for superhot peppers
- **Safety Warnings**: Alerts for dangerous heat levels
- **Neutralizer Recommendations**: Best foods/drinks to counteract heat
- **Cumulative Additions**: Build your sauce recipe incrementally

## Installation

```bash
git clone https://github.com/airborne-commando/pepper-calculator.git && cd pepper-calculator && python hotsauce-cal.py
```

## Usage

1. Select peppers by name and quantity
2. Choose a bottle size (or continue adding to existing batch)
3. View calculated SHU and heat level
4. Get safety recommendations and neutralizer suggestions

### Example

```text
🔥 Ultimate Hot Sauce Calculator 🔥
---------------------------------

MENU:
1. View available peppers
2. View bottle sizes
3. Add peppers to your sauce
4. Calculate SHU
5. Start new sauce (reset)
6. Exit

Select option (1-6): 3

Enter pepper type: ghost
How many peppers? 2
Adding to existing 150ml batch
Added 2 Ghost Pepper peppers (~14g)

Select option (1-6): 4

Your Hot Sauce Composition:
- 2 Ghost Pepper peppers = 14g

Total pepper weight: 14g
Total volume: 150ml

Estimated SHU: 99,666
Heat level: Extremely hot - serious heat experience
Safety: 🔥 EXTREME HEAT: Have dairy ready. Start with 1/4 teaspoon servings.

Recommended Neutralizers:
- Dairy products: Milk, yogurt, or sour cream...
- Starchy foods: White bread, rice, or potatoes...
```

## Pepper Database

Includes comprehensive data on:
- Average weights per pepper
- Scoville ranges (min/max SHU)
- Origin information
- Heat level descriptions

## Bottle Sizes

| Size | Milliliters | Fluid Ounces |
|------|------------|--------------|
| 1oz  | 30ml       | 1.0 fl oz    |
| 2oz  | 60ml       | 2.0 fl oz    |
| 5oz  | 150ml      | 5.0 fl oz    |
| 10oz | 300ml      | 10.0 fl oz   |
| 16oz | 480ml      | 16.0 fl oz   |
| 32oz | 960ml      | 32.0 fl oz   |
| 64oz | 1890ml     | 63.0 fl oz   |
