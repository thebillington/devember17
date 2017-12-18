// Code to house a simple snake game
// Time started: 21:45
// Time finished: 

// Store the grid size
gridSize = 20;

// Canvas size
cSize = 600;

// Setup function
function setup() {
    
    // Create a canvas
    createCanvas(cSize, cSize);
    
}

// Render function
function draw() {
    
    // Draw the grid
    drawGrid();
    
}

// Create a function to render the grid
function drawGrid() {
    
    // Calculate pixel size
    var pixelSize = width / gridSize;
    
    // Loop
    for (var i = 0; i < gridSize; i++) {
        for(var j = 0; j < gridSize; j++) {
    
            color(0);
            
            // Get x and y
            var x = i * pixelSize;
            var y = j * pixelSize;
            
            // Draw a quad at the correct location
            quad(x, y, x + pixelSize, y, x + pixelSize, y + pixelSize, x, y + pixelSize);
            
        }
        
    }
    
}