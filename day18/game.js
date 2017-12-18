// Code to house a simple snake game
// Time started: 21:45
// Time finished: 

// Store the grid size
var gridSize = 20;

// Canvas size
var cSize = 600;

// Pixel size
var pixelSize;

// List to hold the snake
var snake;

// Snake speed
var speed;

// Function to return a coordinate
function Coord(x, y) {
    
    // Return the object
    return {"x": x, "y": y};
    
}

// Setup function
function setup() {
    
    // Create a canvas
    createCanvas(cSize, cSize);
    
    // Calculate pixel size
    pixelSize = width / gridSize;
    
    // Create the snake
    snake = [Coord(2, 0), Coord(1, 0), Coord(0, 0)];
    
    // Set the snakes speed
    speed = {"dx": 1, "dy": 0};
    
}

// Render function
function draw() {
    
    // Draw the grid
    drawGrid();
    
    // Draw the snake
    drawSnake();
    
}

// Function to drawe a snake
function drawSnake() {
    
    // Draw each of the pixels
    for (var i = 0; i < snake.length; i++) {
        
        console.log(snake[i]);
        
        // Get the x and y
        var x = snake[i].x * pixelSize;
        var y = snake[i].y * pixelSize;
        
        // Fill the pixel
        color(0);
        fill(0);
        quad(x, y, x + pixelSize, y, x + pixelSize, y + pixelSize, x, y + pixelSize);
        
    }
    
}

// Create a function to render the grid
function drawGrid() {
    
    // Loop
    for (var i = 0; i < gridSize; i++) {
        for(var j = 0; j < gridSize; j++) {
            
            // Fill color
            color(0);
            fill(255);
            
            // Get x and y
            var x = i * pixelSize;
            var y = j * pixelSize;
            
            // Draw a quad at the correct location
            quad(x, y, x + pixelSize, y, x + pixelSize, y + pixelSize, x, y + pixelSize);
            
        }
        
    }
    
}