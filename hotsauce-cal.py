class Pepper:
    def __init__(self, name, min_shu, max_shu, avg_weight_g, origin, description=""):
        self.name = name
        self.min_shu = min_shu
        self.max_shu = max_shu
        self.avg_weight_g = avg_weight_g
        self.origin = origin
        self.description = description
    
    def average_shu(self):
        return (self.min_shu + self.max_shu) // 2


class HotSauceCalculator:
    BOTTLE_SIZES = {
        '1oz': 30, '2oz': 60, '5oz': 150, '10oz': 300,
        '16oz': 480, '32oz': 960, '64oz': 1890
    }

    PEPPERS = {
        # No heat (0 SHU)
        'bell': Pepper("Bell Pepper", 0, 0, 120, "Americas", "Sweet, no heat"),
        'pimento': Pepper("Pimento", 0, 0, 40, "Americas", "Sweet, heart-shaped"),
        'sweet banana': Pepper("Sweet Banana", 0, 0, 30, "Hungary", "Mild and sweet"),
        
        # Mild (100-2,500 SHU)
        'poblano': Pepper("Poblano", 1000, 1500, 40, "Mexico", "Mild, used for chiles rellenos"),
        'anaheim': Pepper("Anaheim", 500, 2500, 25, "USA", "Mild, good for roasting"),
        'cubanelle': Pepper("Cubanelle", 100, 1000, 20, "Cuba", "Sweet with slight heat"),
        'pepperoncini': Pepper("Pepperoncini", 100, 500, 15, "Italy/Greece", "Mild tangy flavor"),
        'cherry': Pepper("Cherry Pepper", 100, 500, 10, "Americas", "Round, sweet and mild"),
        'shishito': Pepper("Shishito", 50, 200, 5, "Japan", "Blistered as appetizer"),
        'trinidad perfume': Pepper("Trinidad Perfume", 0, 500, 8, "Trinidad", "Fragrant with no heat"),
        
        # Medium (2,500-15,000 SHU)
        'jalapeno': Pepper("Jalapeño", 2500, 8000, 15, "Mexico", "Classic medium heat"),
        'guajillo': Pepper("Guajillo", 2500, 5000, 5, "Mexico", "Dried mirasol chili"),
        'chipotle': Pepper("Chipotle", 5000, 10000, 3, "Mexico", "Smoke-dried jalapeño"),
        'fresno': Pepper("Fresno", 2500, 10000, 12, "USA", "Similar to jalapeño"),
        'serrano': Pepper("Serrano", 10000, 23000, 5, "Mexico", "Hotter than jalapeño"),
        'cayenne': Pepper("Cayenne", 30000, 50000, 5, "French Guiana", 
                 "Classic thin red chili, staple in hot sauces and spice racks"),
        'aji amarillo': Pepper("Aji Amarillo", 30000, 50000, 10, "Peru", "Fruity yellow chili"),
        'hungarian wax': Pepper("Hungarian Wax", 1000, 15000, 20, "Hungary", "Varies from mild to hot"),
        'cascabel': Pepper("Cascabel", 1500, 2500, 5, "Mexico", "Rattlesnake-like seeds"),
        'mirasol': Pepper("Mirasol", 2500, 5000, 4, "Peru", "Sun-facing chili"),
        'chile de arbol': Pepper("Chile de Árbol", 15000, 30000, 2, "Mexico", "Thin and very hot"),
        
        # Hot (50,000-350,000 SHU)
        'habanero': Pepper("Habanero", 100000, 350000, 10, "Amazon", "Fruity and very hot"),
        'scotch bonnet': Pepper("Scotch Bonnet", 100000, 350000, 8, "Caribbean", "Similar to habanero"),
        'bird\'s eye': Pepper("Bird's Eye Chili", 50000, 100000, 2, "Africa/Asia", "Small but potent"),
        'piri piri': Pepper("Piri Piri", 50000, 175000, 3, "Africa", "Portuguese-African chili"),
        'tien tsin': Pepper("Tien Tsin", 50000, 75000, 1, "China", "Used in Sichuan cuisine"),
        'aji limon': Pepper("Aji Limon", 30000, 50000, 5, "Peru", "Lemon-flavored heat"),
        'manzano': Pepper("Manzano", 12000, 30000, 15, "Mexico", "Apple-shaped with black seeds"),
        'pequin': Pepper("Pequin", 40000, 58000, 1, "Mexico", "Small but powerful"),
        'santaka': Pepper("Santaka", 50000, 100000, 2, "Japan", "Asian bird pepper"),
        'tabiche': Pepper("Tabiche", 70000, 120000, 3, "Mexico", "Wild Oaxacan chili"),
        
        # Very Hot (350,000-1,000,000 SHU)
        'ghost': Pepper("Ghost Pepper (Bhut Jolokia)", 855000, 1040000, 7, "India", "Former world's hottest"),
        'red savina': Pepper("Red Savina Habanero", 350000, 580000, 12, "USA", "Former record holder"),
        'fatalii': Pepper("Fatalii", 125000, 400000, 10, "Africa", "Citrusy and extremely hot"),
        'devil\'s tongue': Pepper("Devil's Tongue", 125000, 325000, 9, "USA", "Habanero variant"),
        'chocolate habanero': Pepper("Chocolate Habanero", 300000, 500000, 11, "Trinidad", "Earthy flavor"),
        'trinidad scorpion': Pepper("Trinidad Scorpion", 1200000, 2000000, 5, "Trinidad", "Extremely hot"),
        '7 pot': Pepper("7 Pot Pepper", 800000, 1500000, 4, "Trinidad", "Hot enough for 7 pots"),
        'brain strain': Pepper("Brain Strain", 1000000, 1500000, 5, "Trinidad", "Wrinkled like a brain"),
        'moruga scorpion': Pepper("Moruga Scorpion", 1200000, 2000000, 6, "Trinidad", "Former record holder"),
        'dorset naga': Pepper("Dorset Naga", 800000, 1200000, 5, "UK", "British superhot"),
        
        # Extremely Hot (1,000,000+ SHU)
        'carolina reaper': Pepper("Carolina Reaper", 1400000, 2200000, 5, "USA", "Current world record holder"),
        'pepper x': Pepper("Pepper X", 3180000, 3180000, 4, "USA", "Unofficial record holder"),
        'apocalypse scorpion': Pepper("Apocalypse Scorpion", 1200000, 1500000, 5, "Trinidad", "Doomsday heat"),
        'komodo dragon': Pepper("Komodo Dragon", 1400000, 2200000, 6, "UK", "Reaper relative"),
        'dragon\'s breath': Pepper("Dragon's Breath", 2480000, 2480000, 5, "UK", "Medical use potential"),
        'chocolate plague': Pepper("Chocolate Plague", 1300000, 1700000, 5, "USA", "Dark and deadly"),
        'infinity chili': Pepper("Infinity Chili", 1175000, 1175000, 4, "UK", "Brief record holder"),
        'naga viper': Pepper("Naga Viper", 900000, 1380000, 5, "UK", "Unstable hybrid"),
        'bhut jolokia chocolate': Pepper("Bhut Jolokia Chocolate", 800000, 1000000, 7, "India", "Earthy ghost"),
        'trinidad moruga': Pepper("Trinidad Moruga", 2000000, 2000000, 6, "Trinidad", "Peak heat"),
        
        # Special Varieties
        'aji charapita': Pepper("Aji Charapita", 30000, 50000, 1, "Peru", "Wild Amazonian berry pepper"),
        'bishop\'s crown': Pepper("Bishop's Crown", 5000, 15000, 10, "Caribbean", "Distinctive shape"),
        'black cobra': Pepper("Black Cobra", 30000, 40000, 3, "India", "Dark ornamental"),
        'black pearl': Pepper("Black Pearl", 10000, 30000, 2, "USA", "Ornamental beauty"),
        'buena mulata': Pepper("Buena Mulata", 15000, 30000, 8, "Cuba", "Color-changing"),
        'elephant trunk': Pepper("Elephant Trunk", 25000, 40000, 15, "Brazil", "Long curved pods"),
        'lemon drop': Pepper("Lemon Drop", 15000, 30000, 3, "Peru", "Citrusy aji"),
        'peter pepper': Pepper("Peter Pepper", 10000, 23000, 10, "USA", "Distinctive shape"),
        'purple ufo': Pepper("Purple UFO", 30000, 50000, 5, "Hungary", "Unique appearance"),
        'white habanero': Pepper("White Habanero", 100000, 350000, 9, "Mexico", "Rare white variety")
    }
    
    # Enhanced neutralizer recommendations
    NEUTRALIZERS = [
        ("Dairy products", "Milk, yogurt, or sour cream (full-fat works best)"),
        ("Starchy foods", "White bread, rice, or potatoes to absorb capsaicin"),
        ("Sugar", "Honey, sugar cube, or sweet fruit to counteract burning"),
        ("Fatty foods", "Avocado, peanut butter, or olive oil to dissolve capsaicin"),
        ("Alcohol (careful!)", "A shot of liquor may help (but can spread the burn)"),
        ("Coconut milk", "The fat and sugar combo is doubly effective")
    ]
    
    def __init__(self):
        self.peppers_used = []
        self.total_volume_ml = 0
    
    def add_pepper_by_count(self, pepper_type, count, bottle_size=None):
        """Add peppers by count to existing bottle or new bottle"""
        if pepper_type.lower() not in self.PEPPERS:
            similar = self.find_similar_peppers(pepper_type)
            if similar:
                raise ValueError(f"Unknown pepper. Similar: {', '.join(similar)}")
            raise ValueError(f"Unknown pepper type: {pepper_type}")
        
        # If bottle_size is provided, set/update the total volume
        if bottle_size:
            if bottle_size not in self.BOTTLE_SIZES:
                raise ValueError(f"Unknown bottle size. Options: {', '.join(self.BOTTLE_SIZES.keys())}")
            self.total_volume_ml = self.BOTTLE_SIZES[bottle_size]
        # If no bottle_size provided but no volume set yet, use default 5oz
        elif not self.total_volume_ml:
            self.total_volume_ml = self.BOTTLE_SIZES['5oz']
        
        pepper = self.PEPPERS[pepper_type.lower()]
        total_grams = count * pepper.avg_weight_g
        
        self.peppers_used.append({
            'type': pepper_type.lower(),
            'count': count,
            'total_grams': total_grams
        })

    
    def find_similar_peppers(self, name):
        """Find peppers with similar names"""
        name = name.lower()
        return [p for p in self.PEPPERS if name in p or p in name][:3]
    
    def calculate_shu(self):
        """Accurate SHU calculation with non-linear scaling for superhots"""
        if not self.peppers_used or self.total_volume_ml <= 0:
            return 0

        # Separate superhot peppers (>1M SHU) for special handling
        superhot_peppers = []
        normal_peppers = []
        
        for pepper in self.peppers_used:
            pepper_data = self.PEPPERS[pepper['type']]
            if pepper_data.average_shu() >= 1000000:
                superhot_peppers.append(pepper)
            else:
                normal_peppers.append(pepper)

        # Calculate normal pepper contribution
        normal_shu = sum(
            (p['total_grams'] * self.PEPPERS[p['type']].average_shu()) 
            for p in normal_peppers
        ) / self.total_volume_ml

        # Calculate superhot pepper contribution (non-linear scaling)
        superhot_shu = 0
        for pepper in superhot_peppers:
            pepper_data = self.PEPPERS[pepper['type']]
            base_shu = pepper_data.average_shu()
            weight = pepper['total_grams']
            
            # Non-linear scaling for superhots
            if base_shu >= 3000000:  # Pepper X territory
                superhot_shu += (weight * base_shu**0.7) / 1000
            elif base_shu >= 1000000:  # Other superhots
                superhot_shu += (weight * base_shu**0.8) / 1000

        total_shu = normal_shu + (superhot_shu / self.total_volume_ml)
        
        # Ensure minimum SHU reflects the hottest pepper present
        if superhot_peppers:
            min_shu = max(p['total_grams'] * self.PEPPERS[p['type']].min_shu 
                        for p in superhot_peppers) / self.total_volume_ml
            total_shu = max(total_shu, min_shu)

        return int(total_shu)
    
    def get_heat_description(self, shu):
        """Human-readable heat level with safety warnings"""
        if shu == 0: return "No heat - sweet pepper"
        elif shu < 100: return "Barely perceptible warmth"
        elif shu < 500: return "Very mild - noticeable but not spicy"
        elif shu < 1000: return "Mild - gentle warmth"
        elif shu < 2500: return "Medium mild - noticeable but pleasant"
        elif shu < 5000: return "Medium - good balance of flavor and heat"
        elif shu < 15000: return "Medium hot - solid spicy kick"
        elif shu < 50000: return "Hot - significant burning sensation"
        elif shu < 100000: return "Very hot - approaching habanero level"
        elif shu < 350000: return "Extremely hot - serious heat experience"
        elif shu < 1000000: return "Insanely hot - potentially painful"
        else: return "DANGEROUSLY HOT - handle with extreme caution"
    
    def get_safety_warning(self, shu):
        """Specific safety recommendations based on SHU"""
        if shu >= 3000000:
            return ("🚨 MILITARY-GRADE HEAT: Not for human consumption! "
                    "May cause chemical burns. Use gloves and eye protection.")
        elif shu >= 1000000:
            return ("⚠️ WEAPON-LEVEL HEAT: Extreme caution required. "
                    "Use gloves. Taste only toothpick amounts with dairy ready.")
        elif shu >= 350000:
            return ("🔥 EXTREME HEAT: Have dairy ready. "
                    "Start with 1/4 teaspoon servings.")
        elif shu >= 50000:
            return "🌶️ Very Hot: Caution advised for sensitive individuals."
        else:
            return "Enjoy safely!"

    def display_pepper_list(self):
        """Show available peppers with key info"""
        print("\nAvailable Peppers (name | avg weight | SHU range):")
        for name, pepper in sorted(self.PEPPERS.items(), key=lambda x: x[1].average_shu()):
            print(f"- {pepper.name: <22} | {pepper.avg_weight_g: >3}g each | {pepper.min_shu:,}-{pepper.max_shu:,} SHU")

    def display_bottle_sizes(self):
        """Show available bottle size options"""
        print("\nStandard Bottle Sizes:")
        for i, (size, ml) in enumerate(self.BOTTLE_SIZES.items(), 1):
            print(f"{i}. {size: <5} = {ml}ml ({ml/30:.1f} fl oz)")

    def get_bottle_size(self, input_str):
        """Get bottle size from either number or label"""
        # Try to match by number first
        if input_str.isdigit():
            num = int(input_str)
            sizes = list(self.BOTTLE_SIZES.keys())
            if 1 <= num <= len(sizes):
                return sizes[num-1]
        
        # Try to match by label (with or without 'oz')
        clean_input = input_str.lower().replace('oz', '').strip()
        for size in self.BOTTLE_SIZES:
            if clean_input == size.replace('oz', '').strip():
                return size
        
        return None


