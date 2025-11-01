/**
 * Shared JavaScript utilities for board game rendering
 * Provides base classes and functions reused across all game projects
 */

/**
 * Base BoardRenderer class
 * All game-specific renderers should extend this class
 */
class BoardRenderer {
    constructor(canvasId, boardSize, cellSize = null) {
        this.canvas = document.getElementById(canvasId);
        if (!this.canvas) {
            throw new Error(`Canvas with id "${canvasId}" not found`);
        }

        this.ctx = this.canvas.getContext('2d');
        this.boardSize = boardSize;  // e.g., 3 for 3×3, 8 for 8×8
        this.cellSize = cellSize || (this.canvas.width / boardSize);

        // Board state
        this.board = this.createEmptyBoard();
        this.highlightedCells = new Set();

        // Event handling
        this.clickCallback = null;
        this.hoverCallback = null;

        this.setupEventListeners();
    }

    /**
     * Create empty board (override in subclasses if needed)
     */
    createEmptyBoard() {
        return Array(this.boardSize).fill().map(() =>
            Array(this.boardSize).fill(0)
        );
    }

    /**
     * Setup mouse event listeners
     */
    setupEventListeners() {
        this.canvas.addEventListener('click', (e) => this.handleClick(e));
        this.canvas.addEventListener('mousemove', (e) => this.handleMouseMove(e));
        this.canvas.addEventListener('mouseleave', () => this.handleMouseLeave());
    }

    /**
     * Get cell coordinates from mouse event
     */
    getCellFromEvent(event) {
        const rect = this.canvas.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;

        const row = Math.floor(y / this.cellSize);
        const col = Math.floor(x / this.cellSize);

        if (row >= 0 && row < this.boardSize && col >= 0 && col < this.boardSize) {
            return { row, col };
        }
        return null;
    }

    /**
     * Handle click events
     */
    handleClick(event) {
        const cell = this.getCellFromEvent(event);
        if (cell && this.clickCallback) {
            this.clickCallback(cell.row, cell.col);
        }
    }

    /**
     * Handle mouse move events
     */
    handleMouseMove(event) {
        const cell = this.getCellFromEvent(event);
        if (cell && this.hoverCallback) {
            this.hoverCallback(cell.row, cell.col);
        }
    }

    /**
     * Handle mouse leave events
     */
    handleMouseLeave() {
        this.highlightedCells.clear();
        this.render();
    }

    /**
     * Set click callback
     */
    onClick(callback) {
        this.clickCallback = callback;
    }

    /**
     * Set hover callback
     */
    onHover(callback) {
        this.hoverCallback = callback;
    }

    /**
     * Update board state
     */
    updateBoard(board) {
        this.board = board;
        this.render();
    }

    /**
     * Highlight cells (for move hints, etc.)
     */
    highlightCells(cells) {
        this.highlightedCells = new Set(cells.map(c => `${c.row},${c.col}`));
        this.render();
    }

    /**
     * Clear canvas
     */
    clear() {
        this.ctx.clearRect(0, 0, this.canvas.width, this.canvas.height);
    }

    /**
     * Draw grid lines
     */
    drawGrid() {
        this.ctx.strokeStyle = '#bbb';
        this.ctx.lineWidth = 2;

        for (let i = 0; i <= this.boardSize; i++) {
            const pos = i * this.cellSize;

            // Vertical lines
            this.ctx.beginPath();
            this.ctx.moveTo(pos, 0);
            this.ctx.lineTo(pos, this.canvas.height);
            this.ctx.stroke();

            // Horizontal lines
            this.ctx.beginPath();
            this.ctx.moveTo(0, pos);
            this.ctx.lineTo(this.canvas.width, pos);
            this.ctx.stroke();
        }
    }

    /**
     * Draw highlighted cells
     */
    drawHighlights() {
        this.ctx.fillStyle = 'rgba(255, 235, 59, 0.3)';
        for (const key of this.highlightedCells) {
            const [row, col] = key.split(',').map(Number);
            this.ctx.fillRect(
                col * this.cellSize,
                row * this.cellSize,
                this.cellSize,
                this.cellSize
            );
        }
    }

    /**
     * Main render method (override in subclasses)
     */
    render() {
        this.clear();
        this.drawGrid();
        this.drawHighlights();
        // Subclasses should override to draw pieces
    }
}

/**
 * Utility function to make API calls
 */
async function apiCall(endpoint, method = 'POST', data = null) {
    const options = {
        method: method,
        headers: {
            'Content-Type': 'application/json',
        },
    };

    if (data) {
        options.body = JSON.stringify(data);
    }

    try {
        const response = await fetch(endpoint, options);
        if (!response.ok) {
            throw new Error(`API call failed: ${response.statusText}`);
        }
        return await response.json();
    } catch (error) {
        console.error('API Error:', error);
        throw error;
    }
}

/**
 * Utility function to show loading indicator
 */
function setLoading(elementId, isLoading) {
    const element = document.getElementById(elementId);
    if (element) {
        if (isLoading) {
            element.innerHTML = '<span class="loading"></span> Thinking...';
        } else {
            element.innerHTML = '';
        }
    }
}

/**
 * Utility function to update status message
 */
function setStatus(message, type = 'info') {
    const statusElement = document.getElementById('game-status');
    if (statusElement) {
        statusElement.textContent = message;
        statusElement.className = `status-message status-${type}`;
    }
}

/**
 * Utility function to update stat display
 */
function updateStat(statId, value) {
    const element = document.getElementById(statId);
    if (element) {
        element.textContent = value;
    }
}

/**
 * Debounce function for event handling
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = {
        BoardRenderer,
        apiCall,
        setLoading,
        setStatus,
        updateStat,
        debounce
    };
}
