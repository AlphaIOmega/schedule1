/**
 * This file contains the mapping of effect names to their corresponding colors.
 * Colors extracted from the Schedule 1 Wiki Effects page.
 */

const effectColors = {
    // Colors extracted from the HTML spans in the Effects page table
    "anti-gravity": "rgb(35, 91, 203)",       // Blue
    "athletic": "rgb(117, 200, 253)",         // Light blue
    "balding": "rgb(199, 146, 50)",           // Brown
    "bright-eyed": "rgb(190, 247, 253)",      // Pale blue
    "brighteyed": "rgb(190, 247, 253)",       // Pale blue (alternate spelling)
    "calming": "rgb(254, 208, 155)",          // Peach
    "calorie-dense": "rgb(254, 132, 244)",    // Pink
    "cyclopean": "rgb(254, 193, 116)",        // Orange
    "disorienting": "rgb(254, 117, 81)",      // Red-orange
    "electrifying": "rgb(85, 200, 253)",      // Blue
    "energizing": "rgb(154, 254, 109)",       // Light green
    "euphoric": "rgb(254, 234, 116)",         // Yellow
    "explosive": "rgb(254, 75, 64)",          // Red
    "focused": "rgb(117, 241, 253)",          // Blue
    "foggy": "rgb(176, 176, 175)",            // Gray
    "gingeritis": "rgb(254, 136, 41)",        // Orange
    "glowing": "rgb(133, 228, 89)",           // Green
    "jennerising": "rgb(254, 141, 248)",      // Pink
    "laxative": "rgb(118, 60, 37)",           // Brown
    "lethal": "rgb(159, 43, 34)",             // Dark red
    "long faced": "rgb(254, 217, 97)",        // Yellow
    "long-faced": "rgb(254, 217, 97)",        // Yellow (alternate spelling)
    "munchies": "rgb(201, 110, 87)",          // Brick red
    "paranoia": "rgb(196, 103, 98)",          // Reddish
    "refreshing": "rgb(178, 254, 152)",       // Light green
    "schizophrenia": "rgb(100, 90, 253)",     // Purple
    "sedating": "rgb(107, 95, 216)",          // Purple
    "seizure-inducing": "rgb(254, 233, 0)",   // Yellow
    "shrinking": "rgb(182, 254, 218)",        // Mint green
    "slippery": "rgb(162, 223, 253)",         // Light blue
    "smelly": "rgb(125, 188, 49)",            // Green
    "sneaky": "rgb(123, 123, 123)",           // Gray
    "spicy": "rgb(254, 107, 76)",             // Orange-red
    "thought-provoking": "rgb(254, 160, 203)", // Pink
    "thoughtprovoking": "rgb(254, 160, 203)",  // Pink (alternate spelling)
    "toxic": "rgb(95, 154, 49)",              // Green
    "tropic thunder": "rgb(254, 159, 71)",    // Orange
    "tropic-thunder": "rgb(254, 159, 71)",    // Orange (alternate spelling) 
    "tropicthunder": "rgb(254, 159, 71)",     // Orange (alternate spelling)
    "zombifying": "rgb(113, 171, 93)"         // Green
};

/**
 * Returns the color for a given effect name
 * @param {string} effectName - The name of the effect
 * @returns {string} - The color as an RGB value, or a default color if not found
 */
function getEffectColor(effectName) {
    // Normalize the effect name: convert to lowercase and remove spaces/hyphens
    const normalizedName = effectName.toLowerCase().replace(/[\s-]/g, '');
    
    // Try to find the exact match first
    if (effectColors[effectName.toLowerCase()]) {
        return effectColors[effectName.toLowerCase()];
    }
    
    // Try to find using normalized name
    if (effectColors[normalizedName]) {
        return effectColors[normalizedName];
    }
    
    // Return a default color if not found
    return "#cccccc"; // Light gray
}