def main():
    calculator = HotSauceCalculator()
    
    print("🔥 Ultimate Hot Sauce Calculator 🔥")
    print("(Now with cumulative additions to existing bottles)")
    print("-------------------------------------------------")
    
    while True:
        print("\nMENU:")
        print("1. View available peppers")
        print("2. View bottle sizes")
        print("3. Add peppers to your sauce")
        print("4. Calculate SHU")
        print("5. Start new sauce (reset)")
        print("6. Exit")
        
        choice = input("Select option (1-6): ").strip()
        
        if choice == "1":
            calculator.display_pepper_list()
        elif choice == "2":
            calculator.display_bottle_sizes()
        elif choice == "3":
            try:
                calculator.display_pepper_list()
                pepper_type = input("\nEnter pepper type: ").strip().lower()
                if pepper_type == 'back': continue
                
                count = int(input("How many peppers? "))
                if count <= 0:
                    print("Must be at least 1 pepper")
                    continue
                
                # Only ask for bottle size if no volume set yet
                if not calculator.total_volume_ml:
                    calculator.display_bottle_sizes()
                    bottle_input = input("Select bottle size (enter number or size like '5oz'): ").strip()
                    bottle_size = calculator.get_bottle_size(bottle_input)
                    if not bottle_size:
                        raise ValueError(f"Invalid size. Options: {', '.join(calculator.BOTTLE_SIZES.keys())}")
                else:
                    bottle_size = None
                    print(f"Adding to existing {calculator.total_volume_ml}ml batch")
                
                calculator.add_pepper_by_count(pepper_type, count, bottle_size)
                pepper = calculator.PEPPERS[pepper_type]
                print(f"Added {count} {pepper.name} peppers (~{count * pepper.avg_weight_g}g)")
                
            except (ValueError, KeyError) as e:
                print(f"Error: {e}")
        elif choice == "4":
            if not calculator.peppers_used:
                print("No peppers added yet!")
                continue
                
            print("\nYour Hot Sauce Composition:")
            total_grams = 0
            for pepper in calculator.peppers_used:
                p_data = calculator.PEPPERS[pepper['type']]
                print(f"- {pepper['count']} {p_data.name} peppers = {pepper['total_grams']}g")
                total_grams += pepper['total_grams']
            
            shu = calculator.calculate_shu()
            print(f"\nTotal pepper weight: {total_grams}g")
            print(f"Total volume: {calculator.total_volume_ml}ml")
            print(f"\nEstimated SHU: {shu:,}")
            print(f"Heat level: {calculator.get_heat_description(shu)}")
            print(f"Safety: {calculator.get_safety_warning(shu)}")
            
            if shu > 50000:
                print("\nRecommended Neutralizers:")
                for item in calculator.NEUTRALIZERS:
                    print(f"- {item[0]}: {item[1]}")
        elif choice == "5":
            calculator.peppers_used = []
            calculator.total_volume_ml = 0
            print("\nStarted new sauce batch!")
        elif choice == "6":
            print("Happy saucing! 🌶️")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
