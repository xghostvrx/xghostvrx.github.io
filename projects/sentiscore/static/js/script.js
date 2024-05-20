// Initialize the terminal startup sequence
window.onload = function() {
    const terminal = document.getElementById('terminal');
    const input = document.getElementById('input');
    var commands = [
        'Initializing terminal...',
        'Loading system files...',
        'Loading user files...',
        'Starting services...',
        'Starting sentiscore...',
        'System Ready. Type "start" to begin.',
    ];
    var i = 0;

    function typeCommand() {
        if (i < commands.length) {
            var div = document.createElement('div');
            div.textContent = commands[i];
            terminal.appendChild(div);
            i++;
            setTimeout(typeCommand, 1000);  // Wait 1 second before typing the next command
        } else {
            // Enable the input field after the startup sequence
            input.disabled = false;
            input.focus();
        }
    }

    typeCommand();

    // Listen for the 'Enter' key
    input.addEventListener('keydown', function(event) {
        if (event.key === 'Enter') {
            // Prevent the form from being submitted
            event.preventDefault();

            // Append the user's input to the terminal
            var div = document.createElement('div');
            div.textContent = '> ' + input.value;
            terminal.appendChild(div);

            // Clear the input field
            input.value = '';
        }
    });
};
