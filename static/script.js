function addOptions()
{
    // Adding Restaurant Types
    const restTypes = ['Select-Rest-Type', 'Lounge', 'Kiosk', 'Food Truck', 'Irani Cafee',
                        'Confectionery', 'Cafe', 'Microbrewery', 'Dhaba', 'Takeaway', 'Pop Up',
                        'Pub', 'Bar', 'Delivery', 'Meat Shop', 'Beverage Shop', 'Dessert Parlor',
                        'Club', 'Quick Bites', 'Bhojanalya', 'Casual Dining', 'Fine Dining', 'Mess',
                        'Sweet Shop', 'Food Court', 'Bakery'];

    let dropdown = document.getElementById("RT");

    for(let i = 0; i < restTypes.length; i++)
    {
        dropdown.options[dropdown.options.length] = new Option(restTypes[i], restTypes[i]);
    }


    // Adding Cuisines
    const cuisines = ["Select-Cuisines", "Rajasthani", "Mediterranean", "Desserts", "Burmese",
                        "Tibetan", "Belgian", "Seafood", "Raw Meats", "Greek", "African", "Russian",
                        "Italian", "Grill", "Korean", "Ice Cream", "Coffee", "Spanish", "Nepalese",
                        "Afghani", "Momos", "Bar Food", "South American", "Middle Eastern", "Malaysian",
                        "Salad", "Bubble Tea", "German", "Bohri", "Asian", "Hyderabadi", "Tamil", "Turkish",
                        "Arabian", "Sushi", "Awadhi", "Kerala", "Bengali", "Afghan", "Andhra", "Konkan",
                        "Indonesian", "Street Food", "Goan", "Chinese", "BBQ", "Wraps", "Continental", 
                        "Lucknowi", "Bihari", "Sandwich", "Cantonese", "Paan", "Charcoal Chicken", "Iranian",
                        "Portuguese", "Parsi", "Lebanese", "Sindhi", "Naga", "Rolls", "Mithai", "Hot dogs",
                        "Finger Food", "Thai", "Burger", "Juices", "Healthy Food", "Roast Chicken", "Pan Asian",
                        "Assamese", "Vegan", "Tex-Mex", "Vietnamese", "Mughlai", "Gujarati", "Modern Indian",
                        "Steak", "Mongolian", "American", "North Eastern", "Jewish", "North Indian", "European",
                        "French", "Japanese", "Drinks Only", "Tea", "South Indian", "Indian", "Australian", 
                        "Malwani", "Fast Food", "Beverages", "Kebab", "Kashmiri", "Sri Lankan", "Oriya", 
                        "Mangalorean", "Singaporean", "Maharashtrian", "Mexican", "British", "Pizza", "Biryani",
                        "Chettinad"];

    dropdown = document.getElementById("C");

    for(let i = 0; i < cuisines.length; i++)
    {
        dropdown.options[dropdown.options.length] = new Option(cuisines[i], cuisines[i]);
    }
}

