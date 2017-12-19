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

// Store the powerup
var powerup;

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
    speed = {"dx": 0, "dy": 1};
    
    // Generate a powerup
    powerup = getRandCoord();
    
}

// Render function
function draw() {
    
    // Draw the grid
    drawGrid();
    
    // Draw the powerup
    drawGridSquare(powerup.x * pixelSize, powerup.y * pixelSize, color(255, 0, 0));
    
    // Draw the snake
    drawSnake();
    
    // Update the snake
    updateSnake();
    
    // Check if the powrup was eaten
    eaten();
    
}

// Function to update the snake
function updateSnake() {
    
    // Move each of the pixels
    for (var i = snake.length - 1; i > 0; i--) {
        
        // Move the pixel to the previous location
        snake[i] = {"x":snake[i - 1].x, "y":snake[i - 1].y};
        
    }
    
    // Move the last location by speed
    snake[0] = {"x": snake[0].x + speed.dx, "y": snake[0].y + speed.dy}
    
    // Check if the head has wrapped
    if (snake[0].x < 0) {
        snake[0].x = gridSize - 1;
    }
        
    if (snake[0].x >= gridSize) {
        snake[0].x = 0;
    }
    if (snake[0].y < 0) {
        snake[0].y = gridSize - 1;
    }
        
    if (snake[0].y >= gridSize) {
        snake[0].y = 0;
    }
    
}

// Function to check if the player has eaten the powerup
function eaten() {
    
    // If the tail has collided with the powerup
    if (snake[snake.length - 1].x == powerup.x && snake[snake.length - 1].y == powerup.y) {
        
        // Update the snake
        updateSnake();
        
        // Add to the tail of the snake
        snake.push(powerup);
        
        // Generate a new powerup
        powerup = getRandCoord();
        
    }
    
}

// Function to draw a gridSquare
function drawGridSquare(x, y, colour) {
    
    // Set the colour
    color(0);
    fill(colour);
    
    // Draw
    quad(x, y, x + pixelSize, y, x + pixelSize, y + pixelSize, x, y + pixelSize);
    
}

// Function to drawe a snake
function drawSnake() {
    
    // Draw each of the pixels
    for (var i = 0; i < snake.length; i++) {
        
        // Get the x and y
        var x = snake[i].x * pixelSize;
        var y = snake[i].y * pixelSize;
        
        // Fill the pixel
        drawGridSquare(x, y, 0);
        
    }
    
}

// Create a function to render the grid
function drawGrid() {
    
    // Loop
    for (var i = 0; i < gridSize; i++) {
        for(var j = 0; j < gridSize; j++) {
            
            // Get x and y
            var x = i * pixelSize;
            var y = j * pixelSize;
            
            // Draw a quad at the correct location
            drawGridSquare(x, y, 255);
            
        }
        
    }
    
}

// Check for key presses
function keyPressed() {
    
    // Check the value
    if (keyCode == LEFT_ARROW) {
        
        // Set the speed
        speed = {"dx": -1, "dy": 0}
    }
    if (keyCode == RIGHT_ARROW) {
        
        // Set the speed
        speed = {"dx": 1, "dy": 0}
    }
    if (keyCode == UP_ARROW) {
        
        // Set the speed
        speed = {"dx": 0, "dy": -1}
    }
    if (keyCode == DOWN_ARROW) {
        
        // Set the speed
        speed = {"dx": 0, "dy": 1}
    }
    
}

// Function to generate a random coordinate
function getRandCoord() {
    
    // Return a random coordinate in the grid
    return {x: Math.floor(Math.random() * (gridSize) + 1), y: Math.floor(Math.random() * (gridSize) + 1)}
    
}